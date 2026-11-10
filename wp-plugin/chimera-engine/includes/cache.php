<?php
/**
 * Keeps page caches (LiteSpeed Cache) from serving stale copies of the files the engine changes.
 *
 * - Sitemaps, robots.txt and the llms files are never cached, so Google and AI crawlers always see every page.
 * - When an engine page is published or updated, the homepage and the guides hub are purged.
 * - After the plugin is installed or updated, the whole cache is purged once.
 * Every call is a do_action(), so nothing happens if LiteSpeed Cache is not active.
 */

if (!defined('ABSPATH')) {
    exit;
}

function chimera_is_live_file_request()
{
    $path = strtok($_SERVER['REQUEST_URI'] ?? '', '?');
    return (bool) preg_match('#/(wp-sitemap[^/]*\.(xml|xsl)|robots\.txt|llms(-full)?\.txt)$#', (string) $path);
}

add_action('init', function () {
    if (chimera_is_live_file_request()) {
        do_action('litespeed_control_set_nocache', 'Chimera Engine: sitemaps and AI files are always live');
        if (!headers_sent()) {
            header('X-LiteSpeed-Cache-Control: no-cache');
        }
    }
}, 1);

function chimera_live_urls()
{
    return [
        home_url('/'),
        home_url('/insights/'),
        home_url('/wp-sitemap.xml'),
        home_url('/wp-sitemap-posts-page-1.xml'),
        home_url('/robots.txt'),
        home_url('/llms.txt'),
        home_url('/llms-full.txt'),
    ];
}

function chimera_purge_live_urls()
{
    foreach (chimera_live_urls() as $url) {
        do_action('litespeed_purge_url', $url);
    }
}

// Purge after an engine page is saved (runs after its meta is written).
add_action('wp_after_insert_post', function ($post_id, $post) {
    if ($post instanceof WP_Post && $post->post_type === 'page' && chimera_is_engine_page($post_id)) {
        chimera_purge_live_urls();
    }
}, 20, 2);

// One full purge after install or update, so old cached copies disappear right away.
add_action('init', function () {
    if (get_option('chimera_engine_version') !== CHIMERA_ENGINE_VERSION) {
        do_action('litespeed_purge_all');
        update_option('chimera_engine_version', CHIMERA_ENGINE_VERSION, false);
    }
}, 20);

// Lets the engine purge the cache after a publishing run.
add_action('rest_api_init', function () {
    register_rest_route('chimera/v1', '/purge-cache', [
        'methods'             => 'POST',
        'permission_callback' => function () {
            return current_user_can('edit_pages');
        },
        'callback'            => function () {
            // Elementor keeps its own copies of rendered templates and CSS; clear them first.
            $elementor = false;
            if (class_exists('\\Elementor\\Plugin') && isset(\Elementor\Plugin::$instance->files_manager)) {
                \Elementor\Plugin::$instance->files_manager->clear_cache();
                $elementor = true;
            }
            do_action('litespeed_purge_all');
            return ['purged' => true, 'litespeed_active' => defined('LSCWP_V'), 'elementor_cleared' => $elementor];
        },
    ]);
});
