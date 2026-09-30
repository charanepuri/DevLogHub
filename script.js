const POSTS_DATA = window.DEVLOG_DATA || [];

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
