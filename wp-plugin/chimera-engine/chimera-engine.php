<?php
/**
 * Plugin Name: Chimera Engine
 * Description: Support for engine-built landing pages: llms.txt, Markdown copies, robots.txt rules, schema, hub listing, IndexNow, page design, lead form, AI-traffic and lead tracking.
 * Version: 1.3.0
 * Requires at least: 6.0
 * Requires PHP: 7.4
 * Author: The Chimera AI
 */

if (!defined('ABSPATH')) {
    exit;
}

const CHIMERA_ENGINE_VERSION = '1.3.0';

/* -------------------------------------------------------------
 * 1. Page fields the engine writes through the REST API
 * ----------------------------------------------------------- */
add_action('init', function () {
    $can_edit = function () {
        return current_user_can('edit_pages');
    };
    $fields = [
        '_chimera_engine'           => 'boolean',
        '_chimera_query'            => 'string',
        '_chimera_markdown'         => 'string',
        '_chimera_schema'           => 'string',
        '_chimera_meta_description' => 'string',
        '_chimera_eyebrow'          => 'string',
        // Yoast SEO
        '_yoast_wpseo_title'        => 'string',
        '_yoast_wpseo_metadesc'     => 'string',
        '_yoast_wpseo_focuskw'      => 'string',
        // Rank Math
        'rank_math_title'           => 'string',
        'rank_math_description'     => 'string',
        'rank_math_focus_keyword'   => 'string',
    ];
    foreach ($fields as $key => $type) {
        register_post_meta('page', $key, [
            'type'          => $type,
            'single'        => true,
            'show_in_rest'  => true,
            'auth_callback' => $can_edit,
        ]);
    }
});

function chimera_is_engine_page($post_id = null)
{
    $post_id = $post_id ?: get_queried_object_id();
    return $post_id && (bool) get_post_meta($post_id, '_chimera_engine', true);
}

function chimera_engine_pages($limit = -1)
{
    return get_posts([
        'post_type'      => 'page',
        'post_status'    => 'publish',
        'posts_per_page' => $limit,
        'meta_key'       => '_chimera_engine',
        'meta_value'     => '1',
        'orderby'        => 'date',
        'order'          => 'DESC',
    ]);
}

/* -------------------------------------------------------------
 * 2. REST: list engine pages (for the engine's own bookkeeping)
 * ----------------------------------------------------------- */
function chimera_indexnow_key()
{
    $key = get_option('chimera_indexnow_key');
    if (!$key || !preg_match('/^[a-f0-9]{32}$/', $key)) {
        $key = bin2hex(random_bytes(16));
        update_option('chimera_indexnow_key', $key, false);
    }
    return $key;
}

add_action('rest_api_init', function () {
    register_rest_route('chimera/v1', '/indexnow', [
        'methods'             => 'GET',
        'permission_callback' => function () {
            return current_user_can('edit_pages');
        },
        'callback'            => function () {
            return ['key' => chimera_indexnow_key()];
        },
    ]);
    register_rest_route('chimera/v1', '/pages', [
        'methods'             => 'GET',
        'permission_callback' => function () {
            return current_user_can('edit_pages');
        },
        'callback'            => function () {
            return array_map(function ($p) {
                return [
                    'id'    => $p->ID,
                    'slug'  => $p->post_name,
                    'url'   => get_permalink($p),
                    'title' => get_the_title($p),
                    'query' => get_post_meta($p->ID, '_chimera_query', true),
                    'date'  => get_the_date('Y-m-d', $p),
                ];
            }, chimera_engine_pages());
        },
    ]);
});

/* -------------------------------------------------------------
 * 3. <head>: schema, meta description fallback, Markdown link
 * ----------------------------------------------------------- */
add_action('wp_head', function () {
    if (!is_singular('page') || !chimera_is_engine_page()) {
        return;
    }
    $id = get_queried_object_id();

    $schema = json_decode((string) get_post_meta($id, '_chimera_schema', true), true);
    if (is_array($schema)) {
        echo '<script type="application/ld+json">' . wp_json_encode($schema, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE) . "</script>\n";
    }

    // Off by default: WordPress/Elementor already print a description from the excerpt,
    // which the engine sets. Turn on with add_filter('chimera_output_meta_description', '__return_true').
    $has_seo_plugin = defined('WPSEO_VERSION') || class_exists('RankMath');
    $desc = get_post_meta($id, '_chimera_meta_description', true);
    if (!$has_seo_plugin && $desc && apply_filters('chimera_output_meta_description', false)) {
        echo '<meta name="description" content="' . esc_attr($desc) . "\">\n";
    }

    $slug = get_post_field('post_name', $id);
    echo '<link rel="alternate" type="text/markdown" href="' . esc_url(home_url("/$slug.md")) . "\">\n";
}, 5);

