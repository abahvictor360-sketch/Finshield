// Mobile nav
const nav = document.querySelector(".nav");
const toggle = document.querySelector(".nav-toggle");
toggle?.addEventListener("click", () => {
  const open = nav.classList.toggle("open");
  toggle.setAttribute("aria-expanded", open);
});
nav.querySelectorAll(".nav-links a").forEach((a) =>
  a.addEventListener("click", () => nav.classList.remove("open"))
);

// Feature accordion
const features = document.querySelectorAll(".feature-item");
features.forEach((item) => {
  const activate = () => {
    features.forEach((f) => {
      f.classList.toggle("active", f === item);
      f.querySelector(".go").textContent = f === item ? "↗" : "→";
    });
  };
  item.addEventListener("click", activate);
  item.addEventListener("keydown", (e) => {
    if (e.key === "Enter" || e.key === " ") { e.preventDefault(); activate(); }
  });
});

// Generic slider helper
function slider(slides, { dots, prev, next, interval } = {}) {
  let i = 0, timer;
  const show = (n) => {
    i = (n + slides.length) % slides.length;
    slides.forEach((s, k) => s.classList.toggle("active", k === i));
    dots?.forEach((d, k) => d.classList.toggle("active", k === i));
  };
  const restart = () => {
    if (!interval) return;
    clearInterval(timer);
    timer = setInterval(() => show(i + 1), interval);
  };
  dots?.forEach((d, k) => d.addEventListener("click", () => { show(k); restart(); }));
  prev?.addEventListener("click", () => { show(i - 1); restart(); });
  next?.addEventListener("click", () => { show(i + 1); restart(); });
  restart();
}

slider(document.querySelectorAll(".benefit-slide"), {
  dots: document.querySelectorAll(".dots button"),
  interval: 6000,
});
slider(document.querySelectorAll(".t-slide"), {
  prev: document.querySelector(".t-prev"),
  next: document.querySelector(".t-next"),
  interval: 8000,
});

// Count-up numbers + reveal on scroll
const countUp = (el) => {
  const target = +el.dataset.target;
  const start = performance.now();
  const dur = 1400;
  const step = (t) => {
    const p = Math.min((t - start) / dur, 1);
    el.textContent = Math.round(target * (1 - Math.pow(1 - p, 3)));
    if (p < 1) requestAnimationFrame(step);
  };
  requestAnimationFrame(step);
};

const io = new IntersectionObserver((entries) => {
  entries.forEach((e) => {
    if (!e.isIntersecting) return;
    e.target.classList.add("in");
    e.target.querySelectorAll?.(".count").forEach(countUp);
    if (e.target.classList.contains("count")) countUp(e.target);
    io.unobserve(e.target);
  });
}, { threshold: 0.3 });

document.querySelectorAll(".reveal").forEach((el) => io.observe(el));
document.querySelectorAll(".count").forEach((el) => {
  if (!el.closest(".reveal")) io.observe(el);
});

const yearEl = document.getElementById("year");
if (yearEl) yearEl.textContent = new Date().getFullYear();

// ---------- Subpage interactions ----------
const $$ = (sel, root = document) => [...root.querySelectorAll(sel)];

// Forms: validate natively, show inline errors, then swap in the success message
$$("form[data-fake-submit]").forEach((form) => {
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    let ok = true;
    $$("input, select, textarea", form).forEach((el) => {
      if (el.closest(".login-mode") && el.closest(".signup-only")) return;
      const wrap = el.closest(".field, .check");
      wrap?.querySelector(".error")?.remove();
      wrap?.classList.remove("invalid");
      if (!el.checkValidity()) {
        ok = false;
        wrap?.classList.add("invalid");
        if (wrap?.classList.contains("field")) {
          const msg = document.createElement("span");
          msg.className = "error";
          msg.textContent = el.validationMessage;
          wrap.appendChild(msg);
        }
      }
    });
    if (!ok) {
      form.querySelector(".invalid input, .invalid select, .invalid textarea")?.focus();
      return;
    }
    form.classList.add("sent");
  });
});

// Category filters (blog, careers, integrations)
$$("[data-filter-group]").forEach((group) => {
  const items = $$("[data-cat]", group.nextElementSibling);
  $$("button", group).forEach((btn) =>
    btn.addEventListener("click", () => {
      $$("button", group).forEach((b) => b.classList.toggle("active", b === btn));
      const cat = btn.dataset.filter;
      items.forEach((it) => it.classList.toggle("hidden", cat !== "All" && it.dataset.cat !== cat));
    })
  );
});

// Buttons that flip to a confirmed state (Register, Connect, Download…)
$$("[data-toggle-text]").forEach((btn) => {
  const original = btn.textContent;
  btn.addEventListener("click", (e) => {
    e.preventDefault();
    const on = btn.classList.toggle("on");
    btn.textContent = on ? btn.dataset.toggleText : original;
  });
});

