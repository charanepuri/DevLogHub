import io
import sys
import re
import json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def clean_slug(slug):
    s = re.sub(r'^(flask-learning-?|django-|learning-|day-\d+-?)', '', slug, flags=re.IGNORECASE)
    s = re.sub(r'^(day\s*\d+\s*)', '', s, flags=re.IGNORECASE)
    words = s.replace('-', ' ').strip()
    return words.title()

flask_known = {
    'Day 19': 'Flask RESTful APIs & Serialization',
    'Day 20': 'Request Data, Headers & JSON Parsing',
    'Day 21': 'User Authentication & Password Hashing',
    'Day 22': 'Flask-Login & Session Security',
    'Day 27': 'Email Notifications & Background Tasks',
    'Day 29': 'Flask Caching & Performance Optimization',
    'Day 30': 'Unit Testing Flask Apps with Pytest',
    'Day 31': 'Gunicorn & Nginx Production Deployment',
    'Day 33': 'Full-Stack Flask Architecture & WebSockets'
}

categories = [
    {
        'id': 'tech-docs',
        'name': "Technical Documentation & Concept Guides",
        'shortName': "Technical Docs",
        'tagline': "Deep-dive Guides on JavaScript internals, Django Architecture, Infographics & Project Docs",
        'badge': "Documentation",
        'accent': "#f59e0b",
        'icon': "📚",
        'count': 0,
        'posts': []
    },
    {
        'id': 'python',
        'name': 'Python 50-Day Challenge',
        'shortName': 'Python 50D',
        'tagline': 'Core Fundamentals, Slicing, OOP Mastery, Decorators & Problem Solving',
        'badge': '50 Days',
        'accent': '#38bdf8',
        'icon': '🐍',
        'count': 0,
        'posts': []
    },
    {
        'id': 'django',
        'name': 'Django 40-Day Series',
        'shortName': 'Django 40D',
        'tagline': 'Enterprise Full-Stack Architecture, ORM, DRF REST APIs & Production Deployment',
        'badge': '40 Days',
        'accent': '#10b981',
        'icon': '⚡',
        'count': 0,
        'posts': []
    },
    {
        'id': 'flask',
        'name': 'Flask Daily Learning Series',
        'shortName': 'Flask Mastery',
        'tagline': 'Lightweight Microservices, Dynamic Templating, DB Integration & APIs',
        'badge': '33 Days',
        'accent': '#c084fc',
        'icon': '🧪',
        'count': 0,
        'posts': []
    },
    {
        'id': 'sql-mysql',
        'name': 'SQL & Database Engineering',
        'shortName': 'SQL & MySQL',
        'tagline': 'Advanced JOINs, Window Functions, Subqueries, Triggers, Views & PDBC',
        'badge': 'Databases',
        'accent': '#06b6d4',
        'icon': '🗄️',
        'count': 0,
        'posts': []
    },
    {
        'id': 'web-projects',
        'name': 'HTML, CSS & JavaScript Projects',
        'shortName': 'Web Apps',
        'tagline': 'Interactive Frontend Applications, Responsive Web Experiences, UI Clones & Tools',
        'badge': 'Web Dev',
        'accent': '#eab308',
        'icon': '🌐',
        'count': 0,
        'posts': []
    },
    {
        'id': 'react-projects',
        'name': 'React Applications & SPAs',
        'shortName': 'React Apps',
        'tagline': 'Single Page Applications, Modern Component Architecture, Interactive State & Dashboards',
        'badge': 'React.js',
        'accent': '#00d8ff',
        'icon': '⚛️',
        'count': 0,
        'posts': []
    },
    {
        'id': 'django-projects',
        'name': 'Django Web Applications & Systems',
        'shortName': 'Django Apps',
        'tagline': 'Enterprise Full-Stack Architecture, Dynamic ORM Platforms, Translation Engines & Scalable Systems',
        'badge': 'Django Apps',
        'accent': '#10b981',
        'icon': '⚡',
        'count': 0,
        'posts': []
    },
    {
        'id': 'flask-projects',
        'name': 'Flask Web Applications & Microservices',
        'shortName': 'Flask Apps',
        'tagline': 'Production Microservices, Real-Time WebSockets, URL Engines & AI Integrations',
        'badge': 'Flask Apps',
        'accent': '#c084fc',
        'icon': '🧪',
        'count': 0,
        'posts': []
    },
    {
        'id': 'ai-projects',
        'name': 'AI Integrated Applications & LLMs',
        'shortName': 'AI Apps',
        'tagline': 'Generative AI Resume Engines, Code Morphing, Interview Coaches, Multi-Model LLMs & Assistants',
        'badge': 'AI Apps',
        'accent': '#a855f7',
        'icon': '🤖',
        'count': 0,
        'posts': []
    },
    {
        'id': 'tech-glossary',
        'name': 'Tech Glossary Hub',
        'shortName': 'Tech Glossary',
        'tagline': 'Multi-Architecture Engineering: HTML5 Foundation, React Modern SPA, Django Full-Stack, Angular Enterprise & Flask Backend',
        'badge': 'Glossary Hub',
        'accent': '#06b6d4',
        'icon': '📖',
        'count': 0,
        'posts': []
    },
    {
        'id': 'dev-productivity',
        'name': 'Developer Productivity Suite',
        'shortName': 'Productivity Suite',
        'tagline': 'Multi-Architecture Engineering: HTML Foundation, React SPA, Angular Frontend, Flask Backend, Django Platform & Full Stack Evolution',
        'badge': 'Suite',
        'accent': '#6366f1',
        'icon': '🛠️',
        'count': 0,
        'posts': []
    },
    {
        'id': 'projects',
        'name': 'Projects & AI Applications',
        'shortName': 'Projects & AI',
        'tagline': 'LLM Document Chat, Telegram Bots, Translator Apps, Automation & Dashboards',
        'badge': 'Projects',
        'accent': '#f97316',
        'icon': '🚀',
        'count': 0,
        'posts': []
    },
    {
        'id': 'advanced-python',
        'name': 'Advanced Python & Concurrency',
        'shortName': 'Advanced Python',
        'tagline': 'Multithreading, Regex (re), Generators, NumPy, Pandas, Pickling & Exception Handling',
        'badge': 'Deep Dive',
        'accent': '#a3e635',
        'icon': '⚙️',
        'count': 0,
        'posts': []
    },
    {
        'id': 'internships',
        'name': 'Internships & Career Milestones',
        'shortName': 'Career Milestones',
        'tagline': 'Industry Internship Milestones, Offer Letters, Certifications & Experiences',
        'badge': 'Career',
        'accent': '#ec4899',
        'icon': '🎓',
        'count': 0,
        'posts': []
    }
]