/* -------------------------------------------------------------
 * 4. /llms.txt, /llms-full.txt and /{slug}.md
 * ----------------------------------------------------------- */
add_action('parse_request', function () {
    $path = trim((string) wp_parse_url($_SERVER['REQUEST_URI'] ?? '', PHP_URL_PATH), '/');
    $home = trim((string) wp_parse_url(home_url('/'), PHP_URL_PATH), '/');
    if ($home && strpos($path, $home) === 0) {
        $path = trim(substr($path, strlen($home)), '/');
    }

    $indexnow = get_option('chimera_indexnow_key');
    if ($indexnow && $path === $indexnow . '.txt') {
        chimera_send_text($indexnow);
    }
    if ($path === 'llms.txt' || $path === 'llms-full.txt') {
        chimera_send_text(chimera_llms_txt($path === 'llms-full.txt'));
    }
    if (preg_match('#^([a-z0-9-]+)\.md$#', $path, $m)) {
        $page = get_page_by_path($m[1], OBJECT, 'page');
        if ($page && $page->post_status === 'publish' && chimera_is_engine_page($page->ID)) {
            $md = get_post_meta($page->ID, '_chimera_markdown', true);
            if ($md) {
                chimera_send_text($md, 'text/markdown');
            }
        }
    }
});

function chimera_send_text($body, $type = 'text/plain')
{
    status_header(200);
    header("Content-Type: $type; charset=utf-8");
    header('X-Robots-Tag: noindex'); // the HTML page is the one that should rank
    header('Cache-Control: public, max-age=3600');
    echo $body;
    exit;
}

function chimera_llms_txt($full = false)
{
    $name = get_bloginfo('name');
    $desc = get_bloginfo('description');
    $out  = "# $name\n\n";
    if ($desc) {
        $out .= "> $desc\n\n";
    }
    $out .= "Main site: " . home_url('/') . "\n\n";

    $core = get_posts([
        'post_type'      => 'page',
        'post_status'    => 'publish',
        'posts_per_page' => 30,
        'meta_query'     => [['key' => '_chimera_engine', 'compare' => 'NOT EXISTS']],
        'orderby'        => 'menu_order',
        'order'          => 'ASC',
    ]);
    if ($core) {
        $out .= "## Core pages\n\n";
        foreach ($core as $p) {
            $out .= '- [' . get_the_title($p) . '](' . get_permalink($p) . ")\n";
        }
        $out .= "\n";
    }

    $pages = chimera_engine_pages();
    if ($pages) {
        $out .= "## Guides and answers\n\n";
        foreach ($pages as $p) {
            $slug = $p->post_name;
            $line = '- [' . get_the_title($p) . '](' . home_url("/$slug.md") . ')';
            $d    = get_post_meta($p->ID, '_chimera_meta_description', true);
            $out .= $d ? "$line: $d\n" : "$line\n";
        }
        $out .= "\n";
        if ($full) {
            foreach ($pages as $p) {
                $md = get_post_meta($p->ID, '_chimera_markdown', true);
                if ($md) {
                    $out .= "\n---\n\n" . $md . "\n";
                }
            }
        }
    }
    return $out;
}

/* -------------------------------------------------------------
 * 5. robots.txt (only applies when there is no physical robots.txt file)
 * ----------------------------------------------------------- */
