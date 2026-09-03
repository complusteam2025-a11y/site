/* ==========================================================================
   COM+ — Script principal
   Menu burger, fermeture au clic, animations au scroll, formulaire, footer
   ========================================================================== */

document.addEventListener('DOMContentLoaded', function () {

  /* ---------- Année courante dans le footer ---------- */
  var yearEl = document.getElementById('year');
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }

  /* ---------- Menu burger (mobile) ---------- */
  var burger = document.getElementById('burger');
  var nav = document.getElementById('nav');

  function closeMenu() {
    burger.classList.remove('active');
    nav.classList.remove('active');
    burger.setAttribute('aria-expanded', 'false');
  }

  if (burger && nav) {
    burger.addEventListener('click', function () {
      var isActive = nav.classList.toggle('active');
      burger.classList.toggle('active', isActive);
      burger.setAttribute('aria-expanded', String(isActive));
    });

    // Ferme le menu quand on clique sur un lien
    nav.querySelectorAll('.nav-link').forEach(function (link) {
      link.addEventListener('click', closeMenu);
    });
  }

  /* ---------- Animation "fade-in" au scroll ---------- */
  var fadeEls = document.querySelectorAll('.fade-in');

  if ('IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15 });

    fadeEls.forEach(function (el) { observer.observe(el); });
  } else {
    // Fallback : pas d'IntersectionObserver, on affiche tout directement
    fadeEls.forEach(function (el) { el.classList.add('visible'); });
  }

  /* ---------- Bouton retour en haut ---------- */
  var backToTop = document.getElementById('backToTop');

  function toggleBackToTop() {
    if (window.scrollY > 500) {
      backToTop.classList.add('visible');
    } else {
      backToTop.classList.remove('visible');
    }
  }

  window.addEventListener('scroll', toggleBackToTop, { passive: true });
  toggleBackToTop();

  if (backToTop) {
    backToTop.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ---------- Formulaire de contact (interface uniquement, pas de backend) ---------- */
  var contactForm = document.getElementById('contactForm');
  var confirmation = document.getElementById('formConfirmation');

  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();

      if (!contactForm.checkValidity()) {
        contactForm.reportValidity();
        return;
      }

      var nameInput = document.getElementById('name');
      var firstName = nameInput.value.trim().split(' ')[0] || '';

      confirmation.textContent = 'Merci ' + firstName + ' ! Votre message a bien été envoyé. Notre équipe vous recontactera très vite.';
      confirmation.classList.add('show');

      contactForm.reset();

      setTimeout(function () {
        confirmation.classList.remove('show');
      }, 6000);
    });
  }

});