cat_by_id = {c['id']: c for c in categories}

# --- 1. Parse PYTHON_DJANGO_FLASK Daily Learning Links.txt ---
with open('PYTHON_DJANGO_FLASK Daily Learning Links.txt', 'r', encoding='utf-8') as f:
    pdf_text = f.read()

pdf_sections = re.split(r'-{10,}', pdf_text)
# section 0: Flask, section 1: Django, section 2: Python
mapping = [cat_by_id['flask'], cat_by_id['django'], cat_by_id['python']]

for idx, sec in enumerate(pdf_sections):
    cat = mapping[idx]
    lines = [l.strip() for l in sec.strip().split('\n')]
    curr_day = None
    for line in lines[1:]:
        if not line: continue
        if line.startswith('http'):
            m = re.search(r'charan-teja-[^_]+_([a-zA-Z0-9\-]+)-activity', line)
            if m:
                topic = clean_slug(m.group(1))
            else:
                topic = flask_known.get(curr_day, 'Practical Framework Concepts & Implementations')
            
            day_label = curr_day if curr_day else 'Milestone'
            if '50Days' in line or '50days' in line:
                day_label = 'Grand Finale 🎉'
                topic = '50 Days of Consistent Python Learning Completed'
            elif '40-day' in (curr_day or '') or 'Lessons Beyond Code' in topic:
                day_label = 'Series Wrap-up 🚀'
                topic = '40 Days of Django: Lessons Beyond Code & Retrospective'
            
            cat['posts'].append({
                'id': f"{cat['id']}-{len(cat['posts'])+1}",
                'day': day_label,
                'topic': topic,
                'url': line
            })
            curr_day = None
        else:
            curr_day = line

# --- 2. Parse Documentation's Topics & LinkedIn Links.txt exclusively into Technical Documentation Track ---
with open("Documentation's Topics & LinkedIn Links.txt", "r", encoding='utf-8', errors='ignore') as f:
    doc_text = f.read()

doc_lines = [l.strip() for l in doc_text.split('\n')]
current_subdomain = "JavaScript"

for i, line in enumerate(doc_lines):
    if not line: continue
    if "JavaScript" in line and not line.startswith("http") and len(line) < 20:
        current_subdomain = "JavaScript"
        continue
    elif "Django" in line and "🐍" in line:
        current_subdomain = "Django"
        continue
    elif "Photo's" in line:
        current_subdomain = "Visual Guides & AI"
        continue
    elif "Other Documentation's" in line:
        current_subdomain = "System Projects"
        continue

    if line.startswith('http'):
        title = "Documentation Guide"
        for p in range(i-1, -1, -1):
            if doc_lines[p]:
                title = doc_lines[p]
                break

        clean_title = title.strip()
        clean_title = re.sub(r'[\u2013\u2014]', ' - ', clean_title)
        clean_title = re.sub(r'\s+', ' ', clean_title).strip()

        # Build appropriate day label indicating it is an in-depth documentation guide
        day_tag = f"Doc: {current_subdomain}"

        cat_by_id['tech-docs']['posts'].append({
            'id': f"doc-{len(cat_by_id['tech-docs']['posts'])+1}",
            'day': day_tag,
            'topic': clean_title,
            'url': line,
            'subdomain': current_subdomain
        })

