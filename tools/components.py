"""Reusable HTML building blocks for the generated pages."""

ICONS = {
    "shield": '<path d="M12 3 4 6v5.5c0 4.6 3.4 8.6 8 9.5 4.6-.9 8-4.9 8-9.5V6l-8-3Z"/><path d="m9 12 2 2 4-4"/>',
    "chart": '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
    "users": '<circle cx="9" cy="8" r="3.2"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6M15 14.5c3 0 6 2 6 5.5"/>',
    "database": '<ellipse cx="12" cy="5" rx="8" ry="3"/><path d="M4 5v14c0 1.7 3.6 3 8 3s8-1.3 8-3V5M4 12c0 1.7 3.6 3 8 3s8-1.3 8-3"/>',
    "plug": '<path d="M9 2v6M15 2v6M6 8h12v4a6 6 0 0 1-12 0V8ZM12 18v4"/>',
    "lock": '<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
    "card": '<rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20M6 15h4"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.5 3.8 5.5 3.8 9s-1.3 6.5-3.8 9c-2.5-2.5-3.8-5.5-3.8-9S9.5 5.5 12 3Z"/>',
    "bolt": '<path d="M13 2 4 14h7l-1 8 9-12h-7l1-8Z"/>',
    "book": '<path d="M4 4h6a3 3 0 0 1 3 3v14a2 2 0 0 0-2-2H4V4ZM20 4h-4a3 3 0 0 0-3 3v14a2 2 0 0 1 2-2h5V4Z"/>',
    "video": '<rect x="2" y="6" width="14" height="12" rx="2"/><path d="m16 10 6-3v10l-6-3"/>',
    "briefcase": '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M2 13h20"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m2 6 10 7 10-7"/>',
    "phone": '<path d="M5 3h4l2 5-2.5 1.5a11 11 0 0 0 6 6L16 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 5a2 2 0 0 1 2-2Z"/>',
    "pin": '<path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12Z"/><circle cx="12" cy="10" r="2.5"/>',
    "help": '<circle cx="12" cy="12" r="9"/><path d="M9.5 9a2.5 2.5 0 1 1 3.5 2.3c-.7.3-1 .9-1 1.7M12 17h.01"/>',
    "doc": '<path d="M6 2h8l5 5v15H6V2Z"/><path d="M14 2v5h5M9 13h7M9 17h7"/>',
    "target": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
    "star": '<path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9L12 3Z"/>',
    "wallet": '<path d="M3 7a2 2 0 0 1 2-2h13v4"/><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M16 13.5h2"/>',
    "refresh": '<path d="M20 11a8 8 0 0 0-14.9-3M4 4v4h4M4 13a8 8 0 0 0 14.9 3M20 20v-4h-4"/>',
    "eye": '<path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12Z"/><circle cx="12" cy="12" r="3"/>',
    "plane": '<path d="M10 14 3 11l1-2 8 1 4-5c1-1 3-1 3 1l-4 5 1 8-2 1-3-7-3 3v3l-2 1-1-4-4-1 1-2h3l3-3Z"/>',
    "percent": '<path d="M19 5 5 19"/><circle cx="7" cy="7" r="2.5"/><circle cx="17" cy="17" r="2.5"/>',
    "check": '<path d="m5 12 5 5 9-10"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "heart": '<path d="M12 21s-8-5-8-11a4.5 4.5 0 0 1 8-2.8A4.5 4.5 0 0 1 20 10c0 6-8 11-8 11Z"/>',
    "coffee": '<path d="M4 8h13v5a6 6 0 0 1-12 0V8ZM17 9h1.5a2.5 2.5 0 0 1 0 5H17M7 2v3M11 2v3M15 2v3"/>',
    "home": '<path d="M3 11 12 3l9 8M5 9.5V21h14V9.5"/>',
    "cookie": '<path d="M12 3a9 9 0 1 0 9 9 3 3 0 0 1-3-3 3 3 0 0 1-3-3 3 3 0 0 1-3-3Z"/><path d="M8 12h.01M12 16h.01M15 13h.01M9 8h.01"/>',
    "tag": '<path d="M3 3h8l10 10-8 8L3 11V3Z"/><circle cx="7.5" cy="7.5" r="1.5"/>',
    "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/>',
}


def icon(name):
    return f'<svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[name]}</svg>'


def page_hero(crumb, eyebrow, title, lead, actions="", aside="", cls=""):
    return f"""<section class="container page-hero {cls}">
      <div class="ph-copy">
        <p class="crumbs"><a href="index.html">Home</a> <span>/</span> {crumb}</p>
        <p class="eyebrow orange">{eyebrow}</p>
        <h1>{title}</h1>
        <p class="ph-lead">{lead}</p>
        {f'<div class="btn-group">{actions}</div>' if actions else ''}
      </div>
      <div class="ph-aside">{aside}</div>
      <svg class="sparkle sparkle-lg" viewBox="0 0 40 40" aria-hidden="true"><path d="M20 0c1.6 10.6 8.8 17.8 20 20-11.2 2.2-18.4 9.4-20 20-1.6-10.6-8.8-17.8-20-20C11.2 17.8 18.4 10.6 20 0Z"/></svg>
    </section>"""


def cta_pair(label, href, circle_cls="btn-orange", sm=False):
    size = " btn-sm" if sm else ""
    return (f'<a href="{href}" class="btn btn-orange{size}">{label}</a>'
            f'<a href="{href}" class="btn-circle {circle_cls}" aria-label="{label}">↗</a>')


