// Mobile nav
const nav = document.querySelector(".nav");
const toggle = document.querySelector(".nav-toggle");
toggle.addEventListener("click", () => {
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

document.getElementById("year").textContent = new Date().getFullYear();