# --- 3. Parse LinkedIn Posts Links.txt ---
with open("LinkedIn Posts Links.txt", "r", encoding='utf-8', errors='ignore') as f:
    lp_text = f.read()

lp_lines = [l.strip() for l in lp_text.split('\n')]
lp_items = []
for idx, line in enumerate(lp_lines):
    if not line: continue
    if line.startswith('http'):
        title = "LinkedIn Post"
        for p in range(idx - 1, -1, -1):
            if lp_lines[p] and not lp_lines[p].startswith('http'):
                title = lp_lines[p]
                break
        urls = re.findall(r'https?://[^\s]+', line)
        for u in set(urls):
            lp_items.append((title, u))

for raw_title, url in lp_items:
    t_lower = raw_title.lower()
    m = re.search(r'charan-teja-[^_]+_([a-zA-Z0-9\-]+)-activity', url)
    slug = m.group(1) if m else ""
    cleaned_topic = clean_slug(slug) if slug else raw_title

    if any(k in t_lower or k in slug for k in ['internship', 'sysslan', 'code asire', 'codeasire', 'codec', 'saiket', 'offer']):
        if 'completion' in slug or 'completion' in t_lower:
            day_tag = "Certificate 🏆"
        elif 'selected' in t_lower or 'offer' in slug:
            day_tag = "Offer / Selection 🌟"
        else:
            day_tag = "Internship Log 💼"
        
        topic_disp = cleaned_topic
        if 'Certificate' in raw_title or 'Certificate' in cleaned_topic:
            topic_disp = cleaned_topic
        elif len(raw_title) < 60 and not raw_title.startswith('I’m'):
            topic_disp = raw_title

        cat_by_id['internships']['posts'].append({
            'id': f"intern-{len(cat_by_id['internships']['posts'])+1}",
            'day': day_tag,
            'topic': topic_disp,
            'url': url
        })
    elif any(k in t_lower or k in slug for k in ['sql', 'mysql', 'join', 'queries', 'query', 'subqueries', 'triggers', 'pdbc', 'database connection']):
        day_tag = f"SQL Day #{len(cat_by_id['sql-mysql']['posts'])+1}"
        topic_disp = cleaned_topic
        if len(raw_title) <= 50 and not raw_title.startswith('I '):
            topic_disp = raw_title

        cat_by_id['sql-mysql']['posts'].append({
            'id': f"sql-{len(cat_by_id['sql-mysql']['posts'])+1}",
            'day': day_tag,
            'topic': topic_disp,
            'url': url
        })
    elif any(k in t_lower or k in slug for k in ['dashboard', 'translator', 'telegram', 'bot', 'llm', 'chat-with-multiple-pdfs', 'password-strength', 'organizer', 'patterns']):
        day_tag = "App Build 🛠️"
        topic_disp = cleaned_topic
        if len(raw_title) <= 55 and not raw_title.startswith('Built a Python Program to'):
            topic_disp = raw_title

        cat_by_id['projects']['posts'].append({
            'id': f"app-{len(cat_by_id['projects']['posts'])+1}",
            'day': day_tag,
            'topic': topic_disp,
            'url': url
        })
    else:
        day_tag = "Core & Libs ⚙️"
        topic_disp = cleaned_topic
        if len(raw_title) <= 45:
            topic_disp = raw_title

        cat_by_id['advanced-python']['posts'].append({
            'id': f"advpy-{len(cat_by_id['advanced-python']['posts'])+1}",
            'day': day_tag,
            'topic': topic_disp,
            'url': url
        })

# --- 4. Parse projects.txt into HTML, CSS & JavaScript Projects Track ---
with open('projects.txt', 'r', encoding='utf-8', errors='ignore') as f:
    proj_lines = [l.strip() for l in f.readlines()]

blocks = []
curr = []
for l in proj_lines:
    if not l:
        if curr:
            blocks.append(curr)
            curr = []
    else:
        curr.append(l)
if curr:
    blocks.append(curr)

