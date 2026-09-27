"""Content for every generated Finshield page, keyed by output filename."""
from components import (
    avatar, cards, cta_band, cta_pair, faq, field, form, head, icon, mini_card,
    page_hero, perks, prose_page, quote, section, split, stats, steps,
)

PAGES = {}


def page(filename, title, description, hero, body, active=None):
    PAGES[filename] = {
        "title": title, "description": description, "hero": hero,
        "body": body, "active": active,
    }


CARD_STACK = f"""<div class="hero-cards">
  {mini_card(variant="black", name="Jaylen Brown")}
  {mini_card(variant="silver")}
  {mini_card()}
</div>"""

GENERAL_FAQ = [
    ("Is Finshield a bank?", "Finshield is a financial technology company. Banking services are provided by our licensed partner banks, and eligible deposits are protected up to the applicable limit."),
    ("How long does it take to open an account?", "Most people are up and running in under five minutes. You'll need a valid ID and a phone that can receive verification codes."),
    ("Are there any monthly fees?", "The Basic plan is free forever. Plus and Business plans are billed monthly or yearly and can be cancelled at any time."),
    ("Can I use my card abroad?", "Yes. Finshield cards work in over 150 countries with no foreign transaction fees on Plus and Business plans."),
]

# --------------------------------------------------------------------------
# Products
# --------------------------------------------------------------------------
PLANS = [
    ("Basic", "0", "0", "For everyday spending and getting started.", False,
     ["Free virtual &amp; physical debit card", "Instant spending notifications", "1% cashback on groceries", "Access to 24K partner ATMs"]),
    ("Plus", "9.99", "95", "For people who travel, save and want more.", True,
     ["Everything in Basic", "2% cashback on all purchases", "No foreign transaction fees", "Travel insurance &amp; lounge access", "4.5% APY savings vault"]),
    ("Business", "24.99", "240", "For teams, freelancers and growing companies.", False,
     ["Everything in Plus", "Up to 25 team cards", "Spend controls &amp; approvals", "Accounting integrations", "Dedicated account manager"]),
]


def plans_html():
    out = []
    for name, monthly, yearly, desc, featured, feats in PLANS:
        badge = '<span class="badge">Most popular</span>' if featured else ""
        cls = " featured" if featured else ""
        items = "".join(f"<li>{icon('check')}{f}</li>" for f in feats)
        out.append(f"""<article class="plan{cls} reveal">
      <div class="plan-top"><h3>{name}</h3>{badge}</div>
      <p class="plan-desc">{desc}</p>
      <p class="price"><span class="cur">$</span><span data-m="{monthly}" data-y="{yearly}">{monthly}</span><small data-m="/month" data-y="/year">/month</small></p>
      <a href="signup.html" class="btn {'btn-orange' if featured else 'btn-dark'}">Choose {name}</a>
      <ul>{items}</ul>
    </article>""")
    return f"""<div class="billing-toggle" role="group" aria-label="Billing period">
      <button class="active" data-billing="m">Monthly</button><button data-billing="y">Yearly <em>save 20%</em></button>
    </div>
    <div class="plans">{''.join(out)}</div>"""


PRODUCTS = [
    ("card", "Everyday Debit Card", "A contactless debit card with real-time notifications, instant freeze and smart spending insights."),
    ("star", "Finshield Plus Card", "Premium metal card with 2% cashback, travel insurance and zero foreign transaction fees."),
    ("wallet", "Savings Vault", "Earn up to 4.5% APY, automate round-ups and set goals you can actually reach."),
    ("briefcase", "Business Account", "Team cards, expense controls and accounting sync for businesses of every size."),
]

page(
    "products.html", "Products",
    "Cards, accounts and savings products designed to secure your financial future.",
    page_hero("Products", "Our products", "Cards &amp; accounts<br />built for you",
              "From your first debit card to a full business account, every Finshield product is built on the same promise: security, speed and transparency.",
              cta_pair("Open an account", "signup.html"), CARD_STACK),
    section(head("What we offer", "One app,<br />every account", "Pick the products you need today and add more as your life changes — everything lives in a single, secure app.")
            + cards([(i, t, d, "Get started", "signup.html") for i, t, d in PRODUCTS], cols=4))
    + section(head("Pricing", "Simple, honest<br />pricing", "No hidden fees, no surprises. Switch or cancel your plan any time from the app.") + plans_html(), cls="gray", sid="pricing")
    + section(split(
        f'<div class="phone-mock reveal"><div class="pm-head"><span>Total balance</span><b>$24,580.40</b></div>{mini_card()}<ul class="pm-list"><li><span>Grocery Mart</span><b>-$64.20</b></li><li><span>Salary</span><b class="pos">+$4,200.00</b></li><li><span>Metro Transit</span><b>-$2.75</b></li></ul></div>',
        '<p class="eyebrow">The app</p><h2>Everything in<br />your pocket</h2><p class="body-lg">Track spending, move money, freeze cards and talk to a real person — all from one beautifully simple app.</p>'
        + perks([("bolt", "Instant transfers between Finshield users, free."), ("eye", "Live balances and categorized transactions."), ("lock", "Face ID, 2FA and one-tap card freeze.")])
        + f'<div class="btn-group">{cta_pair("See all features", "features.html", "btn-outline", True)}</div>'))
    + section(head("FAQ", "Product<br />questions") + faq(GENERAL_FAQ), cls="gray")
    + cta_band("Find the right plan", "Start free and upgrade whenever you're ready."),
    active="products.html",
)

# --------------------------------------------------------------------------
# Features
# --------------------------------------------------------------------------
FEATURE_ROWS = [
    ("Secure and Easy<br />Transactions", "Bank-grade encryption and biometric verification on every payment, so moving money is as safe as it is simple.", "security.html"),
    ("Real-Time Financial<br />Monitoring", "Instant alerts and live balances across all your accounts, with fraud detection that never sleeps.", "analytics.html"),
    ("Fast &amp; Easy<br />Transactions", "Send, receive and split payments in seconds — at home or abroad — with transparent, low fees.", "products.html"),
    ("Comprehensive Financial<br />Planning", "Personalised budgets, savings goals and expert guidance to help you plan for what matters most.", "strategic.html"),
    ("Shared Accounts &amp;<br />Team Spending", "Invite family or teammates, set roles and approve spending together.", "collaboration.html"),
    ("Connected<br />Integrations", "Sync with the accounting, commerce and productivity tools you already use.", "integrations.html"),
]


def feature_list():
    items = []
    for i, (title, desc, href) in enumerate(FEATURE_ROWS, 1):
        active = " active" if i == 1 else ""
        go = "↗" if i == 1 else "→"
        items.append(f"""<li class="feature-item{active}" role="tab" tabindex="0">
        <div class="container feature-row"><span class="num">0{i}</span><span class="title">{title}</span><span class="go">{go}</span></div>
        <p class="container feature-desc">{desc} <a href="{href}">Learn more →</a></p>
      </li>""")
    return f'<div class="feature-wrap"><ul class="feature-list full" role="tablist">{"".join(items)}</ul></div>'


