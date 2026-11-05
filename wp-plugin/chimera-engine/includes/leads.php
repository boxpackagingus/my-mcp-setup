<?php
/**
 * Lead form: renders the audit form, saves every lead as a private record,
 * and emails it to the address in the "chimera_lead_email" option.
 */

if (!defined('ABSPATH')) {
    exit;
}

const CHIMERA_LEAD_EMAIL_DEFAULT = 'zaroon@thechimeramarketing.com';

function chimera_lead_email()
{
    $to = get_option('chimera_lead_email', CHIMERA_LEAD_EMAIL_DEFAULT);
    return apply_filters('chimera_lead_email', is_email($to) ? $to : CHIMERA_LEAD_EMAIL_DEFAULT);
}

/* Private record for every lead (only administrators can see them). */
add_action('init', function () {
    register_post_type('chimera_lead', [
        'labels'          => ['name' => 'Leads', 'singular_name' => 'Lead', 'menu_name' => 'Chimera Leads'],
        'public'          => false,
        'show_ui'         => true,
        'show_in_menu'    => true,
        'menu_icon'       => 'dashicons-email-alt',
        'supports'        => ['title', 'editor', 'custom-fields'],
        'capability_type' => 'chimera_lead',
        'capabilities'    => [
            'edit_post' => 'manage_options', 'read_post' => 'manage_options', 'delete_post' => 'manage_options',
            'edit_posts' => 'manage_options', 'edit_others_posts' => 'manage_options',
            'publish_posts' => 'manage_options', 'read_private_posts' => 'manage_options',
            'delete_posts' => 'manage_options', 'create_posts' => 'do_not_allow',
        ],
        'map_meta_cap'    => false,
    ]);
});

const CHIMERA_BUDGETS = ['Not sure yet', 'Under $2,000 / month', '$2,000–$5,000 / month', '$5,000–$10,000 / month', '$10,000+ / month'];

/* ---------- The form ---------- */
function chimera_lead_form_html($variant = 'inline')
{
    static $n = 0;
    $n++;
    $id      = 'chimera-lead-' . $n;
    $action  = esc_url(admin_url('admin-post.php'));
    $page_id = get_queried_object_id();
    $thanks  = isset($_GET['lead']) && $_GET['lead'] === 'thanks';
    wp_enqueue_script('chimera-lead');

    $budgets = '';
    foreach (CHIMERA_BUDGETS as $b) {
        $budgets .= '<option value="' . esc_attr($b) . '">' . esc_html($b) . '</option>';
    }

    ob_start(); ?>
<form class="cp-form cp-form--<?php echo esc_attr($variant); ?>" id="<?php echo esc_attr($id); ?>" method="post" action="<?php echo $action; ?>" novalidate>
  <input type="hidden" name="action" value="chimera_lead">
  <input type="hidden" name="chimera_page_id" value="<?php echo (int) $page_id; ?>">
  <input type="hidden" name="chimera_landing" value="">
  <input type="hidden" name="chimera_referrer" value="">
  <input type="hidden" name="chimera_utm_source" value="">
  <input type="hidden" name="chimera_utm_medium" value="">
  <input type="hidden" name="chimera_utm_campaign" value="">
  <input type="hidden" name="chimera_ai_engine" value="">
  <input type="hidden" name="chimera_elapsed" value="">
  <div class="cp-hp" aria-hidden="true"><label>Leave this empty <input type="text" name="company_url" tabindex="-1" autocomplete="off"></label></div>
  <div class="cp-form-grid">
    <label class="cp-field"><span>Full name *</span><input type="text" name="name" required maxlength="120" autocomplete="name" placeholder="Jane Cooper"></label>
    <label class="cp-field"><span>Work email *</span><input type="email" name="email" required maxlength="160" autocomplete="email" placeholder="jane@company.com"></label>
    <label class="cp-field"><span>Website *</span><input type="text" name="website" required maxlength="200" autocomplete="url" placeholder="company.com"></label>
    <label class="cp-field"><span>Company</span><input type="text" name="company" maxlength="160" autocomplete="organization" placeholder="Company name"></label>
    <label class="cp-field cp-field--wide"><span>Monthly marketing budget</span><select name="budget"><?php echo $budgets; ?></select></label>
    <label class="cp-field cp-field--wide"><span>What do you want AI search to say about you?</span><textarea name="message" rows="3" maxlength="2000" placeholder="e.g. We want ChatGPT to recommend us for luxury tent rentals in California."></textarea></label>
  </div>
  <button type="submit" class="cp-btn cp-btn--primary cp-form-submit">Get my free AI visibility audit</button>
  <p class="cp-form-note">We reply within one business day. No spam, ever.</p>
  <p class="cp-form-status" role="status" aria-live="polite"<?php echo $thanks ? '' : ' hidden'; ?>><?php echo $thanks ? 'Thanks! Your audit request is in. We\'ll be in touch within one business day.' : ''; ?></p>
</form>
    <?php
    return ob_get_clean();
}