bible_parts = {
    'P1': 'Architecture, Setup & Navigation Shell',
    'P2': 'GitHub Repository & Scripture Directory Structure',
    'P3': 'Scripture Filtering & Dynamic Passage Loading',
    'P4': 'Learning in Public & Scripture Search Mechanics',
    'P5': 'Chapter & Verse Selector UI Controllers',
    'P6': 'Responsive Layout & Mobile Scripture View',
    'P7': 'Dynamic DOM Updates & Content Rendering',
    'P8': 'Local State Management & Caching Pipeline',
    'P9': 'Verse Highlighting & Customization Engine',
    'P10': 'UI/UX Theme Styling & Polished Aesthetics',
    'P11': 'Production GitHub Pages Release & Retrospective'
}

web_posts = cat_by_id['web-projects']['posts']

# Block 2: India Post Digital Tribute
if len(blocks) > 2:
    b2 = blocks[2]
    web_posts.append({
        'id': f"web-{len(web_posts)+1}",
        'day': 'Frontend App 📮',
        'topic': 'India Post Digital Tribute',
        'url': b2[4] if len(b2) > 4 else b2[-1],
        'liveUrl': b2[1] if len(b2) > 1 else '',
        'githubUrl': b2[2] if len(b2) > 2 else '',
        'driveUrl': b2[3] if len(b2) > 3 else ''
    })

# Block 3: T&C Simplifier
if len(blocks) > 3:
    b3 = blocks[3]
    web_posts.append({
        'id': f"web-{len(web_posts)+1}",
        'day': 'SaaS Web App ⚖️',
        'topic': 'Terms & Conditions Simplifier (T&C Simplifier SaaS)',
        'url': b3[4] if len(b3) > 4 else b3[-1],
        'liveUrl': b3[1] if len(b3) > 1 else '',
        'githubUrl': b3[2] if len(b3) > 2 else '',
        'driveUrl': b3[3] if len(b3) > 3 else ''
    })

# Block 4: Anasuya Fan Made Portfolio
if len(blocks) > 4:
    b4 = blocks[4]
    web_posts.append({
        'id': f"web-{len(web_posts)+1}",
        'day': 'Frontend App 🎬',
        'topic': 'Anasuya Filmography & Fan Portfolio Application',
        'url': b4[4] if len(b4) > 4 else b4[-1],
        'liveUrl': b4[1] if len(b4) > 1 else '',
        'githubUrl': b4[2] if len(b4) > 2 else '',
        'driveUrl': b4[3] if len(b4) > 3 else ''
    })

# Block 5: Bible App details (Blocks 6 to 16 are P1 to P11)
if len(blocks) > 5:
    b5 = blocks[5]
    live_bible = b5[1]
    gh_bible = b5[2]
    drive_bible = b5[3]

    # Blocks 6 to 16: Bible App P1 to P11
    for idx, blk in enumerate(blocks[6:17], start=1):
        p_key = f'P{idx}'
        p_url = re.sub(rf'^{p_key}\s+', '', blk[0]).strip()
        web_posts.append({
            'id': f"web-{len(web_posts)+1}",
            'day': f'Bible App {p_key} 📖',
            'topic': f'Bible Reference Application • Part {idx}: {bible_parts[p_key]}',
            'url': p_url,
            'liveUrl': live_bible,
            'githubUrl': gh_bible,
            'driveUrl': drive_bible
        })

# Block 17: Personal Finance Manager
if len(blocks) > 17:
    b17 = blocks[17]
    web_posts.append({
        'id': f"web-{len(web_posts)+1}",
        'day': 'Web Tool 💰',
        'topic': 'Personal Finance Manager (Budget & Expense Tracker)',
        'url': b17[4] if len(b17) > 4 else b17[-1],
        'liveUrl': b17[1] if len(b17) > 1 else '',
        'githubUrl': b17[2] if len(b17) > 2 else '',
        'driveUrl': b17[3] if len(b17) > 3 else ''
    })

# Block 18: 404 Page
if len(blocks) > 18:
    b18 = blocks[18]
    web_posts.append({
        'id': f"web-{len(web_posts)+1}",
        'day': 'UI Component 🎨',
        'topic': 'Interactive 404 Error Page Experience',
        'url': b18[3] if len(b18) > 3 else b18[-1],
        'liveUrl': b18[1] if len(b18) > 1 else '',
        'githubUrl': b18[2] if len(b18) > 2 else ''
    })

# --- 5. Parse React projects into React Applications Track ---
react_posts = cat_by_id['react-projects']['posts']

if len(blocks) > 20:
    b20 = blocks[20]
    react_posts.append({
        'id': f"react-{len(react_posts)+1}",
        'day': 'React SPA ⚡',
        'topic': 'Converter Hub (Unit, Currency & Media Converter Tool)',
        'url': b20[1],
        'liveUrl': b20[1],
        'githubUrl': b20[2],
        'docUrl': b20[3]
    })