def section(inner, cls="", sid=""):
    sid_attr = f' id="{sid}"' if sid else ""
    return f'<section class="section {cls}"{sid_attr}>\n<div class="container">\n{inner}\n</div>\n</section>'


def head(eyebrow, title, lead=""):
    lead_html = f'<p class="lead">{lead}</p>' if lead else ""
    return f"""<div class="section-head">
      <div><p class="eyebrow">{eyebrow}</p><h2>{title}</h2></div>
      {lead_html}
    </div>"""


def cards(items, cols=3, variant=""):
    """items: (icon, title, text[, link_label, link_href])"""
    out = []
    for it in items:
        ic, title, text = it[:3]
        link = f'<a class="card-link" href="{it[4]}">{it[3]} →</a>' if len(it) > 3 else ""
        out.append(f"""<article class="card {variant} reveal">
        <span class="ic">{icon(ic)}</span>
        <h3>{title}</h3>
        <p>{text}</p>{link}
      </article>""")
    return f'<div class="grid cols-{cols}">{"".join(out)}</div>'


def stats(items):
    """items: (value, suffix, text, style) where style is orange|black|light"""
    icons = {"orange": "users", "black": "card", "light": "globe"}
    out = []
    for value, suffix, text, style in items:
        out.append(f"""<article class="stat stat-{style} reveal">
        <span class="stat-icon">{icon(icons[style])}</span>
        <h3><span class="count" data-target="{value}">0</span><sup>{suffix}</sup></h3>
        <p>{text}</p>
      </article>""")
    return f'<div class="stats stats-even">{"".join(out)}</div>'


def steps(items):
    out = "".join(
        f'<li class="step reveal"><span class="step-num">0{i}</span><h3>{t}</h3><p>{d}</p></li>'
        for i, (t, d) in enumerate(items, 1)
    )
    return f'<ol class="steps">{out}</ol>'


def faq(items, group=""):
    out = "".join(
        f'<details class="faq-item"><summary>{q}<span class="go">+</span></summary><p>{a}</p></details>'
        for q, a in items
    )
    title = f'<h3 class="faq-group-title">{group}</h3>' if group else ""
    return f'<div class="faq" data-faq-group>{title}{out}</div>'


def split(visual, copy, reverse=False):
    rev = " reverse" if reverse else ""
    return f'<div class="split{rev}"><div class="split-visual">{visual}</div><div class="split-copy">{copy}</div></div>'


def perks(items):
    return '<ul class="perks">' + "".join(
        f'<li><span class="perk-ic">{icon(ic)}</span>{text}</li>' for ic, text in items
    ) + "</ul>"


def cta_band(title, text, label="Get Started", href="signup.html"):
    return f"""<section class="section cta-section"><div class="container">
      <div class="cta-band reveal">
        <div><h2>{title}</h2><p>{text}</p></div>
        <div class="btn-group"><a href="{href}" class="btn btn-white">{label}</a><a href="{href}" class="btn-circle btn-ghost" aria-label="{label}">↗</a></div>
      </div>
    </div></section>"""


def avatar(initials, color, cls="av"):
    return f'<span class="{cls}" style="--c:{color}">{initials}</span>'


def quote(text, name, role, initials, color):
    return f"""<figure class="quote-card reveal">
      <span class="quote-mark" aria-hidden="true">❞</span>
      <blockquote>“{text}”</blockquote>
      <figcaption>{avatar(initials, color)}<div><b>{name}</b><small>{role}</small></div></figcaption>
    </figure>"""


def mini_card(brand="finshield", variant="orange", name="Ralph Edwards"):
    return f"""<div class="mini-card mini-{variant}" aria-hidden="true">
      <span class="card-brand">{brand}</span><span class="chip"></span>
      <span class="mini-num">•••• •••• •••• 4589</span><span class="mini-name">{name}</span>
    </div>"""


def field(label, name, type_="text", placeholder="", required=True, attrs=""):
    req = " required" if required else ""
    if type_ == "textarea":
        control = f'<textarea id="{name}" name="{name}" placeholder="{placeholder}"{req} {attrs}></textarea>'
    elif type_ == "select":
        opts = "".join(f"<option>{o}</option>" for o in placeholder.split("|"))
        control = f'<select id="{name}" name="{name}"{req} {attrs}>{opts}</select>'
    else:
        control = f'<input id="{name}" name="{name}" type="{type_}" placeholder="{placeholder}"{req} {attrs} />'
    return f'<div class="field"><label for="{name}">{label}</label>{control}</div>'


def form(fields, button, success_title, success_text, cls=""):
    return f"""<form class="form {cls}" data-fake-submit novalidate>
      <div class="form-body">{fields}
        <button type="submit" class="btn btn-orange">{button}</button>
      </div>
      <div class="form-success" role="status">
        <span class="ic">{icon("check")}</span>
        <h3>{success_title}</h3><p>{success_text}</p>
      </div>
    </form>"""


def prose_page(sections, updated):
    toc = "".join(f'<a href="#s{i}">{t}</a>' for i, (t, _) in enumerate(sections, 1))
    body = "".join(f'<h2 id="s{i}">{i}. {t}</h2>{c}' for i, (t, c) in enumerate(sections, 1))
    return f"""<section class="section"><div class="container legal">
      <aside class="toc"><p class="eyebrow">On this page</p>{toc}</aside>
      <article class="prose"><p class="updated">Last updated: {updated}</p>{body}</article>
    </div></section>"""
