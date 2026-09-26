import json

with open('data.json', 'r', encoding='utf-8') as f:
    categories = json.load(f)

html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>PyPulse | Charan Teja's Python, Django & Flask Journey</title>
  <meta name="description" content="Explore Charan Teja's 125-day hands-on mastery roadmap across Python, Django, DRF, and Flask with daily LinkedIn posts and code milestones.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-primary: #090d16;
      --bg-secondary: #0f172a;
      --bg-card: rgba(17, 24, 39, 0.75);
      --bg-card-hover: rgba(30, 41, 59, 0.85);
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-sub: #cbd5e1;
      --border-color: rgba(255, 255, 255, 0.08);
      --border-hover: rgba(56, 189, 248, 0.4);
      --python-color: #38bdf8;
      --django-color: #10b981;
      --flask-color: #c084fc;
      --accent: #38bdf8;
      --accent-glow: rgba(56, 189, 248, 0.25);
      --card-radius: 16px;
      --transition: all 0.28s cubic-bezier(0.4, 0, 0.2, 1);
    }

    [data-theme="light"] {
      --bg-primary: #f8fafc;
      --bg-secondary: #ffffff;
      --bg-card: rgba(255, 255, 255, 0.85);
      --bg-card-hover: #ffffff;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --text-sub: #334155;
      --border-color: rgba(0, 0, 0, 0.08);
      --border-hover: rgba(14, 165, 233, 0.4);
      --python-color: #0284c7;
      --django-color: #059669;
      --flask-color: #7c3aed;
      --accent: #0284c7;
      --accent-glow: rgba(2, 132, 199, 0.15);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      scroll-behavior: smooth;
    }

    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-primary);
      color: var(--text-main);
      min-height: 100vh;
      line-height: 1.6;
      overflow-x: hidden;
      transition: background-color 0.3s ease, color 0.3s ease;
      background-image: 
        radial-gradient(circle at 15% 15%, rgba(56, 189, 248, 0.08) 0%, transparent 40%),
        radial-gradient(circle at 85% 25%, rgba(16, 185, 129, 0.08) 0%, transparent 40%),
        radial-gradient(circle at 50% 80%, rgba(192, 132, 252, 0.06) 0%, transparent 50%);
      background-attachment: fixed;
    }

    /* Ambient background grid */
    .bg-grid {
      position: fixed;
      inset: 0;
      background-size: 40px 40px;
      background-image: 
        linear-gradient(to right, var(--border-color) 1px, transparent 1px),
        linear-gradient(to bottom, var(--border-color) 1px, transparent 1px);
      pointer-events: none;
      opacity: 0.4;
      z-index: 0;
    }

    /* Header / Nav */
    header {
      position: sticky;
      top: 0;
      z-index: 100;
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      background: rgba(9, 13, 22, 0.75);
      border-bottom: 1px solid var(--border-color);
      transition: var(--transition);
    }

    [data-theme="light"] header {
      background: rgba(248, 250, 252, 0.85);
    }

    .nav-container {
      max-width: 1280px;
      margin: 0 auto;
      padding: 0.9rem 1.5rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      text-decoration: none;
      color: var(--text-main);
    }

    .brand-icon {
      width: 40px;
      height: 40px;
      border-radius: 12px;
      background: linear-gradient(135deg, #0284c7, #10b981);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.3rem;
      box-shadow: 0 4px 14px var(--accent-glow);
    }

    .brand-title {
      font-weight: 800;
      font-size: 1.3rem;
      letter-spacing: -0.02em;
      background: linear-gradient(120deg, #38bdf8, #10b981, #c084fc);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .brand-author {
      font-size: 0.78rem;
      color: var(--text-muted);
      font-weight: 500;
      display: block;
    }

    .nav-actions {
      display: flex;
      align-items: center;
      gap: 1rem;
    }

    .theme-toggle-btn {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 0.5rem 0.85rem;
      border-radius: 10px;
      cursor: pointer;
      font-size: 1rem;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      transition: var(--transition);
    }

    .theme-toggle-btn:hover {
      border-color: var(--accent);
      transform: translateY(-1px);
    }

    .profile-link-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      background: #0a66c2;
      color: #ffffff;
      padding: 0.5rem 1.1rem;
      border-radius: 10px;
      font-weight: 600;
      font-size: 0.88rem;
      text-decoration: none;
      transition: var(--transition);
      box-shadow: 0 4px 12px rgba(10, 102, 194, 0.25);
    }

    .profile-link-btn:hover {
      background: #004182;
      transform: translateY(-2px);
      box-shadow: 0 6px 18px rgba(10, 102, 194, 0.4);
    }

    /* Hero Section */
    .hero {
      position: relative;
      z-index: 1;
      max-width: 1280px;
      margin: 0 auto;
      padding: 3.5rem 1.5rem 2rem;
      text-align: center;
    }

    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.35rem 0.95rem;
      background: rgba(56, 189, 248, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-radius: 999px;
      color: var(--accent);
      font-size: 0.82rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 1.25rem;
    }

    .hero-badge .pulse {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--accent);
      box-shadow: 0 0 10px var(--accent);
      animation: pulse-dot 2s infinite;
    }

    @keyframes pulse-dot {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.4; transform: scale(0.85); }
    }

    .hero-title {
      font-size: clamp(2.2rem, 5vw, 3.6rem);
      font-weight: 800;
      line-height: 1.15;
      letter-spacing: -0.03em;
      margin-bottom: 1.1rem;
    }

    .hero-title span.grad {
      background: linear-gradient(135deg, #38bdf8 0%, #10b981 50%, #c084fc 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .hero-desc {
      max-width: 720px;
      margin: 0 auto 2.5rem;
      color: var(--text-muted);
      font-size: 1.08rem;
      line-height: 1.65;
    }

    /* Stats Ribbon */
    .stats-ribbon {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
      gap: 1.25rem;
      max-width: 1040px;
      margin: 0 auto 3rem;
    }

    .stat-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--card-radius);
      padding: 1.35rem;
      backdrop-filter: blur(10px);
      text-align: left;
      position: relative;
      overflow: hidden;
      transition: var(--transition);
    }

    .stat-card:hover {
      transform: translateY(-3px);
      border-color: var(--border-hover);
    }

    .stat-card::before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 3px;
      background: linear-gradient(90deg, var(--accent), transparent);
    }

    .stat-card.stat-python::before { background: linear-gradient(90deg, var(--python-color), transparent); }
    .stat-card.stat-django::before { background: linear-gradient(90deg, var(--django-color), transparent); }
    .stat-card.stat-flask::before { background: linear-gradient(90deg, var(--flask-color), transparent); }

    .stat-number {
      font-size: 2.2rem;
      font-weight: 800;
      font-family: 'JetBrains Mono', monospace;
      color: var(--text-main);
      display: flex;
      align-items: baseline;
      gap: 0.35rem;
    }

    .stat-number small {
      font-size: 1rem;
      color: var(--text-muted);
      font-weight: 400;
    }

    .stat-label {
      color: var(--text-muted);
      font-size: 0.85rem;
      font-weight: 500;
      margin-top: 0.2rem;
    }

    /* Main Container */
    main {
      position: relative;
      z-index: 1;
      max-width: 1280px;
      margin: 0 auto;
      padding: 0 1.5rem 5rem;
    }

    /* Sticky Control Toolbar */
    .controls-wrapper {
      position: sticky;
      top: 68px;
      z-index: 90;
      background: rgba(9, 13, 22, 0.85);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      padding: 1rem;
      margin-bottom: 2rem;
      border-radius: var(--card-radius);
      border: 1px solid var(--border-color);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    [data-theme="light"] .controls-wrapper {
      background: rgba(255, 255, 255, 0.9);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
    }

    .tabs-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      flex-wrap: wrap;
    }

    .filter-tabs {
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
    }

    .filter-tab {
      background: transparent;
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      padding: 0.55rem 1.1rem;
      border-radius: 10px;
      cursor: pointer;
      font-weight: 600;
      font-size: 0.88rem;
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      transition: var(--transition);
    }

    .filter-tab:hover {
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.05);
      border-color: var(--border-hover);
    }

    .filter-tab.active {
      background: var(--accent);
      color: #090d16;
      border-color: var(--accent);
      font-weight: 700;
      box-shadow: 0 4px 14px var(--accent-glow);
    }

    [data-theme="light"] .filter-tab.active {
      color: #ffffff;
    }

    .filter-tab .badge-count {
      background: rgba(0, 0, 0, 0.15);
      padding: 0.15rem 0.5rem;
      border-radius: 999px;
      font-size: 0.75rem;
      font-family: 'JetBrains Mono', monospace;
    }

    .filter-tab.active .badge-count {
      background: rgba(0, 0, 0, 0.25);
      color: inherit;
    }

    .search-filter-row {
      display: flex;
      gap: 1rem;
      align-items: center;
      flex-wrap: wrap;
    }

    .search-box {
      flex: 1;
      min-width: 260px;
      position: relative;
    }

    .search-box input {
      width: 100%;
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 0.7rem 1rem 0.7rem 2.6rem;
      border-radius: 10px;
      font-size: 0.92rem;
      font-family: inherit;
      outline: none;
      transition: var(--transition);
    }

    .search-box input:focus {
      border-color: var(--accent);
      box-shadow: 0 0 0 3px var(--accent-glow);
    }

    .search-icon {
      position: absolute;
      left: 0.9rem;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      pointer-events: none;
    }

    .sort-box {
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .sort-select {
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      padding: 0.65rem 1rem;
      border-radius: 10px;
      font-size: 0.88rem;
      font-family: inherit;
      outline: none;
      cursor: pointer;
      transition: var(--transition);
    }

    .sort-select:focus {
      border-color: var(--accent);
    }

    /* Results Bar */
    .results-info {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1.5rem;
      padding: 0 0.25rem;
      font-size: 0.88rem;
      color: var(--text-muted);
    }

    .results-info strong {
      color: var(--text-main);
      font-family: 'JetBrains Mono', monospace;
    }

    /* Cards Grid */
    .posts-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
      gap: 1.35rem;
    }

    .post-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--card-radius);
      padding: 1.5rem;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      backdrop-filter: blur(8px);
      transition: var(--transition);
      position: relative;
      overflow: hidden;
    }

    .post-card:hover {
      transform: translateY(-4px);
      background: var(--bg-card-hover);
      border-color: var(--border-hover);
      box-shadow: 0 12px 28px rgba(0, 0, 0, 0.25);
    }

    .card-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 1rem;
    }

    .day-pill {
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      font-size: 0.78rem;
      padding: 0.3rem 0.65rem;
      border-radius: 8px;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
    }

    .card-category-tag {
      font-size: 0.74rem;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      gap: 0.3rem;
    }

    .post-title {
      font-size: 1.12rem;
      font-weight: 700;
      line-height: 1.4;
      margin-bottom: 0.75rem;
      color: var(--text-main);
    }

    .post-desc {
      font-size: 0.85rem;
      color: var(--text-muted);
      line-height: 1.5;
      margin-bottom: 1.25rem;
      flex-grow: 1;
    }

    .card-footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding-top: 1rem;
      border-top: 1px solid var(--border-color);
      gap: 0.75rem;
    }

    .btn-link {
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      background: rgba(10, 102, 194, 0.15);
      color: #38bdf8;
      border: 1px solid rgba(56, 189, 248, 0.25);
      padding: 0.5rem 0.95rem;
      border-radius: 8px;
      font-size: 0.84rem;
      font-weight: 600;
      text-decoration: none;
      transition: var(--transition);
      flex: 1;
      justify-content: center;
    }

    .btn-link:hover {
      background: #0a66c2;
      color: #ffffff;
      border-color: #0a66c2;
      transform: translateY(-1px);
    }

    .btn-copy {
      background: transparent;
      border: 1px solid var(--border-color);
      color: var(--text-muted);
      width: 36px;
      height: 36px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: var(--transition);
      flex-shrink: 0;
    }

    .btn-copy:hover {
      border-color: var(--accent);
      color: var(--text-main);
      background: rgba(255, 255, 255, 0.05);
    }

    /* Category Themes */
    .card-python .day-pill {
      background: rgba(56, 189, 248, 0.12);
      color: var(--python-color);
      border: 1px solid rgba(56, 189, 248, 0.25);
    }
    .card-django .day-pill {
      background: rgba(16, 185, 129, 0.12);
      color: var(--django-color);
      border: 1px solid rgba(16, 185, 129, 0.25);
    }
    .card-flask .day-pill {
      background: rgba(192, 132, 252, 0.12);
      color: var(--flask-color);
      border: 1px solid rgba(192, 132, 252, 0.25);
    }

    /* Empty state */
    .empty-state {
      grid-column: 1 / -1;
      text-align: center;
      padding: 4rem 1.5rem;
      background: var(--bg-card);
      border: 1px dashed var(--border-color);
      border-radius: var(--card-radius);
    }

    .empty-state-icon {
      font-size: 2.8rem;
      margin-bottom: 1rem;
      opacity: 0.6;
    }

    .empty-state h3 {
      font-size: 1.3rem;
      margin-bottom: 0.5rem;
    }

    .empty-state p {
      color: var(--text-muted);
      font-size: 0.95rem;
      margin-bottom: 1.25rem;
    }

    .empty-state button {
      background: var(--accent);
      color: #090d16;
      border: none;
      padding: 0.55rem 1.25rem;
      border-radius: 8px;
      font-weight: 700;
      cursor: pointer;
    }

    /* Toast Notification */
    .toast {
      position: fixed;
      bottom: 2rem;
      right: 2rem;
      background: #10b981;
      color: #ffffff;
      padding: 0.75rem 1.25rem;
      border-radius: 10px;
      font-weight: 600;
      font-size: 0.9rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
      z-index: 999;
      opacity: 0;
      transform: translateY(20px);
      pointer-events: none;
      transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    .toast.show {
      opacity: 1;
      transform: translateY(0);
      pointer-events: auto;
    }

    /* Back to Top Floating Button */
    .back-to-top {
      position: fixed;
      bottom: 2rem;
      left: 2rem;
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      opacity: 0;
      visibility: hidden;
      transition: var(--transition);
      z-index: 80;
      box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }

    .back-to-top.visible {
      opacity: 1;
      visibility: visible;
    }

    .back-to-top:hover {
      background: var(--accent);
      color: #090d16;
      transform: translateY(-3px);
    }

    /* Footer */
    footer {
      border-top: 1px solid var(--border-color);
      background: var(--bg-secondary);
      padding: 3rem 1.5rem;
      text-align: center;
      color: var(--text-muted);
      font-size: 0.88rem;
    }

    .footer-content {
      max-width: 1280px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 1.25rem;
    }

    .footer-links {
      display: flex;
      gap: 1.5rem;
      flex-wrap: wrap;
      justify-content: center;
    }

    .footer-links a {
      color: var(--text-sub);
      text-decoration: none;
      transition: var(--transition);
      font-weight: 500;
    }

    .footer-links a:hover {
      color: var(--accent);
    }

    /* Responsive */
    @media (max-width: 768px) {
      .controls-wrapper {
        top: 60px;
        padding: 0.85rem;
      }
      .filter-tabs {
        width: 100%;
        overflow-x: auto;
        padding-bottom: 0.25rem;
      }
      .posts-grid {
        grid-template-columns: 1fr;
      }
      .stats-ribbon {
        grid-template-columns: 1fr 1fr;
      }
    }

    @media (max-width: 480px) {
      .stats-ribbon {
        grid-template-columns: 1fr;
      }
      .nav-container {
        padding: 0.75rem 1rem;
      }
      .hero {
        padding: 2.5rem 1rem 1.5rem;
      }
      .hero-title {
        font-size: 1.9rem;
      }
    }
  </style>
</head>
<body>
  <div class="bg-grid"></div>

  <!-- Header -->
  <header>
    <div class="nav-container">
      <a href="#" class="brand">
        <div class="brand-icon">⚡</div>
        <div>
          <span class="brand-title">PyPulse Hub</span>
          <span class="brand-author">by Charan Teja</span>
        </div>
      </a>
      <div class="nav-actions">
        <button id="themeToggle" class="theme-toggle-btn" title="Toggle Theme" aria-label="Toggle theme">
          <span id="themeIcon">☀️</span>
        </button>
        <a href="https://www.linkedin.com/in/charan-teja-972aa9231" target="_blank" rel="noopener noreferrer" class="profile-link-btn">
          <svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
          LinkedIn Profile
        </a>
      </div>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="hero">
    <div class="hero-badge">
      <span class="pulse"></span>
      125+ Days of Continuous Engineering
    </div>
    <h1 class="hero-title">
      Full-Stack Python, Django &amp; Flask <br>
      <span class="grad">Daily Learning Portfolio</span>
    </h1>
    <p class="hero-desc">
      A comprehensive archive of Charan Teja's engineering journey documenting real-world problem solving, backend architectural patterns, ORM mechanics, RESTful APIs, and cloud deployments posted daily to LinkedIn.
    </p>

    <!-- Stats Ribbon -->
    <div class="stats-ribbon">
      <div class="stat-card">
        <div class="stat-number" id="totalPostsStat">125<small>posts</small></div>
        <div class="stat-label">Total Documented Days</div>
      </div>
      <div class="stat-card stat-python">
        <div class="stat-number">50<small>days</small></div>
        <div class="stat-label">Python Challenge</div>
      </div>
      <div class="stat-card stat-django">
        <div class="stat-number">41<small>milestones</small></div>
        <div class="stat-label">Django &amp; DRF Deep Dive</div>
      </div>
      <div class="stat-card stat-flask">
        <div class="stat-number">34<small>milestones</small></div>
        <div class="stat-label">Flask Microframework</div>
      </div>
    </div>
  </section>

  <!-- Main Content Area -->
  <main>
    <!-- Controls Toolbar -->
    <div class="controls-wrapper">
      <div class="tabs-row">
        <div class="filter-tabs" id="filterTabs">
          <button class="filter-tab active" data-category="all">
            <span>🌟 All Tracks</span>
            <span class="badge-count" id="countAll">125</span>
          </button>
          <button class="filter-tab" data-category="python">
            <span>🐍 Python 50 Days</span>
            <span class="badge-count" id="countPython">51</span>
          </button>
          <button class="filter-tab" data-category="django">
            <span>⚡ Django &amp; DRF</span>
            <span class="badge-count" id="countDjango">41</span>
          </button>
          <button class="filter-tab" data-category="flask">
            <span>🧪 Flask Mastery</span>
            <span class="badge-count" id="countFlask">33</span>
          </button>
        </div>
      </div>

      <div class="search-filter-row">
        <div class="search-box">
          <svg class="search-icon" width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
          <input type="text" id="searchInput" placeholder="Search by topic, day (e.g. Day 10), ORM, JWT, Decorators..." aria-label="Search posts">
        </div>
        <div class="sort-box">
          <label for="sortOrder" style="font-size: 0.85rem; color: var(--text-muted); font-weight: 500;">Sort:</label>
          <select id="sortOrder" class="sort-select">
            <option value="original">Original Roadmap Order</option>
            <option value="title-asc">Topic Name (A-Z)</option>
            <option value="title-desc">Topic Name (Z-A)</option>
          </select>
        </div>
      </div>
    </div>

    <!-- Results Status -->
    <div class="results-info">
      <div>Showing <strong id="visibleCount">125</strong> learning milestones</div>
      <div id="filterStatusHint"></div>
    </div>

    <!-- Posts Grid -->
    <div class="posts-grid" id="postsGrid">
      <!-- Dynamically rendered -->
    </div>
  </main>

  <!-- Back to Top Floating Button -->
  <button id="backToTop" class="back-to-top" title="Back to top" aria-label="Back to top">
    <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 15l7-7 7 7"/></svg>
  </button>

  <!-- Toast Notification -->
  <div id="toast" class="toast">
    <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>
    <span id="toastMessage">Link copied to clipboard!</span>
  </div>

  <!-- Footer -->
  <footer>
    <div class="footer-content">
      <div>
        <strong>PyPulse Hub</strong> &bull; Crafted for Charan Teja's Professional Portfolio
      </div>
      <div class="footer-links">
        <a href="https://www.linkedin.com/in/charan-teja-972aa9231" target="_blank" rel="noopener noreferrer">LinkedIn Profile</a>
        <a href="#top">Back to Top</a>
        <a href="javascript:void(0)" onclick="shareCollection()">Share Collection</a>
      </div>
      <p style="font-size: 0.8rem; color: var(--text-muted); opacity: 0.8;">
        Built strictly with pure HTML5, Internal CSS &amp; Vanilla JavaScript &bull; Fast, Responsive &amp; Lightweight
      </p>
    </div>
  </footer>

  <script>
    // Embedded Data Generated from PYTHON_DJANGO_FLASK Daily Learning Links.txt
    const POSTS_DATA = %DATA_PLACEHOLDER%;

    // State
    let currentCategory = 'all';
    let searchQuery = '';
    let sortMethod = 'original';

    // Flatten all items with extra metadata
    const allPosts = [];
    POSTS_DATA.forEach(cat => {
      cat.posts.forEach((p, idx) => {
        allPosts.push({
          ...p,
          categoryId: cat.id,
          categoryName: cat.shortName,
          categoryBadge: cat.badge,
          categoryIcon: cat.icon,
          originalOrder: allPosts.length
        });
      });
    });

    // DOM Elements
    const grid = document.getElementById('postsGrid');
    const searchInput = document.getElementById('searchInput');
    const sortSelect = document.getElementById('sortOrder');
    const filterTabs = document.querySelectorAll('.filter-tab');
    const visibleCountEl = document.getElementById('visibleCount');
    const filterStatusHint = document.getElementById('filterStatusHint');
    const themeToggleBtn = document.getElementById('themeToggle');
    const themeIcon = document.getElementById('themeIcon');
    const backToTopBtn = document.getElementById('backToTop');
    const toast = document.getElementById('toast');
    const toastMessage = document.getElementById('toastMessage');

    // Counts Setup
    document.getElementById('totalPostsStat').innerHTML = `${allPosts.length}<small>posts</small>`;
    document.getElementById('countAll').textContent = allPosts.length;
    document.getElementById('countPython').textContent = allPosts.filter(p => p.categoryId === 'python').length;
    document.getElementById('countDjango').textContent = allPosts.filter(p => p.categoryId === 'django').length;
    document.getElementById('countFlask').textContent = allPosts.filter(p => p.categoryId === 'flask').length;

    // Render Function
    function renderPosts() {
      // 1. Filter by category
      let filtered = allPosts.filter(post => {
        if (currentCategory !== 'all' && post.categoryId !== currentCategory) return false;
        
        // 2. Filter by search query
        if (searchQuery.trim() !== '') {
          const q = searchQuery.toLowerCase();
          const matchDay = post.day.toLowerCase().includes(q);
          const matchTopic = post.topic.toLowerCase().includes(q);
          const matchCategory = post.categoryName.toLowerCase().includes(q);
          return matchDay || matchTopic || matchCategory;
        }
        return true;
      });

      // 3. Sort
      if (sortMethod === 'title-asc') {
        filtered.sort((a, b) => a.topic.localeCompare(b.topic));
      } else if (sortMethod === 'title-desc') {
        filtered.sort((a, b) => b.topic.localeCompare(a.topic));
      } else {
        filtered.sort((a, b) => a.originalOrder - b.originalOrder);
      }

      visibleCountEl.textContent = filtered.length;
      if (searchQuery.trim()) {
        filterStatusHint.textContent = `Matching "${searchQuery}"`;
      } else {
        filterStatusHint.textContent = '';
      }

      if (filtered.length === 0) {
        grid.innerHTML = `
          <div class="empty-state">
            <div class="empty-state-icon">🔍</div>
            <h3>No learning logs found</h3>
            <p>We couldn't find any post matching "<strong>${escapeHtml(searchQuery)}</strong>". Try checking for typos or resetting your search.</p>
            <button onclick="resetFilters()">Clear Filters</button>
          </div>
        `;
        return;
      }

      grid.innerHTML = filtered.map(post => {
        return `
          <article class="post-card card-${post.categoryId}" data-id="${post.id}">
            <div>
              <div class="card-top">
                <span class="day-pill">${escapeHtml(post.day)}</span>
                <span class="card-category-tag">${post.categoryIcon} ${post.categoryName}</span>
              </div>
              <h2 class="post-title">${escapeHtml(post.topic)}</h2>
              <p class="post-desc">
                ${getPostSummary(post)}
              </p>
            </div>
            <div class="card-footer">
              <a href="${post.url}" target="_blank" rel="noopener noreferrer" class="btn-link">
                <svg width="15" height="15" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
                Read on LinkedIn
              </a>
              <button class="btn-copy" onclick="copyPostLink('${post.url}', this)" title="Copy Post URL" aria-label="Copy post link">
                <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"/></svg>
              </button>
            </div>
          </article>
        `;
      }).join('');
    }

    function getPostSummary(post) {
      if (post.categoryId === 'python') {
        return `Hands-on Python milestone covering core mechanics, code architecture, problem-solving paradigms, and clean Pythonic idioms.`;
      } else if (post.categoryId === 'django') {
        return `Django engineering milestone focusing on backend enterprise architecture, database models, view controllers, and REST APIs.`;
      } else {
        return `Flask web development milestone demonstrating lightweight routing, request lifecycles, template rendering, and practical backend APIs.`;
      }
    }

    function escapeHtml(str) {
      if (!str) return '';
      return str.replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;')
                .replace(/"/g, '&quot;')
                .replace(/'/g, '&#039;');
    }

    function resetFilters() {
      searchQuery = '';
      currentCategory = 'all';
      searchInput.value = '';
      filterTabs.forEach(t => {
        t.classList.toggle('active', t.dataset.category === 'all');
      });
      renderPosts();
    }

    // Copy URL to Clipboard
    function copyPostLink(url, btnElement) {
      navigator.clipboard.writeText(url).then(() => {
        showToast('LinkedIn post link copied to clipboard!');
        const origSvg = btnElement.innerHTML;
        btnElement.innerHTML = `<svg width="16" height="16" fill="none" stroke="#10b981" stroke-width="2.5" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg>`;
        setTimeout(() => {
          btnElement.innerHTML = origSvg;
        }, 1800);
      }).catch(() => {
        showToast('Failed to copy. Please open the link directly.');
      });
    }

    function showToast(msg) {
      toastMessage.textContent = msg;
      toast.classList.add('show');
      setTimeout(() => {
        toast.classList.remove('show');
      }, 2500);
    }

    function shareCollection() {
      if (navigator.share) {
        navigator.share({
          title: "Charan Teja's Python, Django & Flask Learning Hub",
          text: "Check out this full 125-day roadmap of Python, Django, and Flask learning posts!",
          url: window.location.href
        }).catch(() => {});
      } else {
        navigator.clipboard.writeText(window.location.href);
        showToast('Portfolio URL copied to clipboard!');
      }
    }

    // Event Listeners
    filterTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        filterTabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');
        currentCategory = tab.dataset.category;
        renderPosts();
      });
    });

    searchInput.addEventListener('input', (e) => {
      searchQuery = e.target.value;
      renderPosts();
    });

    sortSelect.addEventListener('change', (e) => {
      sortMethod = e.target.value;
      renderPosts();
    });

    // Theme Toggle
    function toggleTheme() {
      const currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
      const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', newTheme);
      themeIcon.textContent = newTheme === 'dark' ? '☀️' : '🌙';
      localStorage.setItem('pypulse-theme', newTheme);
    }

    // Initialize Theme
    const savedTheme = localStorage.getItem('pypulse-theme') || 'dark';
    document.documentElement.setAttribute('data-theme', savedTheme);
    themeIcon.textContent = savedTheme === 'dark' ? '☀️' : '🌙';
    themeToggleBtn.addEventListener('click', toggleTheme);

    // Back to top scroll handler
    window.addEventListener('scroll', () => {
      if (window.scrollY > 400) {
        backToTopBtn.classList.add('visible');
      } else {
        backToTopBtn.classList.remove('visible');
      }
    });

    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // Initial Render
    renderPosts();
  </script>
</body>
</html>
'''

data_json_str = json.dumps(categories, separators=(',', ':'))
full_html = html_template.replace('%DATA_PLACEHOLDER%', data_json_str)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Generated index.html successfully! Size:", len(full_html), "bytes")