page(
    "features.html", "Features",
    "Explore Finshield's features: secure transactions, real-time monitoring, analytics, integrations and more.",
    page_hero("Features", "Features", "All-in-one platform<br />for savings",
              "Simplify your financial life by securely connecting your accounts, automatically categorizing transactions and getting guidance when it matters.",
              cta_pair("Get started", "signup.html"),
              stats([("98", "%", "Faster transaction processing time", "orange")])),
    f'<section class="section features-page">{feature_list()}</section>'
    + section(head("Explore", "Dig into<br />each feature", "Every tool is designed to work together, so your money is organized without the busywork.")
              + cards([
                  ("chart", "Analytics", "See where your money goes with live dashboards and smart categories.", "Explore analytics", "analytics.html"),
                  ("users", "Collaboration", "Shared accounts, roles and approvals for families and teams.", "Explore collaboration", "collaboration.html"),
                  ("database", "Data Management", "Export, archive and control every piece of your financial data.", "Explore data", "data-management.html"),
                  ("plug", "Integrations", "Connect Finshield to 40+ tools you already use every day.", "Explore integrations", "integrations.html"),
                  ("shield", "Security", "256-bit encryption, 24/7 monitoring and zero liability protection.", "Explore security", "security.html"),
                  ("target", "Strategic Planning", "Goal-based plans and one-on-one sessions with our advisors.", "Explore planning", "strategic.html"),
              ]), cls="gray")
    + section(head("How it works", "Up and running<br />in three steps")
              + steps([("Select your provider", "Choose the Finshield plan that fits your life or business."),
                       ("Set up your account", "Verify your identity in minutes — no paperwork, no branch visits."),
                       ("Enjoy seamless banking", "Spend, save and grow with everything in a single app.")]))
    + cta_band("Try every feature free", "Open a Basic account in five minutes and upgrade whenever you like."),
    active="features.html",
)

# --------------------------------------------------------------------------
# Benefits
# --------------------------------------------------------------------------
CALC = """<div class="calc reveal">
  <p class="eyebrow">Cashback calculator</p>
  <label for="spend">Monthly card spend: <b id="spend-out">$1,500</b></label>
  <input type="range" id="spend" min="100" max="10000" step="100" value="1500" />
  <div class="calc-results">
    <div><small>Monthly cashback</small><b id="cb-month">$30</b></div>
    <div><small>Yearly cashback</small><b id="cb-year">$360</b></div>
  </div>
  <p class="calc-note">Based on 2% cashback with Finshield Plus.</p>
</div>"""

page(
    "benefits.html", "Benefits",
    "Cashback, travel perks, high-yield savings and round-the-clock protection with Finshield.",
    page_hero("Benefits", "Benefits", "More value from<br />every dollar",
              "Earn while you spend, save while you sleep and travel with peace of mind. Here's what you get with Finshield.",
              cta_pair("Get started", "signup.html"), CALC),
    section(split(
        f'<div class="benefit-cards static">{mini_card()}</div>',
        '<p class="eyebrow">Shopping</p><h2>Shopping on<br />international</h2>'
        + perks([("percent", "Get 2% cashback on all purchases."), ("plane", "Access exclusive travel deals and discounts on flights and hotels."), ("shield", "Includes travel insurance and purchase protection.")])))
    + section(split(
        '<div class="savings-visual reveal"><p>Savings vault</p><b>$12,840</b><div class="goal"><span style="width:72%"></span></div><small>72% of your "New home" goal</small><div class="apy">4.5% <em>APY</em></div></div>',
        '<p class="eyebrow">Saving</p><h2>Saving made<br />automatic</h2>'
        + perks([("percent", "Earn up to 4.5% APY on your savings vault."), ("refresh", "Round up every purchase and save the spare change."), ("target", "Set goals and track your progress in real time.")]),
        reverse=True), cls="gray")
    + section(split(
        f'<div class="alert-visual reveal"><div class="alert"><span class="ic">{icon("shield")}</span><div><b>Suspicious charge blocked</b><small>$489.00 · Online store · Just now</small></div></div><div class="alert ok"><span class="ic">{icon("check")}</span><div><b>Card unfrozen</b><small>You can use your card again</small></div></div></div>',
        '<p class="eyebrow">Protection</p><h2>Protection<br />that never sleeps</h2>'
        + perks([("eye", "24/7 fraud monitoring on every transaction."), ("lock", "Freeze and unfreeze your card with a single tap."), ("check", "Zero liability on unauthorised purchases.")])))
    + section(head("By the numbers", "Real rewards,<br />real people")
              + stats([("2", "%", "Cashback on every purchase with Finshield Plus", "orange"),
                       ("150", "+", "Countries with fee-free card spending", "black"),
                       ("24", "K", "Partner ATMs available worldwide", "light")]), cls="gray")
    + cta_band("Start earning today", "Upgrade to Plus and unlock every benefit."),
    active="benefits.html",
)

# --------------------------------------------------------------------------
# Partners
# --------------------------------------------------------------------------
PARTNER_NAMES = ["Apple Pay", "PayPal", "Wise", "Google Pay", "Visa", "Mastercard", "Plaid", "Stripe"]

page(
    "partners.html", "Partners",
    "Finshield partners with leading payment and technology companies. Become a partner.",
    page_hero("Partners", "Our trusted partners", "Real-time financial<br />monitoring",
              "Just like us, our partners believe in building long-term relationships with clients. Their focus on customer service aligns perfectly with our own values.",
              cta_pair("Become a partner", "#become"),
              stats([("98", "%", "Partners are happy with our collaboration, noting increased efficiency and mutual growth.", "orange")])),
    section(head("Network", "Who we<br />work with", "Finshield works with the world's leading payment networks and fintech platforms.")
            + '<div class="logo-wall">' + "".join(f'<div class="tile reveal"><span class="wordmark">{n}</span></div>' for n in PARTNER_NAMES) + "</div>")
    + section(head("Partnership types", "Ways to<br />partner with us")
              + cards([("card", "Payment partners", "Networks and wallets that help our members pay anywhere, instantly."),
                       ("home", "Banking partners", "Licensed institutions that hold deposits and issue Finshield cards."),
                       ("plug", "Technology partners", "Platforms that integrate with Finshield to extend what members can do.")], variant="dark-card"), cls="dark")
    + section(split(
        '<p class="eyebrow">Become a partner</p><h2>Creating impactful<br />solutions and lasting<br />partnerships</h2><p class="body-lg">Tell us about your company and our partnerships team will be in touch within two business days.</p>'
        + perks([("users", "Reach 500K+ engaged Finshield members."), ("chart", "Co-marketing and shared growth programs."), ("bolt", "Dedicated integration support.")]),
        form(field("Company name", "company", placeholder="Acme Inc.")
             + '<div class="form-row">' + field("Your name", "pname", placeholder="Jane Doe") + field("Work email", "pemail", "email", "jane@acme.com") + "</div>"
             + field("Partnership type", "ptype", "select", "Payment partner|Banking partner|Technology partner|Other")
             + field("Tell us more", "pmsg", "textarea", "What would you like to build together?"),
             "Let's work together", "Thanks for reaching out!", "Our partnerships team will contact you within two business days.")
    ), sid="become")
    + cta_band("Questions about partnering?", "Our team is happy to help.", "Contact us", "contact.html"),
    active="partners.html",
)