add_filter('robots_txt', function ($output, $public) {
    if (!$public) {
        return $output; // "Discourage search engines" is on; leave it alone
    }
    $bots = ['GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'PerplexityBot', 'Perplexity-User',
             'ClaudeBot', 'Claude-SearchBot', 'Google-Extended', 'Applebot-Extended', 'Bingbot',
             'CCBot', 'Meta-ExternalAgent', 'DuckAssistBot'];
    $extra = "\n# AI search and answer engines\n";
    foreach ($bots as $bot) {
        $extra .= "User-agent: $bot\nAllow: /\nDisallow: /wp-admin/\n\n";
    }
    if (strpos($output, 'Sitemap:') === false) {
        $sitemap = defined('WPSEO_VERSION') || class_exists('RankMath')
            ? home_url('/sitemap_index.xml') : home_url('/wp-sitemap.xml');
        $extra .= "Sitemap: $sitemap\n";
    }
    $extra .= "# LLM-readable index: " . home_url('/llms.txt') . "\n";
    return $output . $extra;
}, 20, 2);

/* -------------------------------------------------------------
 * 6. Keep engine pages out of automatic menus; list them in a hub
 * ----------------------------------------------------------- */
add_filter('wp_list_pages_excludes', function ($exclude) {
    return array_merge((array) $exclude, wp_list_pluck(chimera_engine_pages(), 'ID'));
});

function chimera_guide_cards($limit = -1)
{
    $pages = chimera_engine_pages($limit);
    if (!$pages) {
        return '<p>New guides are on the way.</p>';
    }
    $html = '<ul class="cp-guidegrid">';
    foreach ($pages as $p) {
        $d   = get_post_meta($p->ID, '_chimera_meta_description', true);
        $tag = get_post_meta($p->ID, '_chimera_eyebrow', true) ?: 'GEO guide';
        $html .= '<li><a class="cp-guide" href="' . esc_url(get_permalink($p)) . '">'
            . '<span class="cp-eyebrow">' . esc_html($tag) . '</span>'
            . '<strong>' . esc_html(get_the_title($p)) . '</strong>'
            . ($d ? '<span class="cp-guide-desc">' . esc_html($d) . '</span>' : '')
            . '<span class="cp-arrow" aria-hidden="true">→</span></a></li>';
    }
    return $html . '</ul>';
}

add_shortcode('chimera_hub', function ($atts) {
    $atts = shortcode_atts(['limit' => 500], $atts);
    $count = count(chimera_engine_pages());
    return '<div class="cp">'
        . '<section class="cp-hub-hero cp-hero"><p class="cp-eyebrow">GEO Insights · ' . (int) $count . ' guides</p>'
        . '<h2>Answers on getting found, cited and recommended by AI</h2>'
        . '<p>Practical guides on Generative Engine Optimization: how ChatGPT, Gemini, Perplexity, Claude and Google AI Overviews choose which brands to name, and what to change on your site.</p>'
        . '<div class="cp-actions"><a class="cp-btn cp-btn--primary" href="' . esc_url(home_url('/#audit')) . '">Get your free AI visibility audit</a>'
        . '<a class="cp-btn cp-btn--ghost" href="' . esc_url(home_url('/')) . '">Back to the homepage</a></div></section>'
        . chimera_guide_cards((int) $atts['limit'])
        . '</div>';
});

/* Homepage: a "Latest GEO guides" section after the page content links to the newest guides. */
add_filter('the_content', function ($content) {
    if (!is_front_page() || !in_the_loop() || !is_main_query() || !apply_filters('chimera_home_guides', true)) {
        return $content;
    }
    static $done = false;
    if ($done || !chimera_engine_pages(1)) {
        return $content;
    }
    $done = true;
    return $content . '<div class="cp"><section class="cp-home-guides"><div class="cp-sec-head"><div>'
        . '<p class="cp-eyebrow">GEO Insights</p><h2>Latest guides on AI search</h2></div>'
        . '<p class="cp-sec-lead">How AI engines decide who to recommend, and what you can do about it. <a href="' . esc_url(home_url('/insights/')) . '">See all guides →</a></p></div>'
        . chimera_guide_cards(6) . '</section></div>';
}, 999);

/* -------------------------------------------------------------
 * 7. Page design and lead form (assets/ and includes/leads.php)
 * ----------------------------------------------------------- */
require_once __DIR__ . '/includes/leads.php';

add_filter('body_class', function ($classes) {
    if (is_singular('page') && chimera_is_engine_page()) {
        $classes[] = 'chimera-engine-page';
    }
    return $classes;
});