add_shortcode('chimera_lead_form', function ($atts) {
    $atts = shortcode_atts(['variant' => 'inline'], $atts);
    return chimera_lead_form_html(sanitize_key($atts['variant']));
});

/* Engine pages carry <div class="chimera-lead" data-chimera-form="inline|full">…fallback…</div>;
   the form replaces it. With an older plugin the fallback button still shows. */
add_filter('the_content', function ($content) {
    if (strpos($content, 'data-chimera-form') === false) {
        return $content;
    }
    return preg_replace_callback(
        '#<div class="chimera-lead" data-chimera-form="(inline|full)">.*?</div>#s',
        function ($m) {
            return chimera_lead_form_html($m[1]);
        },
        $content
    );
}, 20);

/* ---------- Handling a submission ---------- */
function chimera_lead_fail($message, $code = 400)
{
    if (wp_doing_ajax() || (isset($_SERVER['HTTP_ACCEPT']) && strpos($_SERVER['HTTP_ACCEPT'], 'application/json') !== false)) {
        wp_send_json(['ok' => false, 'message' => $message], $code);
    }
    wp_die(esc_html($message), 'Form error', ['response' => $code, 'back_link' => true]);
}

function chimera_handle_lead()
{
    $wants_json = isset($_SERVER['HTTP_ACCEPT']) && strpos($_SERVER['HTTP_ACCEPT'], 'application/json') !== false;
    $p = wp_unslash($_POST);

    // Spam checks: hidden trap field, a human fill time, and a per-visitor rate limit.
    if (!empty($p['company_url'])) {
        $wants_json ? wp_send_json(['ok' => true]) : wp_safe_redirect(home_url('/'));
        exit;
    }
    $elapsed = isset($p['chimera_elapsed']) ? (int) $p['chimera_elapsed'] : 0;
    if ($elapsed > 0 && $elapsed < 2500) {
        chimera_lead_fail('That was quick! Please check your details and send again.');
    }
    $ip_key = 'chimera_lead_' . md5(($_SERVER['REMOTE_ADDR'] ?? '') . wp_salt('nonce'));
    $count  = (int) get_transient($ip_key);
    if ($count >= 5) {
        chimera_lead_fail('Too many requests from this connection. Please try again in an hour.', 429);
    }

    $lead = [
        'name'     => sanitize_text_field($p['name'] ?? ''),
        'email'    => sanitize_email($p['email'] ?? ''),
        'website'  => sanitize_text_field($p['website'] ?? ''),
        'company'  => sanitize_text_field($p['company'] ?? ''),
        'budget'   => in_array($p['budget'] ?? '', CHIMERA_BUDGETS, true) ? $p['budget'] : '',
        'message'  => sanitize_textarea_field($p['message'] ?? ''),
        'page_id'  => (int) ($p['chimera_page_id'] ?? 0),
        'landing'  => sanitize_text_field($p['chimera_landing'] ?? ''),
        'referrer' => esc_url_raw($p['chimera_referrer'] ?? ''),
        'utm_source'   => sanitize_text_field($p['chimera_utm_source'] ?? ''),
        'utm_medium'   => sanitize_text_field($p['chimera_utm_medium'] ?? ''),
        'utm_campaign' => sanitize_text_field($p['chimera_utm_campaign'] ?? ''),
        'ai_engine'    => sanitize_key($p['chimera_ai_engine'] ?? ''),
    ];
    if (!$lead['name'] || !is_email($lead['email']) || !$lead['website']) {
        chimera_lead_fail('Please add your name, a valid work email and your website.');
    }
    $page_url = $lead['page_id'] ? get_permalink($lead['page_id']) : '';
    $source   = $lead['ai_engine'] ? 'AI search: ' . $lead['ai_engine']
        : ($lead['utm_source'] ? 'UTM: ' . $lead['utm_source'] : ($lead['referrer'] ? 'Referrer: ' . $lead['referrer'] : 'Direct / unknown'));

    $lines = [
        'Name: ' . $lead['name'],
        'Email: ' . $lead['email'],
        'Website: ' . $lead['website'],
        'Company: ' . ($lead['company'] ?: '—'),
        'Budget: ' . ($lead['budget'] ?: '—'),
        '',
        'Message:',
        $lead['message'] ?: '—',
        '',
        'Submitted on: ' . ($page_url ?: home_url('/')),
        'First landing page: ' . ($lead['landing'] ?: '—'),
        'Traffic source: ' . $source,
        'Campaign: ' . (trim($lead['utm_medium'] . ' ' . $lead['utm_campaign']) ?: '—'),
        'Time: ' . wp_date('Y-m-d H:i T'),
    ];
    $body = implode("\n", $lines);

    $post_id = wp_insert_post([
        'post_type'    => 'chimera_lead',
        'post_status'  => 'private',
        'post_title'   => $lead['name'] . ' — ' . $lead['website'],
        'post_content' => $body,
    ], true);
    if (!is_wp_error($post_id)) {
        foreach ($lead as $k => $v) {
            update_post_meta($post_id, '_lead_' . $k, $v);
        }
        update_post_meta($post_id, '_lead_page_path', $page_url ? wp_parse_url($page_url, PHP_URL_PATH) : '/');
    }

    $subject = 'New AI audit request: ' . $lead['name'] . ' (' . $lead['website'] . ')';
    $headers = ['Reply-To: ' . str_replace(["\r", "\n"], '', $lead['name']) . ' <' . $lead['email'] . '>'];
    $sent    = wp_mail(chimera_lead_email(), $subject, $body . "\n\n— Sent by the Chimera Engine plugin on " . home_url('/'), $headers);
    if (!is_wp_error($post_id)) {
        update_post_meta($post_id, '_lead_mail_sent', $sent ? 'yes' : 'no');
    }
    set_transient($ip_key, $count + 1, HOUR_IN_SECONDS);

    if ($wants_json) {
        wp_send_json(['ok' => true]);
    }
    $back = wp_get_referer() ?: ($page_url ?: home_url('/'));
    wp_safe_redirect(add_query_arg('lead', 'thanks', $back) . '#get-started');
    exit;
}
add_action('admin_post_nopriv_chimera_lead', 'chimera_handle_lead');
add_action('admin_post_chimera_lead', 'chimera_handle_lead');

