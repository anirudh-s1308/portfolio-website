document.addEventListener('DOMContentLoaded', () => {

  /* ── SCROLL REVEAL ──────────────────────────────
     Auto-tags common sections/cards with .reveal so
     they fade up into view — no template edits needed. */
  const autoRevealSelectors = [
    '.project-card',
    '.page-hero__title',
    '.page-hero__sub',
    '.page-hero__badges',
    '.section-title',
    '.contact-form',
  ];

  autoRevealSelectors.forEach((selector) => {
    document.querySelectorAll(selector).forEach((el, i) => {
      if (!el.classList.contains('anim')) { // don't double up on hero elements
        el.classList.add('reveal', `reveal-delay-${(i % 4) + 1}`);
      }
    });
  });

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('in-view');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll('.reveal').forEach((el) => revealObserver.observe(el));

  /* ── PROJECT CARD 3D TILT ───────────────────────── */
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  if (!prefersReducedMotion) {
    document.querySelectorAll('.project-card').forEach((card) => {
      card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        const rotateX = ((y / rect.height) - 0.5) * -6;
        const rotateY = ((x / rect.width) - 0.5) * 6;
        card.style.transform = `translateY(-4px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
      });
      card.addEventListener('mouseleave', () => {
        card.style.transform = '';
      });
    });
  }

  /* ── MOBILE MENU TOGGLE ─────────────────────────── */
  const burger = document.querySelector('.nav__burger');
  const mobileMenu = document.querySelector('.mobile-menu');
  if (burger && mobileMenu) {
    burger.addEventListener('click', () => {
      mobileMenu.classList.toggle('open');
    });
    mobileMenu.querySelectorAll('a').forEach((link) => {
      link.addEventListener('click', () => mobileMenu.classList.remove('open'));
    });
  }

  /* ── CAROUSEL ARROW SCROLL ──────────────────────── */
  document.querySelectorAll('.carousel').forEach((carousel) => {
    const wrapper = carousel.closest('.featured') || carousel.parentElement;
    const prevBtn = wrapper.querySelector('[data-carousel-prev]');
    const nextBtn = wrapper.querySelector('[data-carousel-next]');
    const scrollAmount = () => carousel.clientWidth * 0.9;

    if (prevBtn) prevBtn.addEventListener('click', () => {
      carousel.scrollBy({ left: -scrollAmount(), behavior: 'smooth' });
    });
    if (nextBtn) nextBtn.addEventListener('click', () => {
      carousel.scrollBy({ left: scrollAmount(), behavior: 'smooth' });
    });
  });

});