if len(blocks) > 21:
    b21 = blocks[21]
    react_posts.append({
        'id': f"react-{len(react_posts)+1}",
        'day': 'Sports Analytics 🏏',
        'topic': 'MS Dhoni Career Records & Analytics Dashboard',
        'url': b21[4],
        'liveUrl': b21[1],
        'githubUrl': b21[2],
        'driveUrl': b21[3]
    })

if len(blocks) > 22:
    b22 = blocks[22]
    react_posts.append({
        'id': f"react-{len(react_posts)+1}",
        'day': 'React App 📖',
        'topic': 'Bible Reference Application (React.js Edition)',
        'url': b22[4],
        'liveUrl': b22[1],
        'githubUrl': b22[2],
        'driveUrl': b22[3]
    })

if len(blocks) > 23:
    b23 = blocks[23]
    react_posts.append({
        'id': f"react-{len(react_posts)+1}",
        'day': 'Cloud Platform ☁️',
        'topic': 'Cloud Explorer (Multi-Service Cloud Resource Navigator)',
        'url': b23[4],
        'liveUrl': b23[1],
        'githubUrl': b23[2],
        'docUrl': b23[3]
    })

if len(blocks) > 24:
    b24 = blocks[24]
    react_posts.append({
        'id': f"react-{len(react_posts)+1}",
        'day': 'Culinary Web App 🍲',
        'topic': 'The Ultimate Biryani Handbook (Culinary Guide & Recipe App)',
        'url': b24[1],
        'liveUrl': b24[1],
        'githubUrl': b24[2],
        'docUrl': b24[3]
    })

if len(blocks) > 25:
    b25 = blocks[25]
    react_posts.append({
        'id': f"react-{len(react_posts)+1}",
        'day': 'Developer Tool 🛠️',
        'topic': 'Smart Error Assistant (Interactive Debugging & Fix Engine)',
        'url': b25[1],
        'liveUrl': b25[1],
        'githubUrl': b25[2]
    })

# --- 6. Parse Flask projects into Flask Web Applications Track ---
flask_app_posts = cat_by_id['flask-projects']['posts']

flask_idx = -1
for i, b in enumerate(blocks):
    if b[0].strip().lower().startswith('flask project'):
        flask_idx = i
        break

if flask_idx != -1:
    fb = blocks[flask_idx+1:]
    # Quick Link URL Shortener
    if len(fb) > 0:
        b0 = fb[0]
        flask_app_posts.append({
            'id': f"flask-app-{len(flask_app_posts)+1}",
            'day': 'Microservice 🔗',
            'topic': 'Quick Link (Flask URL Shortener & Analytics)',
            'url': b0[1],
            'liveUrl': b0[1],
            'githubUrl': b0[2] if len(b0) > 2 else '',
            'driveUrl': b0[3] if len(b0) > 3 else ''
        })
    # CSK Legacy
    if len(fb) > 1:
        b1 = fb[1]
        flask_app_posts.append({
            'id': f"flask-app-{len(flask_app_posts)+1}",
            'day': 'Flask Web App 🏏',
            'topic': 'CSK Legacy (Chennai Super Kings Tribute & Fan Portal)',
            'url': b1[1],
            'liveUrl': b1[1],
            'githubUrl': b1[2] if len(b1) > 2 else ''
        })
    # Real Time Chat Application
    if len(fb) > 2:
        b2 = fb[2]
        flask_app_posts.append({
            'id': f"flask-app-{len(flask_app_posts)+1}",
            'day': 'WebSockets 💬',
            'topic': 'Real-Time Chat Application (Flask & WebSockets)',
            'url': b2[1],
            'liveUrl': b2[1],
            'githubUrl': b2[2] if len(b2) > 2 else '',
            'driveUrl': b2[3] if len(b2) > 3 else ''
        })
    # AI Language Translator
    if len(fb) > 3:
        b3 = fb[3]
        flask_app_posts.append({
            'id': f"flask-app-{len(flask_app_posts)+1}",
            'day': 'AI Web App 🌐',
            'topic': 'AI Language Translator (Deep Translator Web Engine)',
            'url': b3[1],
            'githubUrl': b3[2] if len(b3) > 2 else ''
        })

# --- 7. Parse Django projects into Django Web Applications Track ---
django_app_posts = cat_by_id['django-projects']['posts']

django_idx = -1
for i, b in enumerate(blocks):
    if b[0].strip().lower().startswith('django project'):
        django_idx = i
        break