add_action('wp_enqueue_scripts', function () {
    $base = plugin_dir_url(__FILE__) . 'assets/';
    $post = get_post();
    $hub  = $post && has_shortcode((string) $post->post_content, 'chimera_hub');
    if ((is_singular('page') && chimera_is_engine_page()) || $hub || is_front_page()) {
        wp_enqueue_style('chimera-pages', $base . 'chimera-pages.css', [], CHIMERA_ENGINE_VERSION);
    }
    // The form can appear on any page (engine pages, or anywhere [chimera_lead_form] is used).
    wp_register_script('chimera-lead', $base . 'chimera-lead.js', [], CHIMERA_ENGINE_VERSION, true);
});

/* -------------------------------------------------------------
 * 8. Traffic source + lead tracking (every page, so leads that
 *    start on an engine page and convert elsewhere still count)
 * ----------------------------------------------------------- */
add_action('wp_footer', function () {
    $ai = [
        'chatgpt'    => ['chatgpt.com', 'chat.openai.com'],
        'perplexity' => ['perplexity.ai'],
        'gemini'     => ['gemini.google.com', 'bard.google.com'],
        'copilot'    => ['copilot.microsoft.com', 'bing.com/chat'],
        'claude'     => ['claude.ai'],
        'deepseek'   => ['chat.deepseek.com'],
        'meta_ai'    => ['meta.ai'],
        'you'        => ['you.com'],
    ];
    ?>
<script id="chimera-engine-tracking">
(function () {
  var AI = <?php echo wp_json_encode($ai); ?>;
  var KEY = 'chimera_first_touch';
  function store() { try { return window.localStorage; } catch (e) { return null; } }
  function detectAI(text) {
    text = (text || '').toLowerCase();
    for (var k in AI) { for (var i = 0; i < AI[k].length; i++) { if (text.indexOf(AI[k][i]) !== -1) return k; } }
    return '';
  }
  var params = new URLSearchParams(location.search);
  var touch = {
    landing: location.pathname,
    referrer: document.referrer || '',
    utm_source: params.get('utm_source') || '',
    utm_medium: params.get('utm_medium') || '',
    utm_campaign: params.get('utm_campaign') || ''
  };
  touch.ai_engine = detectAI(touch.utm_source) || detectAI(touch.referrer);
  var s = store(), first = null;
  try { first = JSON.parse((s && s.getItem(KEY)) || 'null'); } catch (e) {}
  if (!first && (touch.referrer.indexOf(location.hostname) === -1 || touch.utm_source)) {
    first = touch;
    try { s && s.setItem(KEY, JSON.stringify(first)); } catch (e) {}
  }
  first = first || touch;

  function send(name, extra) {
    var p = Object.assign({ ai_engine: first.ai_engine || '(none)', first_landing: first.landing }, extra || {});
    if (typeof window.gtag === 'function') window.gtag('event', name, p);
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push(Object.assign({ event: name }, p));
  }
  if (touch.ai_engine) send('ai_referral', { ai_engine: touch.ai_engine });

  // Put the source into hidden form fields named chimera_* if your form has them.
  function fill() {
    ['landing', 'referrer', 'utm_source', 'utm_medium', 'utm_campaign', 'ai_engine'].forEach(function (k) {
      document.querySelectorAll('input[name="chimera_' + k + '"], input[name$="[chimera_' + k + ']"]').forEach(function (el) { el.value = first[k] || ''; });
    });
  }
  document.addEventListener('DOMContentLoaded', fill); fill();

  var sent = false;
  function lead(form) { if (sent) return; sent = true; send('<?php echo esc_js(apply_filters('chimera_lead_event', 'generate_lead')); ?>', { form: form || 'unknown', page: location.pathname }); }
  document.addEventListener('chimera_lead_success', function () { lead('chimera'); });
  document.addEventListener('wpcf7mailsent', function () { lead('cf7'); });
  document.addEventListener('submit_success', function () { lead('elementor'); });
  document.addEventListener('fluentform_submission_success', function () { lead('fluentform'); });
  if (window.jQuery) {
    jQuery(document).on('wpformsAjaxSubmitSuccess', function () { lead('wpforms'); });
    jQuery(document).on('gform_confirmation_loaded', function () { lead('gravityforms'); });
    jQuery(document).on('submit_success', function () { lead('elementor'); });
  }
})();
</script>
    <?php
}, 99);