# --------------------------------------------------------------------------
# Sign up
# --------------------------------------------------------------------------
SIGNUP = f"""<section class="section auth-section"><div class="container auth">
  <div class="auth-panel">
    <div class="auth-tabs" role="tablist">
      <button class="active" data-auth="signup" role="tab">Create account</button>
      <button data-auth="login" role="tab">Log in</button>
    </div>
    <form class="form" data-fake-submit data-auth-form novalidate>
      <div class="form-body">
        <div class="form-row signup-only">{field("First name", "first", placeholder="Kelly")}{field("Last name", "last", placeholder="Williams")}</div>
        {field("Email address", "email", "email", "you@example.com")}
        <div class="field"><label for="password">Password</label>
          <div class="pw-wrap"><input id="password" name="password" type="password" placeholder="At least 8 characters" minlength="8" required />
          <button type="button" class="pw-toggle" aria-label="Show password">Show</button></div>
          <div class="pw-meter signup-only"><span></span></div>
        </div>
        <fieldset class="field signup-only"><legend>Account type</legend>
          <div class="pills">
            <label><input type="radio" name="acct" value="personal" checked /><span>Personal</span></label>
            <label><input type="radio" name="acct" value="business" /><span>Business</span></label>
          </div>
        </fieldset>
        <label class="check signup-only"><input type="checkbox" required /> <span>I agree to the <a href="terms.html">Terms of Service</a> and <a href="privacy.html">Privacy Policy</a>.</span></label>
        <a href="help-center.html" class="forgot login-only">Forgot your password?</a>
        <button type="submit" class="btn btn-orange" data-signup-label="Create account" data-login-label="Log in">Create account</button>
      </div>
      <div class="form-success" role="status">
        <span class="ic">{icon("check")}</span>
        <h3>Welcome to Finshield!</h3><p>Check your inbox to verify your email and finish setting up your account.</p>
      </div>
    </form>
  </div>
  <div class="auth-side">
    {CARD_STACK}
    {perks([("bolt", "Open an account in under 5 minutes."), ("shield", "Bank-grade security from day one."), ("percent", "No monthly fees on the Basic plan.")])}
  </div>
</div></section>"""

page(
    "signup.html", "Sign up",
    "Create your Finshield account in minutes.",
    page_hero("Sign up", "Get started", "Open your<br />account today",
              "Join 95K+ active users who trust Finshield to protect and grow their money.", cls="compact"),
    SIGNUP,
)

# --------------------------------------------------------------------------
# Feature detail pages
# --------------------------------------------------------------------------
BARS = [40, 65, 50, 80, 58, 92, 70, 60, 85, 48, 75, 66]
DASH = f"""<div class="dash reveal">
  <div class="dash-head"><div><small>Spent this month</small><b>$3,284.50</b></div><span class="tag ok">-12% vs last</span></div>
  <div class="bars">{''.join(f'<span style="--h:{h}%"{" class=hi" if i == 5 else ""}></span>' for i, h in enumerate(BARS))}</div>
  <div class="dash-foot">
    <div class="donut"></div>
    <ul class="donut-legend"><li><i class="dot-o"></i>Housing <b>45%</b></li><li><i class="dot-b"></i>Food <b>25%</b></li><li><i class="dot-g"></i>Other <b>30%</b></li></ul>
  </div>
</div>"""

page(
    "analytics.html", "Analytics",
    "Live dashboards, smart categories and insights that show exactly where your money goes.",
    page_hero("Features / Analytics", "Analytics", "Know where every<br />dollar goes",
              "Live dashboards, automatic categories and monthly insights turn your transactions into decisions.",
              cta_pair("Try analytics", "signup.html"), DASH),
    section(head("Capabilities", "Insights that<br />work for you")
            + cards([("chart", "Live dashboards", "Balances, income and spending update the moment a transaction clears."),
                     ("tag", "Smart categories", "Every transaction is categorized automatically — and learns from your edits."),
                     ("target", "Budgets &amp; goals", "Set monthly limits per category and get nudges before you overspend."),
                     ("refresh", "Recurring detection", "Spot subscriptions and bills, and cancel the ones you don't use."),
                     ("doc", "Monthly reports", "A clear summary of your month delivered to your inbox."),
                     ("eye", "Cash-flow forecasts", "See your projected balance for the next 30 days.")]))
    + section(head("Impact", "Members save<br />more with insights")
              + stats([("18", "%", "Average reduction in monthly spending after 3 months", "orange"),
                       ("12", "h", "Saved each month on manual budgeting", "black"),
                       ("40", "+", "Spending categories tracked automatically", "light")]), cls="gray")
    + cta_band("See your money clearly", "Connect your accounts and get your first insights in minutes."),
)

page(
    "collaboration.html", "Collaboration",
    "Shared accounts, roles and approvals for families, partners and teams.",
    page_hero("Features / Collaboration", "Collaboration", "Money is better<br />together",
              "Share accounts with family, give teammates their own cards and approve spending as a team — with full visibility for everyone.",
              cta_pair("Start collaborating", "signup.html"),
              f'<div class="team-card reveal"><p>Household account</p><div class="avatars big">{avatar("KW", "#f5c26b", "")}{avatar("JT", "#9bd1a6", "")}{avatar("CC", "#8fb8f0", "")}<span class="more">+2</span></div><ul class="pm-list"><li><span>Kelly requested $120</span><b class="pos">Approved</b></li><li><span>John added a card</span><b>Viewer</b></li></ul></div>'),
    section(head("Built for sharing", "Everyone on<br />the same page")
            + cards([("users", "Shared accounts", "Pool money for rent, groceries or holidays and see every transaction together."),
                     ("lock", "Roles &amp; permissions", "Owners, admins, spenders and viewers — control exactly who can do what."),
                     ("check", "Spend approvals", "Require approval above a limit and approve requests with one tap."),
                     ("card", "Individual cards", "Give each member their own card with personal limits."),
                     ("chart", "Shared budgets", "Track progress toward shared goals in real time."),
                     ("mail", "Comments &amp; receipts", "Attach receipts and leave notes on any transaction.")]))
    + section(head("Getting started", "Invite your<br />people")
              + steps([("Create a shared space", "Open a shared account or team workspace from the app."),
                       ("Invite members", "Send invites by email or link and assign each person a role."),
                       ("Spend together", "Set limits, approve requests and track everything in one place.")]), cls="gray")
    + section(quote("We run our studio's finances through Finshield now. Approvals take seconds and everyone knows where the budget stands.", "John Terry", "Founder, Northwind Studio", "JT", "#9bd1a6"))
    + cta_band("Bring your team", "Collaboration is included on Plus and Business plans."),
)

DATA_ROWS = [
    ("Transactions", "Up to 10 years", "CSV, PDF, OFX"),
    ("Statements", "Up to 10 years", "PDF"),
    ("Receipts &amp; attachments", "Unlimited", "JPG, PNG, PDF"),
    ("Categories &amp; tags", "Unlimited", "CSV, JSON"),
    ("Tax documents", "7 years", "PDF"),
]