if django_idx != -1:
    db = blocks[django_idx+1:]
    # Block 1: Translator Web Application
    if len(db) > 1:
        b1 = db[1]
        django_app_posts.append({
            'id': f"django-app-{len(django_app_posts)+1}",
            'day': 'Translation App 🌐',
            'topic': 'Translator Web Application (Django Multi-Language Engine)',
            'url': b1[4] if len(b1) > 4 else b1[1],
            'liveUrl': b1[1],
            'githubUrl': b1[2] if len(b1) > 2 else '',
            'docUrl': b1[3].replace('Documentation Link:', '').strip() if len(b1) > 3 else ''
        })

    # Block 2: Sambar Handbook
    if len(db) > 2:
        b2 = db[2]
        django_app_posts.append({
            'id': f"django-app-{len(django_app_posts)+1}",
            'day': 'Web Application 🍲',
            'topic': 'Sambar Handbook (Traditional Culinary Guide & Django Web App)',
            'url': b2[1],
            'liveUrl': b2[1],
            'githubUrl': b2[2] if len(b2) > 2 else ''
        })

    # Block 3: Smart Quote Generator
    if len(db) > 3:
        b3 = db[3]
        django_app_posts.append({
            'id': f"django-app-{len(django_app_posts)+1}",
            'day': 'Dynamic Engine 💡',
            'topic': 'Smart Quote Generator (Dynamic Inspiration Engine)',
            'url': b3[1],
            'liveUrl': b3[1],
            'githubUrl': b3[2] if len(b3) > 2 else '',
            'driveUrl': b3[3] if len(b3) > 3 else ''
        })

    # Block 4: LinguaFlow | Full-Stack Language Translator
    if len(db) > 4:
        b4 = db[4]
        # b4[0]: title
        # b4[1]: github
        # b4[2]: render
        # b4[3]: Documentation Link
        django_app_posts.append({
            'id': f"django-app-{len(django_app_posts)+1}",
            'day': 'Enterprise App 🌍',
            'topic': 'LinguaFlow (Full-Stack Language Translator & Localization Platform)',
            'url': b4[2] if len(b4) > 2 else b4[1],
            'liveUrl': b4[2] if len(b4) > 2 else '',
            'githubUrl': b4[1] if len(b4) > 1 else '',
            'docUrl': b4[3].replace('Documentation Link:', '').strip() if len(b4) > 3 else ''
        })

# --- 8. Parse AI Integrated projects into AI Integrated Applications Track ---
ai_app_posts = cat_by_id['ai-projects']['posts']

ai_idx = -1
for i, b in enumerate(blocks):
    if b[0].strip().lower().startswith('ai integrated project'):
        ai_idx = i
        break

if ai_idx != -1:
    aib = blocks[ai_idx+1:]
    # Nexora AI
    if len(aib) > 0:
        b0 = aib[0]
        ai_app_posts.append({
            'id': f"ai-app-{len(ai_app_posts)+1}",
            'day': 'AI Assistant 🤖',
            'topic': 'Nexora AI (Intelligent Multi-Modal Generative Assistant)',
            'url': b0[1],
            'liveUrl': b0[1],
            'githubUrl': b0[2] if len(b0) > 2 else '',
            'driveUrl': b0[3] if len(b0) > 3 else ''
        })
    # AI Resume Bullet Improver
    if len(aib) > 1:
        b1 = aib[1]
        ai_app_posts.append({
            'id': f"ai-app-{len(ai_app_posts)+1}",
            'day': 'GenAI Resume 📄',
            'topic': 'AI Resume Bullet Improver (ATS Optimization & Impact Enhancer)',
            'url': b1[1],
            'liveUrl': b1[1],
            'githubUrl': b1[2] if len(b1) > 2 else '',
            'docUrl': b1[3] if len(b1) > 3 else ''
        })
    # AI GitHub Assistant
    if len(aib) > 2:
        b2 = aib[2]
        ai_app_posts.append({
            'id': f"ai-app-{len(ai_app_posts)+1}",
            'day': 'Developer AI 🐙',
            'topic': 'AI GitHub Assistant (Repository Code Insights & Automation)',
            'url': b2[1],
            'liveUrl': b2[1],
            'githubUrl': b2[2] if len(b2) > 2 else '',
            'docUrl': b2[3] if len(b2) > 3 else ''
        })
    # AI Codemorph
    if len(aib) > 3:
        b3 = aib[3]
        ai_app_posts.append({
            'id': f"ai-app-{len(ai_app_posts)+1}",
            'day': 'Code Converter ⚡',
            'topic': 'AI Codemorph (Polyglot Code Migration & Transformation Engine)',
            'url': b3[1],
            'liveUrl': b3[1],
            'githubUrl': b3[2] if len(b3) > 2 else '',
            'docUrl': b3[3] if len(b3) > 3 else ''
        })
    # AI Interview Coach
    if len(aib) > 4:
        b4 = aib[4]
        ai_app_posts.append({
            'id': f"ai-app-{len(ai_app_posts)+1}",
            'day': 'Groq AI Coach 🎯',
            'topic': 'AI Interview Coach (Real-Time Groq-Powered Mock Interviews & Feedback)',
            'url': b4[1],
            'liveUrl': b4[1],
            'githubUrl': b4[2] if len(b4) > 2 else '',
            'docUrl': b4[3] if len(b4) > 3 else ''
        })

