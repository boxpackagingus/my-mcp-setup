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

add_action('template_redirect', function () {
    if (is_admin() || wp_doing_ajax() || (defined('REST_REQUEST') && REST_REQUEST) || is_feed()) {
        return;
    }
    if (!is_singular('page')) {
        return;
    }
    $id = get_queried_object_id();
    if (!(chimera_is_engine_page($id) || chimera_draws_own_title($id))) {
        return;
    }
    ob_start('chimera_fix_header_footer');
}, 1);