page(
    "data-management.html", "Data Management",
    "Export, archive and control your financial data with Finshield.",
    page_hero("Features / Data Management", "Data Management", "Your data,<br />your rules",
              "Organize, export and control every piece of financial information — with privacy settings you can actually understand.",
              cta_pair("Get started", "signup.html"),
              f'<div class="export-card reveal"><span class="ic">{icon("database")}</span><b>Export ready</b><small>Transactions_2024.csv · 2.4 MB</small><div class="goal"><span style="width:100%"></span></div><a href="#" class="btn btn-orange btn-sm" data-toggle-text="Downloaded ✓">Download</a></div>'),
    section(head("Control", "Organized from<br />day one")
            + cards([("database", "Unified records", "All accounts, cards and statements searchable in one place."),
                     ("doc", "One-click exports", "Download transactions and statements in CSV, PDF or OFX."),
                     ("tag", "Custom tags &amp; rules", "Create rules that tag and file transactions automatically."),
                     ("clock", "Long-term archive", "Keep up to 10 years of history available at any time."),
                     ("eye", "Privacy controls", "Choose what's shared with partners and revoke access in one tap."),
                     ("refresh", "Automatic backups", "Encrypted, redundant backups across multiple regions.")]))
    + section(head("Retention", "What we keep<br />and for how long", "You can export or request deletion of your data at any time from Settings → Privacy.")
              + '<div class="table-wrap reveal"><table class="data-table"><thead><tr><th>Data type</th><th>Retention</th><th>Export formats</th></tr></thead><tbody>'
              + "".join(f"<tr><td>{a}</td><td>{b}</td><td>{c}</td></tr>" for a, b, c in DATA_ROWS)
              + "</tbody></table></div>", cls="gray")
    + cta_band("Take control of your data", "Open an account and see how simple it can be."),
)

INTEGRATIONS = [
    ("QuickBooks", "Accounting", "#2ca01c"), ("Xero", "Accounting", "#13b5ea"), ("FreshBooks", "Accounting", "#0075dd"),
    ("Slack", "Productivity", "#611f69"), ("Notion", "Productivity", "#111111"), ("Google Sheets", "Productivity", "#0f9d58"),
    ("Shopify", "Commerce", "#95bf47"), ("WooCommerce", "Commerce", "#7f54b3"), ("Stripe", "Commerce", "#635bff"),
    ("Zapier", "Automation", "#ff4a00"), ("Make", "Automation", "#6d00cc"), ("Gusto", "Payroll", "#f45d48"),
]


def integrations_html():
    cats = ["All"] + sorted({c for _, c, _ in INTEGRATIONS})
    filters = "".join(f'<button class="{"active" if c == "All" else ""}" data-filter="{c}">{c}</button>' for c in cats)
    tiles = "".join(f"""<article class="int-tile reveal" data-cat="{c}">
      <span class="int-logo" style="--c:{col}">{n[0]}</span>
      <h3>{n}</h3><small>{c}</small>
      <button class="btn btn-dark btn-sm" data-toggle-text="Connected ✓">Connect</button>
    </article>""" for n, c, col in INTEGRATIONS)
    return f'<div class="filters" data-filter-group>{filters}</div><div class="grid cols-4" data-filter-items>{tiles}</div>'


page(
    "integrations.html", "Integrations",
    "Connect Finshield to the accounting, commerce and productivity tools you already use.",
    page_hero("Features / Integrations", "Integrations", "Works with the<br />tools you love",
              "Sync transactions, receipts and payouts with 40+ apps — no spreadsheets or copy-paste required.",
              cta_pair("Browse integrations", "#all"),
              '<div class="orbit reveal" aria-hidden="true"><span class="orbit-core">finshield</span>'
              + "".join(f'<span class="orbit-dot" style="--i:{i};--c:{col}">{n[0]}</span>' for i, (n, _, col) in enumerate(INTEGRATIONS[:8]))
              + "</div>"),
    section(head("Directory", "All<br />integrations", "Filter by category and connect in a couple of clicks.") + integrations_html(), sid="all")
    + section(head("Developers", "Build your own", "Our REST API and webhooks let you build custom workflows on top of Finshield.")
              + cards([("plug", "REST API", "Read balances, transactions and statements with scoped API keys."),
                       ("bolt", "Webhooks", "Get notified in real time when money moves."),
                       ("lock", "OAuth 2.0", "Let members connect securely without sharing passwords.")], variant="dark-card"), cls="dark")
    + cta_band("Don't see your tool?", "Tell us what you'd like to connect next.", "Request an integration", "contact.html"),
)

page(
    "security.html", "Security",
    "How Finshield protects your money and data: encryption, monitoring and zero liability.",
    page_hero("Features / Security", "Security", "Protection you<br />can count on",
              "Your money and data are protected by multiple layers of security, monitored around the clock by our in-house team.",
              cta_pair("Open a secure account", "signup.html"),
              f'<div class="shield-visual reveal" aria-hidden="true">{icon("shield")}</div>'),
    section(head("Layers of protection", "Security at<br />every step")
            + stats([("256", "-bit", "AES encryption for all data at rest and in transit", "orange"),
                     ("24", "/7", "Fraud monitoring by our in-house security team", "black"),
                     ("0", "$", "Liability for unauthorised card transactions", "light")]))
    + section(head("How we protect you", "Built-in,<br />not bolted on")
              + cards([("lock", "Encryption everywhere", "Data is encrypted in transit with TLS 1.3 and at rest with AES-256."),
                       ("eye", "Real-time fraud detection", "Machine learning models score every transaction in milliseconds."),
                       ("shield", "Two-factor authentication", "Biometrics and one-time codes keep your account yours."),
                       ("card", "Instant card freeze", "Lost your card? Freeze it in one tap and unfreeze just as fast."),
                       ("home", "Insured deposits", "Eligible deposits are held at insured partner banks."),
                       ("users", "Security team", "Specialists who investigate and respond to threats day and night.")]), cls="gray")
    + section(head("Compliance", "Independently<br />verified", "We undergo regular third-party audits and penetration tests.")
              + '<div class="badges">' + "".join(f'<div class="cert reveal"><span class="ic">{icon("check")}</span><b>{b}</b><small>{d}</small></div>' for b, d in [
                  ("PCI DSS", "Level 1 service provider"), ("SOC 2", "Type II audited"), ("GDPR", "EU data protection"), ("ISO 27001", "Information security")]) + "</div>")
    + section(head("Stay safe", "Security<br />questions") + faq([
        ("What should I do if my card is lost or stolen?", "Freeze your card instantly in the app, then order a replacement. Any unauthorised transactions will be refunded under our zero liability policy."),
        ("Will Finshield ever ask for my password?", "Never. We will never ask for your password, PIN or full verification codes by phone, email or text."),
        ("How do I report a suspicious message?", "Forward it to security@finshield.example and delete it. Our team reviews every report."),
    ]), cls="gray")
    + cta_band("Report a security concern", "Our security team responds to every report.", "Contact security", "contact.html"),
)

# --------------------------------------------------------------------------
# Company
# --------------------------------------------------------------------------
TEAM = [("Amara Okafor", "Chief Executive Officer", "AO", "#f5c26b"), ("Daniel Reyes", "Chief Technology Officer", "DR", "#9bd1a6"),
        ("Priya Nair", "Head of Security", "PN", "#8fb8f0"), ("Liam Chen", "Head of Design", "LC", "#f09a8f")]