# --- 9. Parse Tech Glossary Hub into dedicated unified section ---
tech_glossary_posts = cat_by_id['tech-glossary']['posts']
tgh_match = re.search(r'Tech Glossary Hub\s*\n(.*?)(?=Developer Productivity Suite|\Z)', '\n'.join(proj_lines), re.DOTALL)
if tgh_match:
    tgh_section_text = tgh_match.group(1).strip()
    version_badges_tgh = {
        'HTML Version': 'HTML Foundation 🌐',
        'React Version': 'React Modern SPA ⚛️',
        'Django Version': 'Django Full-Stack ⚡',
        'Angular Version': 'Angular Enterprise 🅰️',
        'Flask Version': 'Flask Backend 🧪',
        'Full Stack Version': 'Production Full Stack 🚀'
    }

    tgh_version_descriptions = {
        'HTML Version': 'Interactive tech terminology dictionary and glossary application built with semantic HTML5, CSS3, and modern Vanilla JavaScript. Features real-time search, category filtering, responsive typography, and clean client-side lookup.',
        'React Version': 'Modern Single Page Application evolution of Tech Glossary Hub built with React.js. Features component-based glossary cards, live search filtering, category exploration, state hooks, and responsive modern UI.',
        'Django Version': 'Enterprise-grade full-stack glossary platform engineered with Django, Python, and dynamic relational models. Supports comprehensive database querying, category navigation, admin panel management, and production-ready server-side rendering.',
        'Angular Version': 'Enterprise frontend edition of Tech Glossary Hub architected with Angular and TypeScript. Implements modular component hierarchies, dependency injection services, client-side routing, and structured design patterns.',
        'Flask Version': 'Lightweight backend web edition of Tech Glossary Hub powered by Python and Flask. Designed for fast server-side response times, dynamic glossary term routing, template rendering, and clean microservice architecture.'
    }

    v_matches = re.findall(r'(^[ \t]*(\w+(?:\s+\w+)*\s+Version)[ \t]*\n.*?)(?=(?:^[ \t]*\w+(?:\s+\w+)*\s+Version)|\Z)', tgh_section_text, re.MULTILINE | re.DOTALL)
    for v_full, v_head in v_matches:
        v_title = v_head.strip()
        day_badge = version_badges_tgh.get(v_title, f'{v_title} 📖')
        custom_desc = tgh_version_descriptions.get(v_title, 'Comprehensive multi-framework tech glossary and software engineering terminology knowledge platform.')

        live_m = re.search(r'Live Link:\s*(https://[^\s]+)', v_full)
        gh_m = re.search(r'GitHub Repository:\s*(https://[^\s]+)', v_full)
        doc_m = re.search(r'Documentation Link:\s*(https://[^\s]+)', v_full)
        li_links = re.findall(r'LinkedIn Post Link:\s*(https://[^\s]+)', v_full)

        live_url = live_m.group(1).strip() if live_m else ''
        gh_url = gh_m.group(1).strip() if gh_m else ''
        doc_url = doc_m.group(1).strip() if doc_m else ''

        if v_title == 'Django Version' and len(li_links) >= 3:
            # Add the 3 milestone posts for Django Version to give full transparency
            # Post 1: Milestone 1 - Core Setup & Schemas
            tech_glossary_posts.append({
                'id': f"tech-glossary-{len(tech_glossary_posts)+1}",
                'day': 'Milestone 1 🏗️',
                'topic': 'Tech Glossary Hub (Django) • Progress Update 1: Core Setup & Schemas',
                'url': li_links[0],
                'liveUrl': live_url,
                'githubUrl': gh_url,
                'docUrl': doc_url,
                'description': 'First development milestone of the Django edition of Tech Glossary Hub, documenting initial architectural setup, data models, schema definitions, and project structure.'
            })
            # Post 2: Milestone 2 - Architecture & Models
            tech_glossary_posts.append({
                'id': f"tech-glossary-{len(tech_glossary_posts)+1}",
                'day': 'Milestone 2 ⚙️',
                'topic': 'Tech Glossary Hub (Django) • Progress Update 2: Architecture & Models',
                'url': li_links[1],
                'liveUrl': live_url,
                'githubUrl': gh_url,
                'docUrl': doc_url,
                'description': 'Second milestone detailing database model relationships, view controllers, query optimizations, and template rendering integration in Django.'
            })
            # Post 3: Official Platform Launch
            tech_glossary_posts.append({
                'id': f"tech-glossary-{len(tech_glossary_posts)+1}",
                'day': 'Platform Launch 🚀',
                'topic': 'Tech Glossary Hub (Full-Stack Django Knowledge System)',
                'url': li_links[2],
                'liveUrl': live_url,
                'githubUrl': gh_url,
                'docUrl': doc_url,
                'description': custom_desc
            })
        else:
            primary_url = li_links[0] if li_links else (live_url or gh_url or '')
            entry = {
                'id': f"tech-glossary-{len(tech_glossary_posts)+1}",
                'day': day_badge,
                'topic': f'Tech Glossary Hub • {v_title}',
                'url': primary_url,
                'description': custom_desc
            }
            if live_url:
                entry['liveUrl'] = live_url
            if gh_url:
                entry['githubUrl'] = gh_url
            if doc_url:
                entry['docUrl'] = doc_url
            tech_glossary_posts.append(entry)

