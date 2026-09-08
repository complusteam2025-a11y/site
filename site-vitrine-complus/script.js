/* ==========================================================================
   COM+ — Script principal
   Header au scroll, menu burger, tilt 3D, animations au scroll, formulaire
   ========================================================================== */

document.addEventListener('DOMContentLoaded', function () {

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var canHover = window.matchMedia('(hover: hover) and (pointer: fine)').matches;

  /* ---------- Année courante dans le footer ---------- */
  var yearEl = document.getElementById('year');
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }

  /* ---------- Header : fond plein au scroll ---------- */
  var header = document.getElementById('header');

  function toggleHeader() {
    if (!header) return;
    header.classList.toggle('scrolled', window.scrollY > 40);
  }

  window.addEventListener('scroll', toggleHeader, { passive: true });
  toggleHeader();

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
    fadeEls.forEach(function (el) { el.classList.add('visible'); });
  }

  /* ---------- Tilt 3D au survol (cartes services / hub / entreprises) ---------- */
  if (canHover && !reduceMotion) {
    document.querySelectorAll('.tilt').forEach(function (card) {
      card.addEventListener('mousemove', function (e) {
        var r = card.getBoundingClientRect();
        var x = e.clientX - r.left;
        var y = e.clientY - r.top;
        var rotY = ((x - r.width / 2) / (r.width / 2)) * 8;
        var rotX = -((y - r.height / 2) / (r.height / 2)) * 8;
        card.style.transform = 'perspective(900px) rotateX(' + rotX + 'deg) rotateY(' + rotY + 'deg) translateY(-6px)';
      });

      card.addEventListener('mouseleave', function () {
        card.style.transform = '';
      });
    });
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

      confirmation.textContent = 'Merci ' + firstName + ' ! Votre demande a bien été envoyée. Notre équipe vous recontactera très vite pour connecter votre entreprise au Hub.';
      confirmation.classList.add('show');

      contactForm.reset();

      setTimeout(function () {
        confirmation.classList.remove('show');
      }, 6000);
    });
  }

});
