# Finshield

A responsive multi-page website for **Finshield**, a fintech brand. It uses plain HTML, CSS and JavaScript, and the generated pages are committed, so no build step is needed to view it.

## Run locally

Open `index.html` in a browser, or serve the folder:

```bash
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Pages

| Area | Pages |
| --- | --- |
| Main nav | `index.html`, `products.html` (with pricing), `features.html`, `benefits.html` (cashback calculator), `partners.html`, `signup.html` (sign up / log in) |
| Features | `analytics.html`, `collaboration.html`, `data-management.html`, `integrations.html`, `security.html` |
| Company | `about.html`, `blog.html`, `blog-post.html`, `careers.html`, `cookie-policy.html` |
| Resources | `customers.html`, `strategic.html`, `guides.html`, `webinar.html` |
| Support & legal | `help-center.html` (searchable FAQ), `contact.html`, `terms.html`, `privacy.html`, `404.html` |

## Editing

The homepage (`index.html`) is hand-written. Every other page is generated from shared partials, so the header and footer stay consistent:

- `tools/pages.py` holds each page's content.
- `tools/components.py` holds the reusable blocks (hero, cards, stats, FAQ, forms, CTA band, …).
- `tools/build.py` holds the shared `<head>`, nav and footer.

After changing any of these, regenerate the pages:

```bash
python3 tools/build.py
```

- `styles.css` holds all styles, with breakpoints at 1000px and 760px.
- `script.js` handles the interactions: nav, accordions, sliders, count-ups, form validation, filters, pricing toggle, dialogs, help search and cookie preferences.

Forms are front-end only. They validate input and show a confirmation, but they don't send data anywhere yet.
