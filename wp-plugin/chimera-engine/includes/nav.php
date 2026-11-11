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
  var timer;
  new MutationObserver(function () { clearTimeout(timer); timer = setTimeout(add, 50); })
    .observe(document.body, { childList: true, subtree: true });
  document.addEventListener('DOMContentLoaded', add);
  setTimeout(add, 500);
})();
</script>
    <?php
}, 100);
