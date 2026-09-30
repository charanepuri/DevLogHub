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
  <link rel="stylesheet" href="styles.css">
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
        Pure HTML5, Modular CSS3 &amp; Vanilla JavaScript &bull; Fast, Fully Responsive &amp; Zero External Dependencies
      </p>
    </div>
  </footer>

  <script>
    window.DEVLOG_DATA = %DATA_PLACEHOLDER%;
  </script>
  <script src="script.js"></script>
</body>
</html>
'''

data_json_str = json.dumps(categories, separators=(',', ':'))
full_html = html_template.replace('%DATA_PLACEHOLDER%', data_json_str)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print(f"Generated index.html successfully with all {total_count} items! Size: {len(full_html)} bytes")