page(
    "about.html", "About us",
    "Finshield is on a mission to make financial security simple for everyone.",
    page_hero("About us", "About us", "Getting to<br />know Finshield",
              "We are more than just a financial service provider; we are your trusted partner in navigating the complexities of finance.",
              cta_pair("Join our team", "careers.html"),
              stats([("500", "k", "Customers within our first year of operation", "orange")])),
    section(split(
        '<div class="quote-block reveal"><span class="quote-mark">❞</span><p>Financial security shouldn\'t be a privilege. We\'re building the tools we always wished we had.</p><small>— Amara Okafor, CEO</small></div>',
        '<p class="eyebrow">Our story</p><h2>Built to make<br />money simple</h2><p class="body-lg">Finshield started in 2021 with a simple idea: everyone deserves clear, honest and secure tools to manage their money. Today we serve over half a million members in more than 30 countries.</p><p class="body-lg">We combine the protection of a traditional bank with the speed and transparency of modern technology — and we never hide fees in the fine print.</p>'))
    + section(head("In numbers", "Growing with<br />our members")
              + stats([("500", "k", "Members rely on Finshield every day", "orange"),
                       ("98", "%", "Of transactions processed in under 3 seconds", "black"),
                       ("30", "+", "Countries where our members live and work", "light")]), cls="gray")
    + section(head("Values", "What we<br />stand for")
              + cards([("shield", "Security first", "We protect our members' money and data like it's our own."),
                       ("eye", "Radical transparency", "Clear pricing, plain language and no hidden fees."),
                       ("heart", "Member obsessed", "Every decision starts with what's best for the people we serve.")]))
    + section(head("Milestones", "Our journey")
              + '<ol class="timeline">' + "".join(f'<li class="reveal"><b>{y}</b><div><h3>{t}</h3><p>{d}</p></div></li>' for y, t, d in [
                  ("2021", "Founded", "Finshield launches with a free debit card and real-time notifications."),
                  ("2022", "500K members", "We reach half a million members within our first year of operation."),
                  ("2023", "Finshield Plus", "Premium plan launches with 2% cashback and travel benefits."),
                  ("2024", "Business accounts", "Teams and companies get cards, approvals and accounting sync.")]) + "</ol>", cls="gray")
    + section(head("Leadership", "Meet the team")
              + '<div class="grid cols-4">' + "".join(f'<article class="member reveal"><div class="photo" style="--c:{c}">{i}</div><h3>{n}</h3><p>{r}</p></article>' for n, r, i, c in TEAM) + "</div>")
    + cta_band("Want to build with us?", "We're hiring across engineering, design and operations.", "View open roles", "careers.html"),
)

POSTS = [
    ("Security", "5 ways to spot a phishing message before it's too late", "Scammers are getting smarter. Here's how to recognise the warning signs.", "Sep 12, 2024", "6 min", "a"),
    ("Saving", "The 50/30/20 rule, explained for real life", "A simple budgeting framework that actually fits around your life.", "Aug 28, 2024", "5 min", "b"),
    ("Travel", "How to spend abroad without losing money on fees", "Exchange rates, dynamic conversion and other traps to avoid.", "Aug 14, 2024", "7 min", "c"),
    ("Product", "Introducing shared budgets for households", "Plan, track and hit goals together with our latest feature.", "Jul 30, 2024", "3 min", "a"),
    ("Saving", "Building an emergency fund from scratch", "How much you need, where to keep it and how to get started.", "Jul 16, 2024", "8 min", "b"),
    ("Business", "Expense policies your team will actually follow", "Simple rules and smart cards that keep spending on track.", "Jul 2, 2024", "6 min", "c"),
]


def blog_html():
    cats = ["All"] + sorted({p[0] for p in POSTS})
    filters = "".join(f'<button class="{"active" if c == "All" else ""}" data-filter="{c}">{c}</button>' for c in cats)
    grid = "".join(f"""<article class="post-card reveal" data-cat="{c}">
      <a href="blog-post.html"><div class="post-thumb thumb-{v}"><span>{c}</span></div>
      <div class="post-body"><p class="meta">{d} · {r} read</p><h3>{t}</h3><p>{e}</p></div></a>
    </article>""" for c, t, e, d, r, v in POSTS)
    return f'<div class="filters" data-filter-group>{filters}</div><div class="grid cols-3" data-filter-items>{grid}</div>'


page(
    "blog.html", "Blog",
    "News, guides and money tips from the Finshield team.",
    page_hero("Blog", "Blog", "Money tips &amp;<br />Finshield news",
              "Practical guides, product updates and stories from the team building the future of finance.",
              aside='<a href="blog-post.html" class="featured-post reveal"><div class="post-thumb thumb-a"><span>Featured</span></div><div class="post-body"><p class="meta">Sep 20, 2024 · 9 min read</p><h3>How real-time monitoring stopped $2M in fraud this year</h3></div></a>'),
    section(head("Latest", "Recent articles") + blog_html())
    + section(split(
        '<p class="eyebrow">Newsletter</p><h2>Get money tips<br />in your inbox</h2><p class="body-lg">One email a month. No spam, unsubscribe any time.</p>',
        form(field("Email address", "nl-email", "email", "you@example.com"), "Subscribe", "You're subscribed!", "Look out for our next issue at the start of the month.")), cls="gray"),
)

ARTICLE = """<section class="section"><div class="container article">
  <p class="meta">Security · Sep 20, 2024 · 9 min read</p>
  <div class="article-author"><span class="av" style="--c:#8fb8f0">PN</span><div><b>Priya Nair</b><small>Head of Security</small></div></div>
  <div class="post-thumb thumb-a article-cover"><span>Security</span></div>
  <div class="prose">
    <p class="body-lg">This year, our real-time monitoring systems flagged and stopped more than $2 million in fraudulent transactions before they ever reached our members' accounts. Here's a look at how it works.</p>
    <h2>Scoring every transaction in milliseconds</h2>
    <p>Every time a Finshield card is used, our fraud models evaluate more than 200 signals — location, merchant type, device, spending history and more — to produce a risk score in under 50 milliseconds. Low-risk payments go through instantly. High-risk ones are paused and the member is asked to confirm in the app.</p>
    <h2>Humans in the loop</h2>
    <p>Models are only part of the story. Our in-house security team reviews edge cases around the clock, investigates new fraud patterns and feeds what they learn back into the system.</p>
    <blockquote>“The best fraud prevention is invisible when things are normal, and instant when they're not.”</blockquote>
    <h2>What you can do</h2>
    <ul>
      <li>Keep notifications on so you can confirm unusual payments quickly.</li>
      <li>Freeze your card from the app whenever it's not in use.</li>
      <li>Never share one-time codes — Finshield will never ask for them.</li>
    </ul>
    <p>Want to learn more? Visit our <a href="security.html">security page</a> or <a href="contact.html">contact the security team</a>.</p>
  </div>
  <a href="blog.html" class="btn btn-dark btn-sm back-link">← Back to blog</a>
</div></section>"""

page(
    "blog-post.html", "How real-time monitoring stopped $2M in fraud",
    "A look inside Finshield's real-time fraud monitoring.",
    page_hero('<a href="blog.html">Blog</a> <span>/</span> Article', "Security", "How real-time monitoring<br />stopped $2M in fraud",
              "Inside the systems and people that keep Finshield members safe.", cls="compact"),
    ARTICLE,
)

