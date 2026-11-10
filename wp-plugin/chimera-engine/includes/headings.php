<?php
/**
 * Clean heading order on Chimera pages: one H1, then H2 → H3 with no skipped levels.
 *
 * - Pages that draw their own title (blog posts and the /blog/ page) turn off the theme's
 *   duplicate H1 title (Hello Elementor).
 * - Small H5/H6 labels in the Elementor header and footer (logo text, footer captions) are
 *   printed as <p> with the same classes, so they look the same but stop counting as headings.
 */

if (!defined('ABSPATH')) {
    exit;
}

function chimera_draws_own_title($post_id = null)
{
    $post = get_post($post_id ?: get_queried_object_id());
    if (!$post || $post->post_type !== 'page') {
        return false;
    }
    $c = (string) $post->post_content;
    return strpos($c, 'cpb-band') !== false || strpos($c, 'cpbi-band') !== false;
}

add_filter('hello_elementor_page_title', function ($show) {
    return (is_singular('page') && chimera_draws_own_title()) ? false : $show;
}, 20);

function chimera_demote_labels($html)
{
    return preg_replace('#<h([56])(\s[^>]*)?>(.*?)</h\1>#si', '<p$2>$3</p>', $html);
}

function chimera_fix_header_footer($html)
{
    // Header: from the Elementor header block to the start of the page content.
    $h = strpos($html, 'elementor-location-header');
    if ($h !== false) {
        $h = strrpos(substr($html, 0, $h), '<');
        $end = false;
        foreach (['<main', 'class="page-content', 'data-elementor-type="wp-page"', '<article'] as $marker) {
            $pos = strpos($html, $marker, $h);
            if ($pos !== false && ($end === false || $pos < $end)) {
                $end = $pos;
            }
        }
        if ($end !== false) {
            $html = substr($html, 0, $h) . chimera_demote_labels(substr($html, $h, $end - $h)) . substr($html, $end);
        }
    }
    // Footer: from the Elementor footer block to the end of the document.
    $f = strpos($html, 'elementor-location-footer');
    if ($f !== false) {
        $f = strrpos(substr($html, 0, $f), '<');
        $html = substr($html, 0, $f) . chimera_demote_labels(substr($html, $f));
    }
    return $html;
}

/**
 * Homepage: its first big headline becomes the page's one H1, and small H5/H6 labels anywhere
 * on the page become <p> with the same classes (same look).
 */
function chimera_fix_front_page($html)
{
    $body = strpos($html, '<body');
    if ($body === false) {
        return $html;
    }
    $head = substr($html, 0, $body);
    $rest = chimera_demote_labels(substr($html, $body));
    if (!preg_match('#<h1[\s>]#i', $rest)) {
        $rest = preg_replace('#<h2(\s[^>]*elementor-heading-title[^>]*)>(.*?)</h2>#si', '<h1$1>$2</h1>', $rest, 1);
    }
    // No skipped levels: a heading may go at most one level deeper than the one before it.
    $prev = 0;
    $rest = preg_replace_callback('#<h([1-6])(\s[^>]*)?>(.*?)</h\1>#si', function ($m) use (&$prev) {
        $lvl = (int) $m[1];
        if ($prev && $lvl > $prev + 1) {
            $lvl = $prev + 1;
        }
        $prev = $lvl;
        return "<h{$lvl}{$m[2]}>{$m[3]}</h{$lvl}>";
    }, $rest);
    return $head . $rest;
}

add_action('template_redirect', function () {
    if (is_admin() || wp_doing_ajax() || (defined('REST_REQUEST') && REST_REQUEST) || is_feed()) {
        return;
    }
    if (is_front_page()) {
        ob_start('chimera_fix_front_page');
        return;
    }
    if (!is_singular('page')) {
        return;
    }
    $id   = get_queried_object_id();
    $post = get_post($id);
    $hub  = $post && has_shortcode((string) $post->post_content, 'chimera_hub');
    if (!(chimera_is_engine_page($id) || chimera_draws_own_title($id) || $hub)) {
        return;
    }
    ob_start('chimera_fix_header_footer');
}, 1);
