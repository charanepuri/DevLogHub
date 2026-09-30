import json

with open('data.json', 'r', encoding='utf-8') as f:
    categories = json.load(f)

total_count = sum(c['count'] for c in categories)

html_template = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>DevLog Hub | Charan Teja's Engineering & Learning Portfolio</title>
  <meta name="description" content="Explore Charan Teja's 200+ milestone engineering archive covering Technical Documentation, Python 50D, Django 40D, Flask Mastery, SQL, Projects, and Career Milestones.">
  <link rel="icon" type="image/png" href="DevLog%20Hub.png">
  <link rel="apple-touch-icon" href="DevLog%20Hub.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-primary: #090d16;
      --bg-secondary: #0f172a;
      --bg-card: rgba(17, 24, 39, 0.78);
      --bg-card-hover: rgba(30, 41, 59, 0.9);
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --text-sub: #cbd5e1;
      --border-color: rgba(255, 255, 255, 0.08);
      --border-hover: rgba(56, 189, 248, 0.4);
      --docs-color: #f59e0b;
      --python-color: #38bdf8;
      --django-color: #10b981;
      --flask-color: #c084fc;
      --sql-color: #06b6d4;
      --web-color: #eab308;
      --react-color: #00d8ff;
      --django-app-color: #10b981;
      --flask-app-color: #c084fc;
      --ai-color: #a855f7;
      --techglossary-color: #06b6d4;
      --devprod-color: #6366f1;
      --projects-color: #f97316;
      --advpy-color: #a3e635;
      --intern-color: #ec4899;
      --accent: #38bdf8;
      --accent-glow: rgba(56, 189, 248, 0.25);
      --card-radius: 16px;
      --transition: all 0.28s cubic-bezier(0.4, 0, 0.2, 1);
    }

    [data-theme="light"] {
      --bg-primary: #f8fafc;
      --bg-secondary: #ffffff;
      --bg-card: rgba(255, 255, 255, 0.9);
      --bg-card-hover: #ffffff;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --text-sub: #334155;
      --border-color: rgba(0, 0, 0, 0.08);
      --border-hover: rgba(14, 165, 233, 0.4);
      --docs-color: #d97706;
      --python-color: #0284c7;
      --django-color: #059669;
      --flask-color: #7c3aed;
      --sql-color: #0891b2;
      --web-color: #ca8a04;
      --react-color: #0284c7;
      --django-app-color: #059669;
      --flask-app-color: #7c3aed;
      --ai-color: #9333ea;
      --techglossary-color: #0891b2;
      --devprod-color: #4f46e5;
      --projects-color: #ea580c;
      --advpy-color: #65a30d;
      --intern-color: #db2777;
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
        radial-gradient(circle at 50% 80%, rgba(245, 158, 11, 0.06) 0%, transparent 50%);
      background-attachment: fixed;
    }

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
      background: rgba(9, 13, 22, 0.82);
      border-bottom: 1px solid var(--border-color);
      transition: var(--transition);
    }

    [data-theme="light"] header {
      background: rgba(248, 250, 252, 0.88);
    }

    .nav-container {
      max-width: 1360px;
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
      width: 42px;
      height: 42px;
      border-radius: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      box-shadow: 0 4px 14px var(--accent-glow);
      flex-shrink: 0;
    }

    .brand-icon img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
    }

    .brand-title {
      font-weight: 800;
      font-size: 1.3rem;
      letter-spacing: -0.02em;
      background: linear-gradient(120deg, #f59e0b, #38bdf8, #10b981, #c084fc);
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
      max-width: 1360px;
      margin: 0 auto;
      padding: 3.2rem 1.5rem 1.8rem;
      text-align: center;
    }

    .hero-badge {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.35rem 0.95rem;
      background: rgba(245, 158, 11, 0.1);
      border: 1px solid rgba(245, 158, 11, 0.3);
      border-radius: 999px;
      color: var(--docs-color);
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
      background: var(--docs-color);
      box-shadow: 0 0 10px var(--docs-color);
      animation: pulse-dot 2s infinite;
    }

    @keyframes pulse-dot {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.4; transform: scale(0.85); }
    }

    .hero-title {
      font-size: clamp(2.2rem, 5vw, 3.6rem);
      font-weight: 800;
      line-height: 1.18;
      letter-spacing: -0.03em;
      margin-bottom: 1.1rem;
    }

    .hero-title span.grad {
      background: linear-gradient(135deg, #f59e0b 0%, #38bdf8 35%, #10b981 65%, #c084fc 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .hero-desc {
      max-width: 800px;
      margin: 0 auto 2.25rem;
      color: var(--text-muted);
      font-size: 1.05rem;
      line-height: 1.65;
    }

    /* Stats Ribbon */
    .stats-ribbon {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
      gap: 0.9rem;
      max-width: 1300px;
      margin: 0 auto 2.75rem;
    }

    .stat-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--card-radius);
      padding: 1rem 0.85rem;
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
    }

    .stat-card.stat-total::before { background: linear-gradient(90deg, #f59e0b, #38bdf8, #10b981); }
    .stat-card.stat-docs::before { background: linear-gradient(90deg, var(--docs-color), transparent); }
    .stat-card.stat-python::before { background: linear-gradient(90deg, var(--python-color), transparent); }
    .stat-card.stat-django::before { background: linear-gradient(90deg, var(--django-color), transparent); }
    .stat-card.stat-flask::before { background: linear-gradient(90deg, var(--flask-color), transparent); }
    .stat-card.stat-sql::before { background: linear-gradient(90deg, var(--sql-color), transparent); }
    .stat-card.stat-web::before { background: linear-gradient(90deg, var(--web-color), transparent); }
    .stat-card.stat-react::before { background: linear-gradient(90deg, var(--react-color), transparent); }
    .stat-card.stat-django-app::before { background: linear-gradient(90deg, var(--django-app-color), transparent); }
    .stat-card.stat-flask-app::before { background: linear-gradient(90deg, var(--flask-app-color), transparent); }
    .stat-card.stat-ai-app::before { background: linear-gradient(90deg, var(--ai-color), transparent); }
    .stat-card.stat-techglossary::before { background: linear-gradient(90deg, var(--techglossary-color), transparent); }
    .stat-card.stat-devprod::before { background: linear-gradient(90deg, var(--devprod-color), transparent); }
    .stat-card.stat-projects::before { background: linear-gradient(90deg, var(--projects-color), transparent); }
    .stat-card.stat-advpy::before { background: linear-gradient(90deg, var(--advpy-color), transparent); }
    .stat-card.stat-intern::before { background: linear-gradient(90deg, var(--intern-color), transparent); }

    .stat-number {
      font-size: 1.75rem;
      font-weight: 800;
      font-family: 'JetBrains Mono', monospace;
      color: var(--text-main);
      display: flex;
      align-items: baseline;
      gap: 0.25rem;
    }

    .stat-number small {
      font-size: 0.8rem;
      color: var(--text-muted);
      font-weight: 400;
    }

    .stat-label {
      color: var(--text-muted);
      font-size: 0.76rem;
      font-weight: 600;
      margin-top: 0.2rem;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }

    /* Main Container */
    main {
      position: relative;
      z-index: 1;
      max-width: 1360px;
      margin: 0 auto;
      padding: 0 1.5rem 5rem;
    }

    /* Controls Toolbar */
    .controls-wrapper {
      position: sticky;
      top: 68px;
      z-index: 90;
      background: rgba(9, 13, 22, 0.88);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      padding: 1rem;
      margin-bottom: 2rem;
      border-radius: var(--card-radius);
      border: 1px solid var(--border-color);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    [data-theme="light"] .controls-wrapper {
      background: rgba(255, 255, 255, 0.92);
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
    }

    .tabs-row {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      overflow-x: auto;
      padding-bottom: 0.25rem;
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
      padding: 0.45rem 0.85rem;
      border-radius: 10px;
      cursor: pointer;
      font-weight: 600;
      font-size: 0.83rem;
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      transition: var(--transition);
      white-space: nowrap;
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
      padding: 0.12rem 0.45rem;
      border-radius: 999px;
      font-size: 0.7rem;
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

    /* Results Info */
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

    /* Posts Grid */
    .posts-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
      gap: 1.35rem;
    }

    .post-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--card-radius);
      padding: 1.45rem;
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
      margin-bottom: 0.85rem;
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
      font-size: 1.08rem;
      font-weight: 700;
      line-height: 1.4;
      margin-bottom: 0.65rem;
      color: var(--text-main);
    }

    .post-desc {
      font-size: 0.84rem;
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
      gap: 0.6rem;
    }

    .card-actions-group {
      display: flex;
      align-items: center;
      gap: 0.45rem;
      flex: 1;
      flex-wrap: wrap;
    }

    .btn-link {
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      background: rgba(10, 102, 194, 0.15);
      color: #38bdf8;
      border: 1px solid rgba(56, 189, 248, 0.25);
      padding: 0.48rem 0.8rem;
      border-radius: 8px;
      font-size: 0.82rem;
      font-weight: 600;
      text-decoration: none;
      transition: var(--transition);
      flex: 1;
      min-width: fit-content;
      justify-content: center;
      white-space: nowrap;
    }

    .btn-link:hover {
      background: #0a66c2;
      color: #ffffff;
      border-color: #0a66c2;
      transform: translateY(-1px);
    }

    .btn-link.btn-live {
      background: rgba(16, 185, 129, 0.15);
      color: #34d399;
      border-color: rgba(16, 185, 129, 0.3);
    }

    .btn-link.btn-live:hover {
      background: #059669;
      color: #ffffff;
      border-color: #059669;
    }

    .btn-link.btn-github {
      background: rgba(255, 255, 255, 0.08);
      color: #f1f5f9;
      border-color: rgba(255, 255, 255, 0.18);
    }

    .btn-link.btn-github:hover {
      background: #24292e;
      color: #ffffff;
      border-color: #6e5494;
    }

    .btn-link.btn-doc {
      background: rgba(245, 158, 11, 0.15);
      color: #fbbf24;
      border-color: rgba(245, 158, 11, 0.3);
    }

    .btn-link.btn-doc:hover {
      background: #d97706;
      color: #ffffff;
      border-color: #d97706;
    }

    .btn-link.btn-drive {
      background: rgba(59, 130, 246, 0.15);
      color: #60a5fa;
      border-color: rgba(59, 130, 246, 0.3);
    }

    .btn-link.btn-drive:hover {
      background: #2563eb;
      color: #ffffff;
      border-color: #2563eb;
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

    /* Category Specific Themes */
    .card-tech-docs .day-pill {
      background: rgba(245, 158, 11, 0.12);
      color: var(--docs-color);
      border: 1px solid rgba(245, 158, 11, 0.25);
    }
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
    .card-sql-mysql .day-pill {
      background: rgba(6, 182, 212, 0.12);
      color: var(--sql-color);
      border: 1px solid rgba(6, 182, 212, 0.25);
    }
    .card-web-projects .day-pill {
      background: rgba(234, 179, 8, 0.12);
      color: var(--web-color);
      border: 1px solid rgba(234, 179, 8, 0.25);
    }
    .card-react-projects .day-pill {
      background: rgba(0, 216, 255, 0.12);
      color: var(--react-color);
      border: 1px solid rgba(0, 216, 255, 0.28);
    }
    .card-django-projects .day-pill {
      background: rgba(16, 185, 129, 0.12);
      color: var(--django-app-color);
      border: 1px solid rgba(16, 185, 129, 0.28);
    }
    .card-flask-projects .day-pill {
      background: rgba(192, 132, 252, 0.12);
      color: var(--flask-app-color);
      border: 1px solid rgba(192, 132, 252, 0.28);
    }
    .card-ai-projects .day-pill {
      background: rgba(168, 85, 247, 0.12);
      color: var(--ai-color);
      border: 1px solid rgba(168, 85, 247, 0.28);
    }
    .card-tech-glossary .day-pill {
      background: rgba(6, 182, 212, 0.12);
      color: var(--techglossary-color);
      border: 1px solid rgba(6, 182, 212, 0.28);
    }
    .card-dev-productivity .day-pill {
      background: rgba(99, 102, 241, 0.12);
      color: var(--devprod-color);
      border: 1px solid rgba(99, 102, 241, 0.28);
    }
    .card-projects .day-pill {
      background: rgba(249, 115, 22, 0.12);
      color: var(--projects-color);
      border: 1px solid rgba(249, 115, 22, 0.25);
    }
    .card-advanced-python .day-pill {
      background: rgba(163, 230, 53, 0.12);
      color: var(--advpy-color);
      border: 1px solid rgba(163, 230, 53, 0.25);
    }
    .card-internships .day-pill {
      background: rgba(236, 72, 153, 0.12);
      color: var(--intern-color);
      border: 1px solid rgba(236, 72, 153, 0.25);
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

    /* Connected Ecosystem & Footer Styling */
    .ecosystem-section {
      max-width: 1360px;
      margin: 0 auto 4rem;
      padding: 0 1.5rem;
    }

    .ecosystem-card {
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--card-radius);
      padding: 2.2rem;
      box-shadow: 0 15px 35px rgba(0, 0, 0, 0.25);
      position: relative;
      overflow: hidden;
    }

    .ecosystem-card::before {
      content: "";
      position: absolute;
      top: 0;
      left: 0;
      width: 100%;
      height: 4px;
      background: linear-gradient(90deg, #f59e0b, #38bdf8, #10b981, #ec4899);
    }

    .ecosystem-header {
      text-align: center;
      margin-bottom: 2rem;
    }

    .ecosystem-header h2 {
      font-size: 1.65rem;
      font-weight: 800;
      margin-bottom: 0.4rem;
      background: linear-gradient(120deg, #f59e0b, #38bdf8, #10b981);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .ecosystem-header p {
      color: var(--text-muted);
      font-size: 0.95rem;
    }

    .ecosystem-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
      gap: 1.75rem;
      margin-bottom: 2rem;
    }

    .ecosystem-col {
      background: rgba(255, 255, 255, 0.02);
      border: 1px solid var(--border-color);
      border-radius: 12px;
      padding: 1.4rem;
    }

    .ecosystem-col-title {
      font-size: 1.05rem;
      font-weight: 700;
      margin-bottom: 1.1rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
      color: var(--text-main);
    }

    .links-chip-group {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .eco-link-btn {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 0.7rem 1rem;
      border-radius: 10px;
      text-decoration: none;
      font-weight: 600;
      font-size: 0.88rem;
      color: var(--text-main);
      background: var(--bg-secondary);
      border: 1px solid var(--border-color);
      transition: var(--transition);
    }

    .eco-link-btn:hover {
      transform: translateY(-2px);
      border-color: var(--accent);
      color: var(--accent);
      box-shadow: 0 4px 14px var(--accent-glow);
    }

    .eco-link-btn .eco-label {
      display: flex;
      align-items: center;
      gap: 0.65rem;
    }

    .eco-badge {
      font-size: 0.72rem;
      font-family: 'JetBrains Mono', monospace;
      padding: 0.2rem 0.5rem;
      border-radius: 6px;
      background: rgba(255, 255, 255, 0.08);
      color: var(--text-muted);
    }

    /* Social Bar */
    .socials-row {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 0.85rem;
      padding-top: 1.5rem;
      border-top: 1px solid var(--border-color);
    }

    .social-pill {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.55rem 1.15rem;
      border-radius: 999px;
      font-weight: 600;
      font-size: 0.86rem;
      text-decoration: none;
      transition: var(--transition);
      border: 1px solid var(--border-color);
      color: var(--text-main);
      background: var(--bg-secondary);
    }

    .social-pill:hover {
      transform: translateY(-2px);
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }

    .social-pill.social-linkedin:hover {
      background: #0a66c2;
      border-color: #0a66c2;
      color: #ffffff;
    }

    .social-pill.social-github:hover {
      background: #24292e;
      border-color: #6e5494;
      color: #ffffff;
    }

    .social-pill.social-instagram:hover {
      background: linear-gradient(45deg, #f09433 0%, #e6683c 25%, #dc2743 50%, #cc2366 75%, #bc1888 100%);
      border-color: #dc2743;
      color: #ffffff;
    }

    .social-pill.social-snapchat:hover {
      background: #fffc00;
      border-color: #fffc00;
      color: #000000;
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
      max-width: 1360px;
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
    @media (max-width: 900px) {
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
        grid-template-columns: repeat(3, 1fr);
      }
    }

    @media (max-width: 540px) {
      .stats-ribbon {
        grid-template-columns: repeat(2, 1fr);
      }
      .nav-container {
        padding: 0.75rem 1rem;
      }
      .hero {
        padding: 2.2rem 1rem 1.4rem;
      }
      .hero-title {
        font-size: 1.95rem;
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
        <div class="brand-icon">
          <img src="DevLog%20Hub.png" alt="DevLog Hub Logo" width="42" height="42">
        </div>
        <div>
          <span class="brand-title">DevLog Hub</span>
          <span class="brand-author">by Charan Teja</span>
        </div>
      </a>
      <div class="nav-actions">
        <button id="themeToggle" class="theme-toggle-btn" title="Toggle Theme" aria-label="Toggle theme">
          <span id="themeIcon">☀️</span>
        </button>
        <a href="#ecosystem" class="theme-toggle-btn" style="text-decoration: none; font-size: 0.85rem; font-weight: 600;" title="View Live Portfolios & Projects">
          <span>🌐 Portfolios</span>
        </a>
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
      251+ Verified Technical Milestones
    </div>
    <h1 class="hero-title">
      Full-Stack Engineering, Data &amp; <br>
      <span class="grad">Professional Learning Portfolio</span>
    </h1>
    <p class="hero-desc">
      A unified, interactive knowledge hub indexing 251+ technical milestones authored by Charan Teja &mdash; featuring in-depth Technical Documentation Guides, 50 Days of Python, 40 Days of Django, Flask Microservices, SQL &amp; MySQL, HTML/CSS/JS Web Applications, React SPAs, Django Systems, Flask Applications, AI Integrated Apps, Tech Glossary Hub, Developer Productivity Suite, Projects &amp; AI, and Career Milestones.
    </p>

    <!-- Stats Ribbon -->
    <div class="stats-ribbon">
      <div class="stat-card stat-total">
        <div class="stat-number" id="totalPostsStat">251<small>posts</small></div>
        <div class="stat-label">Total Engineering Posts</div>
      </div>
      <div class="stat-card stat-docs">
        <div class="stat-number">26<small>guides</small></div>
        <div class="stat-label">Technical Documentation</div>
      </div>
      <div class="stat-card stat-python">
        <div class="stat-number">51<small>days</small></div>
        <div class="stat-label">Python 50D Challenge</div>
      </div>
      <div class="stat-card stat-django">
        <div class="stat-number">41<small>days</small></div>
        <div class="stat-label">Django 40D Series</div>
      </div>
      <div class="stat-card stat-flask">
        <div class="stat-number">33<small>days</small></div>
        <div class="stat-label">Flask Microservices</div>
      </div>
      <div class="stat-card stat-sql">
        <div class="stat-number">18<small>queries</small></div>
        <div class="stat-label">SQL &amp; MySQL Databases</div>
      </div>
      <div class="stat-card stat-web">
        <div class="stat-number">16<small>apps</small></div>
        <div class="stat-label">HTML, CSS &amp; JS Apps</div>
      </div>
      <div class="stat-card stat-react">
        <div class="stat-number">6<small>spas</small></div>
        <div class="stat-label">React Applications</div>
      </div>
      <div class="stat-card stat-django-app">
        <div class="stat-number">4<small>apps</small></div>
        <div class="stat-label">Django Applications</div>
      </div>
      <div class="stat-card stat-flask-app">
        <div class="stat-number">4<small>apps</small></div>
        <div class="stat-label">Flask Applications</div>
      </div>
      <div class="stat-card stat-ai-app">
        <div class="stat-number">5<small>apps</small></div>
        <div class="stat-label">AI Integrated Apps</div>
      </div>
      <div class="stat-card stat-techglossary">
        <div class="stat-number">7<small>editions</small></div>
        <div class="stat-label">Tech Glossary Hub</div>
      </div>
      <div class="stat-card stat-devprod">
        <div class="stat-number">7<small>editions</small></div>
        <div class="stat-label">Productivity Suite</div>
      </div>
      <div class="stat-card stat-projects">
        <div class="stat-number">8<small>apps</small></div>
        <div class="stat-label">Projects &amp; AI Apps</div>
      </div>
      <div class="stat-card stat-advpy">
        <div class="stat-number">15<small>topics</small></div>
        <div class="stat-label">Advanced Python &amp; Data</div>
      </div>
      <div class="stat-card stat-intern">
        <div class="stat-number">10<small>milestones</small></div>
        <div class="stat-label">Career Milestones</div>
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
            <span class="badge-count" id="countAll">228</span>
          </button>
          <button class="filter-tab" data-category="tech-docs">
            <span>📚 Technical Docs</span>
            <span class="badge-count" id="countDocs">26</span>
          </button>
          <button class="filter-tab" data-category="python">
            <span>🐍 Python 50D</span>
            <span class="badge-count" id="countPython">51</span>
          </button>
          <button class="filter-tab" data-category="django">
            <span>⚡ Django 40D</span>
            <span class="badge-count" id="countDjango">41</span>
          </button>
          <button class="filter-tab" data-category="flask">
            <span>🧪 Flask</span>
            <span class="badge-count" id="countFlask">33</span>
          </button>
          <button class="filter-tab" data-category="sql-mysql">
            <span>🗄️ SQL &amp; MySQL</span>
            <span class="badge-count" id="countSql">18</span>
          </button>
          <button class="filter-tab" data-category="web-projects">
            <span>🌐 Web Apps</span>
            <span class="badge-count" id="countWeb">16</span>
          </button>
          <button class="filter-tab" data-category="react-projects">
            <span>⚛️ React Apps</span>
            <span class="badge-count" id="countReact">6</span>
          </button>
          <button class="filter-tab" data-category="django-projects">
            <span>⚡ Django Apps</span>
            <span class="badge-count" id="countDjangoApp">4</span>
          </button>
          <button class="filter-tab" data-category="flask-projects">
            <span>🧪 Flask Apps</span>
            <span class="badge-count" id="countFlaskApp">4</span>
          </button>
          <button class="filter-tab" data-category="ai-projects">
            <span>🤖 AI Apps</span>
            <span class="badge-count" id="countAIApp">5</span>
          </button>
          <button class="filter-tab" data-category="tech-glossary">
            <span>📖 Tech Glossary</span>
            <span class="badge-count" id="countTechGlossary">7</span>
          </button>
          <button class="filter-tab" data-category="dev-productivity">
            <span>🛠️ Productivity Suite</span>
            <span class="badge-count" id="countDevProd">7</span>
          </button>
          <button class="filter-tab" data-category="projects">
            <span>🚀 Projects &amp; AI</span>
            <span class="badge-count" id="countProj">8</span>
          </button>
          <button class="filter-tab" data-category="advanced-python">
            <span>⚙️ Advanced Python</span>
            <span class="badge-count" id="countAdvPy">15</span>
          </button>
          <button class="filter-tab" data-category="internships">
            <span>🎓 Career Milestones</span>
            <span class="badge-count" id="countIntern">10</span>
          </button>
        </div>
      </div>

      <div class="search-filter-row">
        <div class="search-box">
          <svg class="search-icon" width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/></svg>
          <input type="text" id="searchInput" placeholder="Search by documentation topic, day, keyword (e.g. DOM, Event Loop, JOIN, LLM, MVT)..." aria-label="Search posts">
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
      <div>Showing <strong id="visibleCount">202</strong> technical milestones</div>
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

  <!-- Connect & Portfolios Ecosystem Section -->
  <section class="ecosystem-section" id="ecosystem">
    <div class="ecosystem-card">
      <div class="ecosystem-header">
        <h2>🌐 Connect &amp; Explore Portfolios</h2>
        <p>Discover Charan Teja's live framework portals, project hubs, and professional social profiles</p>
      </div>

      <div class="ecosystem-grid">
        <!-- Portfolios Column -->
        <div class="ecosystem-col">
          <div class="ecosystem-col-title">
            <span>💼</span> View Live Portfolios
          </div>
          <div class="links-chip-group">
            <a href="https://charanepuri.github.io/PORTFOLIO-USING-HTML-CSS-JS" target="_blank" rel="noopener noreferrer" class="eco-link-btn">
              <span class="eco-label"><span>🌐</span> Basic Portfolio</span>
              <span class="eco-badge">HTML/CSS/JS</span>
            </a>
            <a href="https://portfolio-site-django.onrender.com" target="_blank" rel="noopener noreferrer" class="eco-link-btn">
              <span class="eco-label"><span>⚡</span> Django Portfolio</span>
              <span class="eco-badge">Render</span>
            </a>
            <a href="https://charan-react-portfolio.vercel.app" target="_blank" rel="noopener noreferrer" class="eco-link-btn">
              <span class="eco-label"><span>⚛️</span> React Portfolio</span>
              <span class="eco-badge">Vercel</span>
            </a>
            <a href="https://flask-developer-dashboard-portfolio.onrender.com/" target="_blank" rel="noopener noreferrer" class="eco-link-btn">
              <span class="eco-label"><span>🧪</span> Flask Dashboard</span>
              <span class="eco-badge">Render</span>
            </a>
            <a href="https://angular-portfolio-sigma-eight.vercel.app/" target="_blank" rel="noopener noreferrer" class="eco-link-btn">
              <span class="eco-label"><span>🅰️</span> Angular Portfolio</span>
              <span class="eco-badge">Vercel</span>
            </a>
            <a href="https://profile-card-angular.vercel.app/" target="_blank" rel="noopener noreferrer" class="eco-link-btn">
              <span class="eco-label"><span>🪪</span> Angular Profile Card</span>
              <span class="eco-badge">Vercel</span>
            </a>
          </div>
        </div>

        <!-- Project Hubs Column -->
        <div class="ecosystem-col">
          <div class="ecosystem-col-title">
            <span>🚀</span> Dedicated Project Hubs
          </div>
          <div class="links-chip-group">
            <a href="https://charanepuri.github.io/javascript-projects-portfolio/" target="_blank" rel="noopener noreferrer" class="eco-link-btn">
              <span class="eco-label"><span>📜</span> JavaScript Projects Website</span>
              <span class="eco-badge">GitHub Pages</span>
            </a>
            <a href="https://charanepuri.github.io/django-projects-hub/" target="_blank" rel="noopener noreferrer" class="eco-link-btn">
              <span class="eco-label"><span>⚡</span> Django Projects Hub</span>
              <span class="eco-badge">GitHub Pages</span>
            </a>
            <a href="https://charanepuri.github.io/react-projects-hub/" target="_blank" rel="noopener noreferrer" class="eco-link-btn">
              <span class="eco-label"><span>⚛️</span> React Projects Hub</span>
              <span class="eco-badge">GitHub Pages</span>
            </a>
          </div>
        </div>
      </div>

      <!-- Social Connections Row -->
      <div class="socials-row">
        <a href="https://www.linkedin.com/in/charan-teja-972aa9231" target="_blank" rel="noopener noreferrer" class="social-pill social-linkedin">
          <svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
          LinkedIn
        </a>
        <a href="https://github.com/charanepuri" target="_blank" rel="noopener noreferrer" class="social-pill social-github">
          <svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
          GitHub
        </a>
        <a href="https://www.instagram.com/_just_call_me_charan_tej" target="_blank" rel="noopener noreferrer" class="social-pill social-instagram">
          <svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
          Instagram
        </a>
        <a href="https://www.snapchat.com/add/justcalltej2003?share_id=o3MYfXqlpYE&locale=en-IN" target="_blank" rel="noopener noreferrer" class="social-pill social-snapchat">
          <svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24"><path d="M12.001 2c-3.834 0-6.223 2.654-6.223 5.485 0 1.442.668 2.636 1.488 3.491.137.143.208.33.208.52 0 .428-.43.766-.991 1.15-.494.338-1.096.75-1.096 1.427 0 .543.435.98 1.13 1.14.364.084.774.137 1.206.182.261.027.424.238.384.499-.085.551-.309 1.48-1.706 1.839-.415.106-.728.375-.728.742 0 .684 1.106 1.246 2.64 1.414.288.031.503.267.498.556-.019 1.094.757 1.555 1.455 1.555.515 0 1.047-.197 1.637-.604.421-.29.967-.29 1.388 0 .59.407 1.122.604 1.637.604.698 0 1.474-.461 1.455-1.555-.005-.289.21-.525.498-.556 1.534-.168 2.64-.73 2.64-1.414 0-.367-.313-.636-.728-.742-1.397-.359-1.621-1.288-1.706-1.839-.04-.261.123-.472.384-.499.432-.045.842-.098 1.206-.182.695-.16 1.13-.597 1.13-1.14 0-.677-.602-1.089-1.096-1.427-.561-.384-.991-.722-.991-1.15 0-.19.071-.377.208-.52.82-.855 1.488-2.049 1.488-3.491 0-2.831-2.389-5.485-6.223-5.485z"/></svg>
          Snapchat
        </a>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer>
    <div class="footer-content">
      <div>
        <strong>DevLog Hub</strong> &bull; Developed for Charan Teja's Engineering Portfolio
      </div>
      <div class="footer-links">
        <a href="https://github.com/charanepuri/DevLogHub" target="_blank" rel="noopener noreferrer">GitHub Repository</a>
        <a href="https://www.linkedin.com/in/charan-teja-972aa9231" target="_blank" rel="noopener noreferrer">LinkedIn Profile</a>
        <a href="#top">Back to Top</a>
        <a href="javascript:void(0)" onclick="shareCollection()">Share Collection</a>
      </div>
      <p style="font-size: 0.8rem; color: var(--text-muted); opacity: 0.8;">
        Pure HTML5, Internal CSS &amp; Vanilla JavaScript &bull; Fast, Fully Responsive &amp; Zero External Dependencies
      </p>
    </div>
  </footer>

  <script>
    const POSTS_DATA = %DATA_PLACEHOLDER%;

    // State
    let currentCategory = 'all';
    let searchQuery = '';
    let sortMethod = 'original';

    // Flatten all items with extra metadata
    const allPosts = [];
    POSTS_DATA.forEach(cat => {
      cat.posts.forEach((p) => {
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
    document.getElementById('countDocs').textContent = allPosts.filter(p => p.categoryId === 'tech-docs').length;
    document.getElementById('countPython').textContent = allPosts.filter(p => p.categoryId === 'python').length;
    document.getElementById('countDjango').textContent = allPosts.filter(p => p.categoryId === 'django').length;
    document.getElementById('countFlask').textContent = allPosts.filter(p => p.categoryId === 'flask').length;
    document.getElementById('countSql').textContent = allPosts.filter(p => p.categoryId === 'sql-mysql').length;
    document.getElementById('countWeb').textContent = allPosts.filter(p => p.categoryId === 'web-projects').length;
    document.getElementById('countReact').textContent = allPosts.filter(p => p.categoryId === 'react-projects').length;
    document.getElementById('countDjangoApp').textContent = allPosts.filter(p => p.categoryId === 'django-projects').length;
    document.getElementById('countFlaskApp').textContent = allPosts.filter(p => p.categoryId === 'flask-projects').length;
    document.getElementById('countAIApp').textContent = allPosts.filter(p => p.categoryId === 'ai-projects').length;
    document.getElementById('countTechGlossary').textContent = allPosts.filter(p => p.categoryId === 'tech-glossary').length;
    document.getElementById('countDevProd').textContent = allPosts.filter(p => p.categoryId === 'dev-productivity').length;
    document.getElementById('countProj').textContent = allPosts.filter(p => p.categoryId === 'projects').length;
    document.getElementById('countAdvPy').textContent = allPosts.filter(p => p.categoryId === 'advanced-python').length;
    document.getElementById('countIntern').textContent = allPosts.filter(p => p.categoryId === 'internships').length;

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
        const isLinkedIn = post.url && (post.url.includes('linkedin.com') || post.url.includes('lnkd.in'));
        const linkedInBtn = isLinkedIn ? `
          <a href="${post.url}" target="_blank" rel="noopener noreferrer" class="btn-link" title="Read Post on LinkedIn">
            <svg width="14" height="14" fill="currentColor" viewBox="0 0 24 24"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
            <span>LinkedIn</span>
          </a>
        ` : '';

        const liveBtn = post.liveUrl ? `
          <a href="${post.liveUrl}" target="_blank" rel="noopener noreferrer" class="btn-link btn-live" title="Open Live Application">
            <span>🌐 Live</span>
          </a>
        ` : '';

        const ghBtn = post.githubUrl ? `
          <a href="${post.githubUrl}" target="_blank" rel="noopener noreferrer" class="btn-link btn-github" title="View GitHub Repository">
            <svg width="13" height="13" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
            <span>Code</span>
          </a>
        ` : '';

        const docBtn = post.docUrl ? `
          <a href="${post.docUrl}" target="_blank" rel="noopener noreferrer" class="btn-link btn-doc" title="View Project Documentation">
            <span>📄 Doc</span>
          </a>
        ` : '';

        const driveBtn = post.driveUrl ? `
          <a href="${post.driveUrl}" target="_blank" rel="noopener noreferrer" class="btn-link btn-drive" title="View Project Demo / Drive Resource">
            <span>📁 Drive</span>
          </a>
        ` : '';

        const fallbackBtn = (!isLinkedIn && !liveBtn && !ghBtn && !driveBtn) ? `
          <a href="${post.url}" target="_blank" rel="noopener noreferrer" class="btn-link" title="Open Resource">
            <span>View Link</span>
          </a>
        ` : '';

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
              <div class="card-actions-group">
                ${linkedInBtn}
                ${liveBtn}
                ${ghBtn}
                ${docBtn}
                ${driveBtn}
                ${fallbackBtn}
              </div>
              <button class="btn-copy" onclick="copyPostLink('${post.liveUrl || post.url}', this)" title="Copy Post URL" aria-label="Copy post link">
                <svg width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z"/></svg>
              </button>
            </div>
          </article>
        `;
      }).join('');
    }

    function getPostSummary(post) {
      if (post.description) {
        return escapeHtml(post.description);
      }
      switch (post.categoryId) {
        case 'tech-docs':
          return `Comprehensive technical documentation and reference guide covering architectural paradigms, runtime execution models, and visual systems.`;
        case 'python':
          return `Hands-on Python milestone covering core mechanics, data structures, OOP principles, and clean Pythonic logic.`;
        case 'django':
          return `Django engineering milestone focusing on backend enterprise architecture, database models, view controllers, and REST APIs.`;
        case 'flask':
          return `Flask web development milestone demonstrating lightweight routing, request lifecycles, template rendering, and practical backend APIs.`;
        case 'projects':
          return `Real-world project build featuring end-to-end implementation details, architectural choices, and practical engineering solutions.`;
        case 'sql-mysql':
          return `Database engineering milestone focusing on relational data queries, complex joins, aggregation mechanics, views, and triggers.`;
        case 'web-projects':
          return `Frontend web application engineered with semantic HTML5, modern CSS3 styling, and modular JavaScript, featuring interactive UI states, responsive layout, and clean client-side logic.`;
        case 'react-projects':
          return `Modern React application engineered with reusable component architecture, client-side routing, state hooks, and high-performance interactive UI.`;
        case 'django-projects':
          return `Enterprise Django full-stack web application engineered with modular app architecture, ORM schemas, view controllers, and production deployment.`;
        case 'flask-projects':
          return `Production-ready Flask application featuring lightweight modular routing, WebSocket communications, REST APIs, and responsive UI integration.`;
        case 'ai-projects':
          return `AI-integrated generative application leveraging large language models, structured prompt pipelines, real-time inference, and modern web interfaces.`;
        case 'tech-glossary':
          return `Multi-architecture interactive tech terminology and software engineering glossary platform engineered across HTML5, React, Django, Angular, and Flask.`;
        case 'dev-productivity':
          return `Modular developer productivity tool engineered across multi-architecture evolutions from responsive frontend utilities to robust full-stack production platforms.`;
        case 'advanced-python':
          return `Advanced Python runtime topics including concurrency, multithreading, regex pattern engines, generators, and data libraries.`;
        case 'internships':
          return `Career milestone documenting real-world internship experiences, software engineering contributions, and verified certifications.`;
        default:
          return `Technical documentation and practical software engineering milestone.`;
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
          title: "Charan Teja's Engineering & Learning Hub",
          text: "Explore Charan Teja's complete 200+ milestone roadmap across Technical Documentation, Python, Django, Flask, SQL, and AI Projects!",
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
      localStorage.setItem('devlog-theme', newTheme);
    }

    // Initialize Theme
    const savedTheme = localStorage.getItem('devlog-theme') || 'dark';
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

print(f"Generated index.html successfully with all {total_count} items! Size: {len(full_html)} bytes")
