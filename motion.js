// Finshield motion: intro animations, scroll reveals, parallax, sticky nav,
// scroll progress and magnetic buttons. Everything is skipped for users who
// prefer reduced motion, so content is always visible without it.
(() => {
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];
  const root = document.documentElement;

  // ---------- Sticky nav + progress bar (safe with reduced motion) ----------
  const nav = document.querySelector(".nav");
  const header = nav?.closest("header");
  const bar = document.createElement("div");
  bar.className = "scroll-progress";
  bar.setAttribute("aria-hidden", "true");
  document.body.prepend(bar);

  let lastY = scrollY;
  const onNavScroll = () => {
    const y = scrollY;
    const max = root.scrollHeight - innerHeight;
    bar.style.transform = `scaleX(${max > 0 ? y / max : 0})`;
    if (!nav) return;
    const stuck = y > (header?.offsetHeight || 400) * 0.35;
    if (stuck && !document.body.classList.contains("nav-stuck")) {
      root.style.setProperty("--nav-h", nav.offsetHeight + "px");
    }
    document.body.classList.toggle("nav-stuck", stuck);
    const menuOpen = nav.classList.contains("open");
    document.body.classList.toggle("nav-hidden", stuck && y > lastY + 4 && !menuOpen);
    if (y < lastY - 4) document.body.classList.remove("nav-hidden");
    lastY = y;
  };
  addEventListener("scroll", onNavScroll, { passive: true });
  onNavScroll();

  if (reduce) {
    document.body.classList.add("loaded", "no-motion");
    return;
  }
  document.body.classList.add("motion");

  // ---------- Split headings into words ----------
  const splitWords = (el) => {
    let i = 0;
    const walk = (node) => {
      [...node.childNodes].forEach((child) => {
        if (child.nodeType === Node.TEXT_NODE) {
          const frag = document.createDocumentFragment();
          child.textContent.split(/(\s+)/).forEach((part) => {
            if (!part) return;
            if (/^\s+$/.test(part)) return frag.append(" ");
            const w = document.createElement("span");
            w.className = "w";
            const inner = document.createElement("span");
            inner.textContent = part;
            inner.style.setProperty("--i", i++);
            w.append(inner);
            frag.append(w);
          });
          child.replaceWith(frag);
        } else if (child.nodeType === Node.ELEMENT_NODE && child.tagName !== "BR") {
          walk(child);
        }
      });
    };
    walk(el);
    el.classList.add("split-words");
  };

  // ---------- Intro (above the fold) ----------
  const heroH1 = document.querySelector(".hero h1, .page-hero h1");
  if (heroH1) splitWords(heroH1);
  const intro = [
    ".hero-copy p", ".hero-copy .btn-group", ".hero-steps li", ".active-users",
    ".page-hero .crumbs", ".page-hero .eyebrow", ".page-hero .ph-lead", ".page-hero .btn-group",
  ];
  let d = 0.35;
  intro.forEach((sel) => $$(sel).forEach((el) => {
    el.classList.add("intro");
    el.style.setProperty("--d", (d += 0.08).toFixed(2) + "s");
  }));
  $$(".card-stack, .page-hero .ph-aside, .sparkle").forEach((el, k) => {
    el.classList.add("intro-pop");
    el.style.setProperty("--d", (0.3 + k * 0.12).toFixed(2) + "s");
  });
  requestAnimationFrame(() => requestAnimationFrame(() => document.body.classList.add("loaded")));

  // ---------- Scroll reveals ----------
  const REVEAL = [
    ".section-head .eyebrow", ".section-head .lead", ".split-copy > *:not(h2)", ".benefit-copy > *:not(.benefit-slides)",
    ".stat", ".card", ".plan", ".tile", ".post-card", ".faq-item", ".job", ".event", ".int-tile", ".step",
    ".member", ".case", ".quote-card", ".guide", ".timeline li", ".feature-item", ".perks li", ".cert",
    ".partner-stat", ".partner-cta", ".t-head", ".t-slides", ".t-nav", ".footer-cta", ".footer-col", ".socials",
    ".auth-panel", ".auth-side", ".filters", ".billing-toggle", ".table-wrap", ".cta-band", ".article > *:not(.prose)",
    ".prose > *", ".toc", ".featured-post", ".no-results",
  ].join(",");
  const LEFT = ".split-visual, .benefit-visual";

  $$(REVEAL).forEach((el) => {
    if (el.closest(".page-hero, .hero-grid, .invoice, dialog")) return;
    el.classList.add("reveal");
  });
  $$(LEFT).forEach((el) => {
    el.classList.add("reveal", el.closest(".split.reverse") ? "from-right" : "from-left");
  });

  // Stagger siblings that reveal together
  const groups = new Map();
  $$(".reveal").forEach((el) => {
    const key = el.parentElement;
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(el);
  });
  groups.forEach((els) => els.forEach((el, k) => el.style.setProperty("--d", Math.min(k * 0.08, 0.48) + "s")));

  // Section headings rise word by word
  $$(".section-head h2, .split-copy h2, .benefit-slide.active h2, .cta-band h2, .footer-cta h2, .partner-cta h4").forEach((h) => {
    if (!h.closest(".page-hero")) { splitWords(h); h.classList.add("reveal-words"); }
  });

  // Once revealed, drop the reveal classes so hover transforms work again
  const settle = (el) => {
    const done = (e) => {
      if (e.target !== el || e.propertyName !== "transform") return;
      el.removeEventListener("transitionend", done);
      el.classList.remove("reveal", "in", "from-left", "from-right");
      el.style.removeProperty("--d");
    };
    el.addEventListener("transitionend", done);
  };

  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (!e.isIntersecting) return;
      e.target.classList.add("in");
      if (e.target.classList.contains("reveal")) settle(e.target);
      io.unobserve(e.target);
    });
  }, { threshold: 0.12, rootMargin: "0px 0px -6% 0px" });
  $$(".reveal, .reveal-words").forEach((el) => io.observe(el));

  // ---------- Footer wordmark: letters rise in ----------
  const giant = document.querySelector(".giant");
  if (giant) {
    const text = giant.textContent.trim();
    giant.textContent = "";
    [...text].forEach((ch, k) => {
      const s = document.createElement("span");
      s.textContent = ch;
      s.style.setProperty("--i", k);
      giant.append(s);
    });
    new IntersectionObserver(([e], obs) => {
      if (e.isIntersecting) { giant.classList.add("in"); obs.disconnect(); }
    }, { threshold: 0.25 }).observe(giant);
  }

  // ---------- Parallax ----------
  const PARALLAX = [
    [".card-stack", 0.12], [".hero-cards", 0.1], [".sparkle-lg", 0.35], [".sparkle-sm", 0.55],
    [".invoice", -0.08], [".benefit-cards", 0.1, 8], [".ph-aside", 0.08], [".v-front", -0.06],
    [".shield-visual", 0.12], [".book-stack", 0.1], [".phone-mock", -0.06], [".quote-block", 0.05],
    [".giant", 0.1], [".savings-visual", -0.05], [".alert-visual", 0.06],
  ];
  const items = [];
  PARALLAX.forEach(([sel, speed, rot = 0]) => $$(sel).forEach((el) => items.push({ el, speed, rot })));

  // Each element rests at its designed position when it is first seen:
  // at page load for above-the-fold items, otherwise when centred on screen.
  const measure = () => {
    items.forEach((it) => {
      it.el.style.translate = "";
      const r = it.el.getBoundingClientRect();
      const center = r.top + scrollY + r.height / 2;
      it.rest = Math.max(0, center - innerHeight / 2);
      it.top = r.top + scrollY;
      it.bottom = r.bottom + scrollY;
    });
  };

  let ticking = false;
  const update = () => {
    ticking = false;
    const y = scrollY;
    const vh = innerHeight;
    const scale = innerWidth < 760 ? 0.5 : 1;
    items.forEach(({ el, speed, rot, rest, top, bottom }) => {
      if (bottom - y < -300 || top - y > vh + 300) return;
      const offset = (rest - y) * speed * scale;
      el.style.translate = `0 ${offset.toFixed(1)}px`;
      if (rot) el.style.rotate = `${((offset / vh) * rot * 4).toFixed(2)}deg`;
    });
  };
  const request = () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } };
  addEventListener("scroll", request, { passive: true });
  addEventListener("resize", () => { measure(); request(); });
  addEventListener("load", () => { measure(); update(); });
  measure();
  update();

  // ---------- Magnetic buttons (pointer devices only) ----------
  if (matchMedia("(hover: hover) and (pointer: fine)").matches) {
    $$(".btn-circle, .btn, .t-nav button, .go").forEach((el) => {
      el.addEventListener("pointermove", (e) => {
        const r = el.getBoundingClientRect();
        const x = (e.clientX - r.left - r.width / 2) * 0.25;
        const y = (e.clientY - r.top - r.height / 2) * 0.35;
        el.style.translate = `${x.toFixed(1)}px ${y.toFixed(1)}px`;
      });
      el.addEventListener("pointerleave", () => { el.style.translate = ""; });
    });

    // Subtle 3D tilt on the hero card stack
    $$(".hero-grid, .page-hero").forEach((zone) => {
      const target = zone.querySelector(".card-stack .card-orange, .hero-cards .mini-card:last-child");
      if (!target) return;
      zone.addEventListener("pointermove", (e) => {
        const r = zone.getBoundingClientRect();
        const x = (e.clientX - r.left) / r.width - 0.5;
        const y = (e.clientY - r.top) / r.height - 0.5;
        target.style.setProperty("--tx", (x * 14).toFixed(1) + "deg");
        target.style.setProperty("--ty", (-y * 14).toFixed(1) + "deg");
      });
      zone.addEventListener("pointerleave", () => {
        target.style.setProperty("--tx", "0deg");
        target.style.setProperty("--ty", "0deg");
      });
    });
  }
})();
