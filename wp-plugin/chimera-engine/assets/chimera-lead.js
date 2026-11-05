/* Chimera lead form: sends without reloading, shows a clear result, records fill time. */
(function () {
  var started = Date.now();
  function ready(fn) { document.readyState === 'loading' ? document.addEventListener('DOMContentLoaded', fn) : fn(); }

  ready(function () {
    document.querySelectorAll('form.cp-form').forEach(function (form) {
      var status = form.querySelector('.cp-form-status');
      var button = form.querySelector('.cp-form-submit');
      var label = button ? button.textContent : '';

      function show(msg, kind) {
        if (!status) return;
        status.hidden = false;
        status.textContent = msg;
        status.dataset.kind = kind;
      }

      form.addEventListener('submit', function (e) {
        var elapsed = form.querySelector('[name="chimera_elapsed"]');
        if (elapsed) elapsed.value = String(Date.now() - started);
        if (!form.checkValidity()) {
          e.preventDefault();
          form.reportValidity();
          return;
        }
        if (!window.fetch || !window.FormData) return; // falls back to a normal post
        e.preventDefault();
        if (button) { button.disabled = true; button.textContent = 'Sending…'; }
        fetch(form.action, { method: 'POST', body: new FormData(form), headers: { Accept: 'application/json' }, credentials: 'same-origin' })
          .then(function (r) { return r.json().catch(function () { return { ok: r.ok }; }); })
          .then(function (res) {
            if (res && res.ok) {
              form.classList.add('is-sent');
              show("Thanks! Your audit request is in. We'll be in touch within one business day.", 'ok');
              document.dispatchEvent(new CustomEvent('chimera_lead_success', { detail: { form: form.id } }));
            } else {
              show((res && res.message) || 'Something went wrong. Please try again.', 'error');
            }
          })
          .catch(function () { show('Could not send. Check your connection and try again.', 'error'); })
          .finally(function () { if (button) { button.disabled = false; button.textContent = label; } });
      });
    });
  });
})();