JOBS = [
    ("Senior Backend Engineer", "Engineering", "Remote (EU)", "Full-time"),
    ("iOS Engineer", "Engineering", "London", "Full-time"),
    ("Security Analyst", "Security", "Remote (US)", "Full-time"),
    ("Product Designer", "Design", "Lagos", "Full-time"),
    ("Customer Success Specialist", "Operations", "Remote", "Full-time"),
    ("Compliance Manager", "Operations", "New York", "Full-time"),
]


def jobs_html():
    depts = ["All"] + sorted({j[1] for j in JOBS})
    filters = "".join(f'<button class="{"active" if d == "All" else ""}" data-filter="{d}">{d}</button>' for d in depts)
    rows = "".join(f"""<details class="job" data-cat="{d}">
      <summary><span class="job-title">{t}</span><span>{d}</span><span>{loc}</span><span>{ty}</span><span class="go">+</span></summary>
      <div class="job-body"><p>We're looking for a {t.lower()} to help us build secure, delightful financial products for 500K+ members. You'll work in a small, senior team with a lot of ownership.</p>
      <ul><li>Competitive salary and equity</li><li>Flexible hours and remote-friendly</li><li>Annual learning budget</li></ul>
      <a href="contact.html" class="btn btn-orange btn-sm">Apply now</a></div>
    </details>""" for t, d, loc, ty in JOBS)
    return f'<div class="filters" data-filter-group>{filters}</div><div class="jobs" data-filter-items>{rows}</div>'


page(
    "careers.html", "Careers",
    "Join Finshield and help build the future of financial security.",
    page_hero("Careers", "Careers", "Build the future<br />of finance with us",
              "We're a remote-friendly team of engineers, designers and operators on a mission to make financial security simple for everyone.",
              cta_pair("See open roles", "#roles"),
              stats([("120", "+", "Teammates across 14 countries", "orange")])),
    section(head("Why Finshield", "Perks &amp;<br />benefits")
            + cards([("heart", "Health &amp; wellbeing", "Comprehensive health cover and a monthly wellness stipend."),
                     ("home", "Work from anywhere", "Remote-first with optional hubs in London, Lagos and New York."),
                     ("book", "Learning budget", "$2,000 per year for courses, books and conferences."),
                     ("coffee", "Time off", "30 days of paid leave plus local public holidays."),
                     ("percent", "Equity for all", "Every teammate owns a piece of what we're building."),
                     ("users", "Team retreats", "Meet the whole team in person twice a year.")], cols=3), cls="gray")
    + section(head("Open roles", "Find your<br />next role", "Don't see the right fit? Send us your CV anyway — we'd love to hear from you.") + jobs_html(), sid="roles")
    + cta_band("Don't see your role?", "We're always looking for great people.", "Get in touch", "contact.html"),
)

COOKIE_PREFS = f"""<div class="cookie-prefs reveal" data-cookie-prefs>
  <h3>Your cookie preferences</h3>
  <label class="switch-row"><div><b>Strictly necessary</b><small>Required for the site to work. Always on.</small></div><input type="checkbox" checked disabled /><span class="switch"></span></label>
  <label class="switch-row"><div><b>Analytics</b><small>Help us understand how the site is used.</small></div><input type="checkbox" data-cookie="analytics" /><span class="switch"></span></label>
  <label class="switch-row"><div><b>Marketing</b><small>Used to show you relevant offers.</small></div><input type="checkbox" data-cookie="marketing" /><span class="switch"></span></label>
  <button class="btn btn-orange btn-sm" data-cookie-save>Save preferences</button>
  <p class="saved-msg" role="status"></p>
</div>"""

page(
    "cookie-policy.html", "Cookie Policy",
    "How Finshield uses cookies and how to manage your preferences.",
    page_hero("Cookie Policy", "Legal", "Cookie Policy",
              "This policy explains what cookies are, how we use them and how you can control them.", cls="compact", aside=COOKIE_PREFS),
    prose_page([
        ("What are cookies?", "<p>Cookies are small text files stored on your device when you visit a website. They help the site remember your actions and preferences over time.</p>"),
        ("How we use cookies", "<p>We use cookies to keep you signed in, remember your preferences, understand how our website is used and improve our services.</p>"),
        ("Types of cookies", "<ul><li><b>Strictly necessary</b> — required for core functionality such as security and authentication.</li><li><b>Analytics</b> — help us measure traffic and understand usage.</li><li><b>Marketing</b> — used to deliver relevant offers on other sites.</li></ul>"),
        ("Managing cookies", "<p>You can change your preferences at any time using the panel at the top of this page, or through your browser settings. Blocking some cookies may affect how the site works.</p>"),
        ("Contact", '<p>Questions about this policy? <a href="contact.html">Contact us</a>.</p>'),
    ], "September 1, 2024"),
)

# --------------------------------------------------------------------------
# Resources
# --------------------------------------------------------------------------
CASES = [
    ("Northwind Studio", "Design agency · 24 people", "Cut expense reporting time by 70% with team cards and approvals.", "70%", "less admin"),
    ("Layers", "SaaS · 60 people", "Consolidated five bank accounts into one Finshield Business workspace.", "5→1", "accounts"),
    ("Orbit Coffee", "Retail · 3 locations", "Syncs every sale and payout to their accounting tool automatically.", "12h", "saved monthly"),
]

page(
    "customers.html", "Customers",
    "Stories from the people and businesses who trust Finshield.",
    page_hero("Customers", "Customers", "Trusted by<br />500K+ members",
              "From freelancers to fast-growing teams, here's how people use Finshield to take control of their finances.",
              cta_pair("Join them", "signup.html"),
              stats([("95", "K+", "Active users every single day", "orange")])),
    section(head("Case studies", "Customer<br />stories")
            + '<div class="grid cols-3">' + "".join(f"""<article class="case reveal">
                <p class="eyebrow orange">{s}</p><h3>{n}</h3><p>{d}</p>
                <div class="case-stat"><b>{k}</b><small>{u}</small></div>
              </article>""" for n, s, d, k, u in CASES) + "</div>")
    + section(head("Reviews", "What they say<br />about us")
              + '<div class="grid cols-3">'
              + quote("Finshield has completely transformed the way I manage my finances. The real-time updates and personalized advice have been invaluable.", "Kelly Williams", "Head of Design, Layers", "KW", "#8fb8f0")
              + quote("Sending money to my family abroad used to take days. With Finshield it takes seconds, and the fees are a fraction of what I paid before.", "John Terry", "Founder, Northwind Studio", "JT", "#9bd1a6")
              + quote("The fraud alerts caught a suspicious charge before I even noticed it. I finally feel like my money is actually protected.", "Caitlin Clark", "Product Manager, Orbit", "CC", "#f5c26b")
              + "</div>", cls="gray")
    + section(head("Ratings", "Loved by<br />our members")
              + stats([("4", ".8", "Average App Store rating from 20K+ reviews", "orange"),
                       ("92", "%", "Of members would recommend Finshield", "black"),
                       ("2", "min", "Average response time from support", "light")]))
    + cta_band("Become our next success story", "Open your account in minutes."),
)

