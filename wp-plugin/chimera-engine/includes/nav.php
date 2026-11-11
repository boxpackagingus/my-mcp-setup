<?php
/**
 * Adds a "Blog" link after "FAQ" in the homepage menus.
 *
 * The homepage header, mobile menu and footer are drawn by the chimera-geo-home app, which has its
 * menu built in. This script adds the link once the app has rendered, and again if the app redraws.
 */
if (!defined('ABSPATH')) {
    exit;
}

add_action('wp_footer', function () {
    if (!is_front_page()) {
        return;
    }
    $url = esc_url(home_url('/blog/'));
    ?>
<script id="chimera-blog-nav">
(function () {
  var URL = <?php echo wp_json_encode($url); ?>;
  function add() {
    // Desktop header, mobile drawer and footer lists: every #faq link inside them.
    var faqs = document.querySelectorAll('.hdr__nav a[href="#faq"], .drawer nav a[href="#faq"], footer li > a[href="#faq"]');
    faqs.forEach(function (faq) {
      var holder = faq.parentElement.tagName === 'LI' ? faq.parentElement : faq;
      var next = holder.nextElementSibling;
      if (next && next.getAttribute('data-chimera-blog') === '1') return;
      var clone = holder.cloneNode(true);
      clone.setAttribute('data-chimera-blog', '1');
      var link = clone.tagName === 'A' ? clone : clone.querySelector('a');
      link.setAttribute('href', URL);
      // Replace the label, keeping any number badge the mobile menu shows.
      var badge = link.querySelector('span');
      if (badge) {
        badge.textContent = String(faq.closest('nav').querySelectorAll('a[href^="#"]:not([href="#scan"]), a[data-chimera-blog]').length + 1).padStart(2, '0');
        link.lastChild.textContent = 'Blog';
      } else {
        link.textContent = 'Blog';
      }
      holder.parentNode.insertBefore(clone, holder.nextSibling);
    });
  }
  // Footer service lists: turn plain items into links to the matching guides.
  var FOOT = <?php echo wp_json_encode(array(
      'AI Visibility Audit'     => home_url('/ai-visibility-audit/'),
      'Content Structuring'     => home_url('/how-to-write-content-for-ai-search/'),
      'Schema and llms.txt'     => home_url('/schema-markup-for-ai-search/'),
      'Citation Optimization'   => home_url('/how-ai-search-engines-choose-sources/'),
      'SEO and Local SEO'       => home_url('/seo-company-orange-county/'),
      'Paid Marketing'          => home_url('/geo-vs-ppc/'),
      'Web Development'         => home_url('/core-web-vitals-for-local-businesses/'),
      'Branding and Design'     => home_url('/how-to-get-brand-mentions-for-ai-search/'),
  )); ?>;
  function footerLinks() {
    document.querySelectorAll('footer li').forEach(function (li) {
      if (li.querySelector('a')) return;
      var label = li.textContent.trim();
      if (!FOOT[label]) return;
      var a = document.createElement('a');
      a.href = FOOT[label];
      // Move the existing text into the link rather than replacing it, so the app's own nodes stay intact.
      while (li.firstChild) a.appendChild(li.firstChild);
      li.appendChild(a);
    });
  }
  var _add = add;
  add = function () { _add(); footerLinks(); };
  var timer;
  new MutationObserver(function () { clearTimeout(timer); timer = setTimeout(add, 50); })
    .observe(document.body, { childList: true, subtree: true });
  document.addEventListener('DOMContentLoaded', add);
  setTimeout(add, 500);
})();
</script>
    <?php
}, 100);