/* Lead counts for the engine's dashboard: numbers only, no personal details. */
add_action('rest_api_init', function () {
    register_rest_route('chimera/v1', '/leads-summary', [
        'methods'             => 'GET',
        'permission_callback' => function () {
            return current_user_can('edit_pages');
        },
        'callback'            => function ($req) {
            $days  = max(1, min(365, (int) ($req['days'] ?: 28)));
            $since = gmdate('Y-m-d H:i:s', time() - $days * DAY_IN_SECONDS);
            $ids   = get_posts(['post_type' => 'chimera_lead', 'post_status' => 'private', 'posts_per_page' => -1,
                                'fields' => 'ids', 'date_query' => [['after' => $since, 'column' => 'post_date_gmt']]]);
            $all   = (int) (wp_count_posts('chimera_lead')->private ?? 0);
            $by_page = [];
            $by_source = [];
            foreach ($ids as $id) {
                $path = get_post_meta($id, '_lead_page_path', true) ?: '/';
                $by_page[$path] = ($by_page[$path] ?? 0) + 1;
                $src = get_post_meta($id, '_lead_ai_engine', true) ?: 'other';
                $by_source[$src] = ($by_source[$src] ?? 0) + 1;
            }
            return ['days' => $days, 'total' => count($ids), 'all_time' => $all,
                    'by_page' => $by_page, 'by_ai_engine' => $by_source];
        },
    ]);
});