page(
    "strategic.html", "Strategic Planning",
    "Goal-based financial planning and one-on-one guidance from Finshield advisors.",
    page_hero("Strategic", "Strategic planning", "A plan for<br />what matters most",
              "Work one-on-one with a Finshield advisor to build a clear, realistic plan for your goals — from a first home to retirement.",
              cta_pair("Book a consultation", "#book"),
              '<div class="plan-visual reveal">' + "".join(f'<div class="pv-row"><span>{g}</span><div class="goal"><span style="width:{w}%"></span></div><b>{w}%</b></div>' for g, w in [("Emergency fund", 100), ("New home", 72), ("Education", 45), ("Retirement", 28)]) + "</div>"),
    section(head("Services", "Guidance for<br />every stage")
            + cards([("target", "Goal planning", "Turn big goals into monthly steps you can actually follow."),
                     ("chart", "Investment strategy", "Understand your options and build a portfolio that fits your risk."),
                     ("home", "Home buying", "Plan your deposit, compare mortgages and budget for the move."),
                     ("briefcase", "Business finances", "Cash-flow planning and growth strategy for founders."),
                     ("doc", "Tax planning", "Make the most of allowances and avoid last-minute surprises."),
                     ("heart", "Retirement", "Know how much you need and how to get there.")]))
    + section(head("Process", "How it<br />works")
              + steps([("Discovery call", "A free 30-minute call to understand your situation and goals."),
                       ("Your plan", "Your advisor builds a personalised, step-by-step plan."),
                       ("Ongoing check-ins", "Quarterly reviews keep you on track as life changes.")]), cls="gray")
    + section(split(
        '<p class="eyebrow">Book a consultation</p><h2>Talk to an<br />advisor</h2><p class="body-lg">Your first 30-minute session is free for all Finshield members.</p>'
        + perks([("clock", "Flexible times, including evenings."), ("video", "Meet by video or phone."), ("lock", "Confidential and pressure-free.")]),
        form('<div class="form-row">' + field("Full name", "sname", placeholder="Jane Doe") + field("Email", "semail", "email", "jane@example.com") + "</div>"
             + '<div class="form-row">' + field("Preferred date", "sdate", "date") + field("Topic", "stopic", "select", "Goal planning|Investments|Home buying|Business|Tax|Retirement") + "</div>"
             + field("Anything we should know?", "snote", "textarea", "Optional", required=False),
             "Book consultation", "Consultation requested!", "An advisor will confirm your time by email within one business day.")), sid="book"),
)

GUIDES = [
    ("The Complete Budgeting Guide", "Build a budget that sticks in one weekend.", "32 pages", "a"),
    ("Saving for Your First Home", "Deposits, mortgages and hidden costs explained.", "28 pages", "b"),
    ("Freelancer's Finance Playbook", "Taxes, invoicing and irregular income made simple.", "40 pages", "c"),
    ("Protecting Yourself from Fraud", "Spot scams and keep your accounts secure.", "18 pages", "b"),
    ("Investing 101", "A jargon-free introduction to growing your money.", "36 pages", "a"),
    ("Small Business Cash Flow", "Forecast, manage and improve your cash flow.", "30 pages", "c"),
]

page(
    "guides.html", "E-books &amp; Guides",
    "Free e-books and guides to help you budget, save, invest and stay secure.",
    page_hero("E-books &amp; Guides", "Resources", "E-books &amp;<br />guides",
              "Free, practical guides written by our advisors to help you make confident money decisions.",
              aside='<div class="book-stack reveal" aria-hidden="true"><div class="book thumb-c"></div><div class="book thumb-b"></div><div class="book thumb-a"><span>Budgeting<br />Guide</span></div></div>'),
    section(head("Library", "Free<br />downloads", "Enter your email and we'll send the guide straight to your inbox.")
            + '<div class="grid cols-3">' + "".join(f"""<article class="guide reveal">
                <div class="guide-cover thumb-{v}"><span>{t}</span></div>
                <div class="guide-body"><p class="meta">{icon("book")} PDF · {p}</p><h3>{t}</h3><p>{d}</p>
                <button class="btn btn-orange btn-sm" data-open-dialog="guide-dialog" data-title="{t}">Download free</button></div>
              </article>""" for t, d, p, v in GUIDES) + "</div>")
    + f"""<dialog id="guide-dialog" class="dialog">
      <button class="dialog-close" aria-label="Close" data-close-dialog>×</button>
      <p class="eyebrow orange">Free download</p><h3 data-dialog-title>Guide</h3>
      {form(field("Email address", "g-email", "email", "you@example.com"), "Send me the guide", "Check your inbox!", "Your guide is on its way.")}
    </dialog>"""
    + cta_band("Want personal advice?", "Book a free session with one of our advisors.", "Book a consultation", "strategic.html#book"),
)

WEBINARS = [
    ("14", "Oct", "Budgeting for the holidays", "Plan ahead so the festive season doesn't break the bank.", "6:00 PM GMT · 45 min", "Liam Chen"),
    ("22", "Oct", "Protecting your accounts from scams", "Our security team shares the latest fraud trends and how to stay safe.", "5:00 PM GMT · 60 min", "Priya Nair"),
    ("05", "Nov", "Finshield Business deep dive", "A live tour of team cards, approvals and accounting sync.", "4:00 PM GMT · 45 min", "Daniel Reyes"),
]
RECORDINGS = [
    ("Investing 101 for beginners", "52 min", "a"),
    ("How to build an emergency fund", "38 min", "b"),
    ("Taxes for freelancers", "47 min", "c"),
]

page(
    "webinar.html", "Webinars",
    "Live and on-demand webinars from Finshield's financial experts.",
    page_hero("Webinar", "Webinars", "Learn live from<br />our experts",
              "Free sessions on budgeting, saving, security and more — join live or watch on demand.",
              cta_pair("See upcoming", "#upcoming"),
              f'<div class="live-card reveal"><span class="live"><i></i>Live now</span>{icon("video")}<b>Q&amp;A with our advisors</b><small>312 watching</small></div>'),
    section(head("Upcoming", "Upcoming<br />sessions") + '<div class="events">' + "".join(f"""<article class="event reveal">
        <div class="event-date"><b>{d}</b><small>{m}</small></div>
        <div class="event-info"><h3>{t}</h3><p>{desc}</p><small>{time} · Hosted by {host}</small></div>
        <button class="btn btn-orange btn-sm" data-toggle-text="Registered ✓">Register</button>
      </article>""" for d, m, t, desc, time, host in WEBINARS) + "</div>", sid="upcoming")
    + section(head("On demand", "Watch<br />recordings") + '<div class="grid cols-3">' + "".join(f"""<article class="post-card reveal">
        <a href="#" data-toggle-text="Playing…"><div class="post-thumb thumb-{v} play"><span>▶</span></div>
        <div class="post-body"><p class="meta">{icon("clock")} {dur}</p><h3>{t}</h3></div></a>
      </article>""" for t, dur, v in RECORDINGS) + "</div>", cls="gray")
    + cta_band("Never miss a session", "Subscribe to get webinar invites by email.", "Subscribe", "blog.html"),
)