# --- 10. Parse Developer Productivity Suite into dedicated unified section ---
dev_prod_posts = cat_by_id['dev-productivity']['posts']
suite_match = re.search(r'Developer Productivity Suite\s*\n(.*?)$', '\n'.join(proj_lines), re.DOTALL)
if suite_match:
    section_text = suite_match.group(1)
    
    # 1. Introduction Milestone Post
    intro_match = re.search(r'Introduction LinkedIn Post Link:\s*(https://[^\s]+)', section_text)
    if intro_match:
        intro_url = intro_match.group(1).strip()
        dev_prod_posts.append({
            'id': f"dev-prod-{len(dev_prod_posts)+1}",
            'day': 'Suite Overview 🚀',
            'topic': 'Developer Productivity Suite • Official Introduction & Architecture Roadmap',
            'url': intro_url,
            'description': 'Official introduction and architectural roadmap for the Developer Productivity Suite — chronicling the evolution from HTML/CSS/JS foundation to modern React SPA, Angular enterprise frontend, Flask backend, Django platform, and full-stack production platform.'
        })

    # 2. Version Editions (v1.0 to v6.0)
    version_badges = {
        'v1.0': 'Foundation v1.0 🌐',
        'v2.0': 'React SPA v2.0 ⚛️',
        'v3.0': 'Angular v3.0 🅰️',
        'v4.0': 'Flask v4.0 🧪',
        'v5.0': 'Django v5.0 ⚡',
        'v6.0': 'Full Stack v6.0 🚀'
    }

    v_matches = re.findall(r'(v\d+\.\d+\s*—[^\n]+)(.*?)(?=(?:v\d+\.\d+\s*—)|$)', section_text, re.DOTALL)
    for title_line, body in v_matches:
        v_title = title_line.strip()
        # Find version key like 'v1.0'
        v_num_match = re.search(r'(v\d+\.\d+)', v_title)
        v_key = v_num_match.group(1) if v_num_match else 'Edition'
        day_badge = version_badges.get(v_key, f'{v_key} 🛠️')

        desc_match = re.search(r'Description:\s*(.*?)(?=(?:GitHub Repository|Live Link|Documentation Link|LinkedIn Post Link|\Z))', body, re.DOTALL)
        desc_text = desc_match.group(1).strip() if desc_match else ''
        # Replace newlines with single space for clean text
        desc_text = ' '.join(desc_text.split())

        gh_match = re.search(r'GitHub Repository:\s*(https://[^\s]+)', body)
        live_match = re.search(r'Live Link:\s*(https://[^\s]+)', body)
        doc_match = re.search(r'Documentation Link:\s*(https://[^\s]+)', body)
        li_match = re.search(r'LinkedIn Post Link:\s*(https://[^\s]+)', body)

        post_entry = {
            'id': f"dev-prod-{len(dev_prod_posts)+1}",
            'day': day_badge,
            'topic': f'Developer Productivity Suite • {v_title}',
            'description': desc_text
        }

        if gh_match:
            post_entry['githubUrl'] = gh_match.group(1).strip()
        if live_match:
            post_entry['liveUrl'] = live_match.group(1).strip()
        if doc_match:
            post_entry['docUrl'] = doc_match.group(1).strip()
        if li_match:
            post_entry['url'] = li_match.group(1).strip()
        else:
            # Fallback primary url to Live or GitHub if LinkedIn not yet available
            post_entry['url'] = post_entry.get('liveUrl') or post_entry.get('githubUrl') or ''

        dev_prod_posts.append(post_entry)

for c in categories:
    c['count'] = len(c['posts'])

total_posts = sum(c['count'] for c in categories)
print(f"Total compiled posts: {total_posts}")
for c in categories:
    print(f"  {c['icon']} {c['name']} ({c['shortName']}): {c['count']} posts")

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(categories, f, indent=2)

print("Saved clean, properly structured data.json successfully!")