// Dialogs (guide downloads)
$$("[data-open-dialog]").forEach((btn) =>
  btn.addEventListener("click", () => {
    const dlg = document.getElementById(btn.dataset.openDialog);
    const title = dlg.querySelector("[data-dialog-title]");
    if (title && btn.dataset.title) title.textContent = btn.dataset.title;
    dlg.querySelector("form")?.classList.remove("sent");
    dlg.showModal();
  })
);
$$("dialog").forEach((dlg) => {
  dlg.addEventListener("click", (e) => { if (e.target === dlg) dlg.close(); });
  $$("[data-close-dialog]", dlg).forEach((b) => b.addEventListener("click", () => dlg.close()));
});

// Cashback calculator
const spend = document.getElementById("spend");
if (spend) {
  const fmt = (n) => "$" + Math.round(n).toLocaleString("en-US");
  const update = () => {
    const v = +spend.value;
    document.getElementById("spend-out").textContent = fmt(v);
    document.getElementById("cb-month").textContent = fmt(v * 0.02);
    document.getElementById("cb-year").textContent = fmt(v * 0.02 * 12);
  };
  spend.addEventListener("input", update);
  update();
}

// Pricing: monthly / yearly toggle
$$("[data-billing]").forEach((btn) =>
  btn.addEventListener("click", () => {
    const mode = btn.dataset.billing;
    $$("[data-billing]").forEach((b) => b.classList.toggle("active", b === btn));
    $$(".price [data-m]").forEach((el) => (el.textContent = el.dataset[mode]));
  })
);

// Sign up / log in
const authForm = document.querySelector("[data-auth-form]");
if (authForm) {
  const submit = authForm.querySelector("button[type=submit]");
  $$("[data-auth]").forEach((tab) =>
    tab.addEventListener("click", () => {
      const login = tab.dataset.auth === "login";
      $$("[data-auth]").forEach((t) => t.classList.toggle("active", t === tab));
      authForm.classList.toggle("login-mode", login);
      authForm.classList.remove("sent");
      submit.textContent = login ? submit.dataset.loginLabel : submit.dataset.signupLabel;
      authForm.querySelector(".form-success h3").textContent = login ? "Welcome back!" : "Welcome to Finshield!";
      authForm.querySelector(".form-success p").textContent = login
        ? "You're signed in. Redirecting you to your dashboard…"
        : "Check your inbox to verify your email and finish setting up your account.";
    })
  );
  if (location.hash === "#login") document.querySelector('[data-auth="login"]').click();

  const pw = authForm.querySelector("#password");
  authForm.querySelector(".pw-toggle").addEventListener("click", (e) => {
    const show = pw.type === "password";
    pw.type = show ? "text" : "password";
    e.target.textContent = show ? "Hide" : "Show";
    e.target.setAttribute("aria-label", show ? "Hide password" : "Show password");
  });
  const bar = authForm.querySelector(".pw-meter span");
  pw.addEventListener("input", () => {
    const v = pw.value;
    const score = [v.length >= 8, /[A-Z]/.test(v), /\d/.test(v), /[^A-Za-z0-9]/.test(v)].filter(Boolean).length;
    bar.style.width = (v ? Math.max(score, 1) * 25 : 0) + "%";
    bar.style.background = ["#d91c1c", "#d91c1c", "#f59e0b", "#84cc16", "#2fbf71"][score];
  });
}

// Cookie preferences (per-browser convenience only)
const prefs = document.querySelector("[data-cookie-prefs]");
if (prefs) {
  const KEY = "finshield-cookies";
  let saved = {};
  try { saved = JSON.parse(localStorage.getItem(KEY)) || {}; } catch {}
  $$("[data-cookie]", prefs).forEach((el) => (el.checked = !!saved[el.dataset.cookie]));
  prefs.querySelector("[data-cookie-save]").addEventListener("click", () => {
    const data = {};
    $$("[data-cookie]", prefs).forEach((el) => (data[el.dataset.cookie] = el.checked));
    try { localStorage.setItem(KEY, JSON.stringify(data)); } catch {}
    prefs.querySelector(".saved-msg").textContent = "Preferences saved.";
  });
}

// Help center search
const helpSearch = document.getElementById("help-search");
if (helpSearch) {
  const noResults = document.querySelector(".no-results");
  helpSearch.addEventListener("input", () => {
    const q = helpSearch.value.trim().toLowerCase();
    let any = false;
    $$("[data-faq-group]").forEach((group) => {
      let groupAny = false;
      $$(".faq-item", group).forEach((item) => {
        const match = !q || item.textContent.toLowerCase().includes(q);
        item.classList.toggle("hidden", !match);
        if (match && q) item.open = true;
        if (!q) item.open = false;
        groupAny ||= match;
      });
      group.classList.toggle("hidden", !groupAny);
      any ||= groupAny;
    });
    noResults.hidden = any;
  });
}