# --------------------------------------------------------------------------
# Support
# --------------------------------------------------------------------------
HELP_GROUPS = [
    ("Account", [
        ("How do I open an account?", "Download the app or <a href='signup.html'>sign up online</a>, verify your identity and you're ready to go in about five minutes."),
        ("How do I reset my password?", "Tap “Forgot password” on the login screen and follow the link we email you."),
        ("Can I have more than one account?", "Yes. You can open multiple savings vaults and add a business account alongside your personal one."),
    ]),
    ("Cards", [
        ("How do I freeze my card?", "Open the app, tap your card and select “Freeze”. You can unfreeze it the same way at any time."),
        ("When will my new card arrive?", "Physical cards usually arrive within 3–5 business days. You can use your virtual card immediately."),
        ("What are the ATM limits?", "Basic accounts can withdraw up to $500 per day; Plus and Business up to $2,000."),
    ]),
    ("Payments", [
        ("How long do transfers take?", "Transfers between Finshield users are instant. Bank transfers usually arrive within one business day."),
        ("Are there fees for international payments?", "Plus and Business plans have no foreign transaction fees. Basic plans pay a 1% fee."),
        ("How do I dispute a transaction?", "Tap the transaction in the app and choose “Report a problem”. We'll keep you updated at every step."),
    ]),
]

page(
    "help-center.html", "Help Center",
    "Answers to common questions about Finshield accounts, cards and payments.",
    page_hero("Help Center", "Help Center", "How can we<br />help you?",
              "Search our help articles or browse by topic below.",
              aside=f'<div class="help-search reveal">{icon("search")}<input id="help-search" type="search" placeholder="Search for answers…" aria-label="Search help articles" /></div>'),
    section('<div class="grid cols-3 topic-cards">' + "".join(f'<a href="#{g.lower()}" class="card reveal"><span class="ic">{icon(i)}</span><h3>{g}</h3><p>{len(q)} articles</p></a>' for (g, q), i in zip(HELP_GROUPS, ["users", "card", "bolt"])) + "</div>")
    + section("".join(f'<div id="{g.lower()}">{faq(q, g)}</div>' for g, q in HELP_GROUPS) + '<p class="no-results" hidden>No articles match your search. <a href="contact.html">Contact support</a> instead.</p>', cls="gray")
    + cta_band("Still need help?", "Our support team is available 24/7.", "Contact support", "contact.html"),
)

page(
    "contact.html", "Contact",
    "Get in touch with Finshield support, sales or partnerships.",
    page_hero("Contact", "Contact", "Let's talk",
              "Questions, feedback or partnership ideas — we'd love to hear from you. Our team usually replies within a few hours.", cls="compact"),
    section(split(
        '<div class="grid contact-cards">' + "".join(f'<article class="card reveal"><span class="ic">{icon(i)}</span><h3>{t}</h3><p>{d}</p><a class="card-link" href="{h}">{l} →</a></article>' for i, t, d, l, h in [
            ("mail", "Email us", "For general questions and support.", "hello@finshield.example", "mailto:hello@finshield.example"),
            ("phone", "Call us", "Mon–Fri, 8am–8pm GMT.", "+44 20 0000 0000", "tel:+442000000000"),
            ("pin", "Visit us", "12 Finsbury Square, London EC2A 1AS", "Get directions", "https://maps.google.com/?q=Finsbury+Square+London"),
            ("help", "Help Center", "Find instant answers to common questions.", "Browse articles", "help-center.html")]) + "</div>",
        '<p class="eyebrow">Send a message</p><h2>We\'re here<br />to help</h2>'
        + form('<div class="form-row">' + field("Full name", "cname", placeholder="Jane Doe") + field("Email", "cemail", "email", "jane@example.com") + "</div>"
               + field("Topic", "ctopic", "select", "General question|Account support|Sales|Partnerships|Press|Careers")
               + field("Message", "cmsg", "textarea", "How can we help?"),
               "Send message", "Message sent!", "Thanks for getting in touch. We'll reply within one business day."))),
)

page(
    "terms.html", "Terms of Service",
    "The terms that govern your use of Finshield.",
    page_hero("Terms of Service", "Legal", "Terms of Service",
              "Please read these terms carefully before using Finshield.", cls="compact"),
    prose_page([
        ("Acceptance of terms", "<p>By creating an account or using Finshield's website, app or services, you agree to these Terms of Service. If you do not agree, please do not use our services.</p>"),
        ("Eligibility", "<p>You must be at least 18 years old and a resident of a supported country to open an account. You agree to provide accurate information and keep it up to date.</p>"),
        ("Your account", "<p>You are responsible for keeping your login details secure and for all activity on your account. Notify us immediately if you suspect unauthorised access.</p>"),
        ("Fees", '<p>Fees for each plan are described on our <a href="products.html#pricing">pricing page</a>. We will give you at least 30 days\' notice of any changes.</p>'),
        ("Prohibited use", "<p>You may not use Finshield for illegal activity, fraud, money laundering or to violate the rights of others.</p>"),
        ("Termination", "<p>You can close your account at any time. We may suspend or close accounts that breach these terms, with notice where required by law.</p>"),
        ("Limitation of liability", "<p>To the extent permitted by law, Finshield is not liable for indirect or consequential losses arising from your use of our services.</p>"),
        ("Contact", '<p>Questions about these terms? <a href="contact.html">Contact us</a>.</p>'),
    ], "September 1, 2024"),
)

page(
    "privacy.html", "Privacy Policy",
    "How Finshield collects, uses and protects your personal information.",
    page_hero("Privacy Policy", "Legal", "Privacy Policy",
              "Your privacy matters. This policy explains what we collect, why, and the choices you have.", cls="compact"),
    prose_page([
        ("Information we collect", "<ul><li><b>Identity data</b> — name, date of birth and ID documents.</li><li><b>Contact data</b> — email, phone number and address.</li><li><b>Financial data</b> — transactions, balances and linked accounts.</li><li><b>Technical data</b> — device, IP address and usage information.</li></ul>"),
        ("How we use it", "<p>We use your information to provide and secure our services, verify your identity, prevent fraud, comply with legal obligations and, with your consent, send you marketing.</p>"),
        ("Sharing", "<p>We share data only with partner banks, payment networks and service providers who help us operate, and with authorities when required by law. We never sell your personal data.</p>"),
        ("Security", '<p>We protect your data with encryption, access controls and continuous monitoring. Learn more on our <a href="security.html">security page</a>.</p>'),
        ("Your rights", '<p>You can access, correct, export or request deletion of your data at any time. See <a href="data-management.html">Data Management</a> for how.</p>'),
        ("Cookies", '<p>See our <a href="cookie-policy.html">Cookie Policy</a> for details on cookies and how to manage them.</p>'),
        ("Contact", '<p>Contact our Data Protection Officer at privacy@finshield.example or via our <a href="contact.html">contact page</a>.</p>'),
    ], "September 1, 2024"),
)

page(
    "404.html", "Page not found",
    "The page you're looking for doesn't exist.",
    page_hero("404", "Error 404", "Page not<br />found",
              "Sorry, we couldn't find the page you're looking for. It may have moved or no longer exists.",
              cta_pair("Back to home", "index.html"), cls="compact"),
    section(head("Popular pages", "Try one of<br />these instead")
            + cards([("card", "Products", "Cards, accounts and pricing.", "View products", "products.html"),
                     ("help", "Help Center", "Answers to common questions.", "Get help", "help-center.html"),
                     ("mail", "Contact", "Talk to our team.", "Contact us", "contact.html")])),
)
