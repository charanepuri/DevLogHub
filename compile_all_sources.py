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

# Block 5: Bible App P1
if len(blocks) > 5:
    b5 = blocks[5]
    live_bible = b5[1]
    gh_bible = b5[2]
    drive_bible = b5[3]
    p1_url = re.sub(r'^P1\s+', '', b5[4]).strip()
    web_posts.append({
        'id': f"web-{len(web_posts)+1}",
        'day': 'Bible App P1 📖',
        'topic': f'Bible Reference Application • Part 1: {bible_parts["P1"]}',
        'url': p1_url,
        'liveUrl': live_bible,
        'githubUrl': gh_bible,
        'driveUrl': drive_bible
    })

    # Blocks 6 to 15: Bible App P2 to P11
    for idx, blk in enumerate(blocks[6:16], start=2):
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

# Block 16: Personal Finance Manager
if len(blocks) > 16:
    b16 = blocks[16]
    web_posts.append({
        'id': f"web-{len(web_posts)+1}",
        'day': 'Web Tool 💰',
        'topic': 'Personal Finance Manager (Budget & Expense Tracker)',
        'url': b16[4] if len(b16) > 4 else b16[-1],
        'liveUrl': b16[1] if len(b16) > 1 else '',
        'githubUrl': b16[2] if len(b16) > 2 else '',
        'driveUrl': b16[3] if len(b16) > 3 else ''
    })

# Block 17: 404 Page
if len(blocks) > 17:
    b17 = blocks[17]
    web_posts.append({
        'id': f"web-{len(web_posts)+1}",
        'day': 'UI Component 🎨',
        'topic': 'Interactive 404 Error Page Experience',
        'url': b17[3] if len(b17) > 3 else b17[-1],
        'liveUrl': b17[1] if len(b17) > 1 else '',
        'githubUrl': b17[2] if len(b17) > 2 else ''
    })

# --- 5. Parse React projects into React Applications Track ---
react_posts = cat_by_id['react-projects']['posts']

if len(blocks) > 19:
    b19 = blocks[19]
    react_posts.append({
        'id': f"react-{len(react_posts)+1}",
        'day': 'React SPA ⚡',
        'topic': 'Converter Hub (Unit, Currency & Media Converter Tool)',
        'url': b19[1],
        'liveUrl': b19[1],
        'githubUrl': b19[2],
        'docUrl': b19[3]
    })

if len(blocks) > 20:
    b20 = blocks[20]
    react_posts.append({
        'id': f"react-{len(react_posts)+1}",
        'day': 'Sports Analytics 🏏',
        'topic': 'MS Dhoni Career Records & Analytics Dashboard',
        'url': b20[4],
        'liveUrl': b20[1],
        'githubUrl': b20[2],
        'driveUrl': b20[3]
    })

if len(blocks) > 21:
    b21 = blocks[21]
    react_posts.append({
        'id': f"react-{len(react_posts)+1}",
        'day': 'React App 📖',
        'topic': 'Bible Reference Application (React.js Edition)',
        'url': b21[4],
        'liveUrl': b21[1],
        'githubUrl': b21[2],
        'driveUrl': b21[3]
    })

if len(blocks) > 22:
    b22 = blocks[22]
    react_posts.append({
        'id': f"react-{len(react_posts)+1}",
        'day': 'Cloud Platform ☁️',
        'topic': 'Cloud Explorer (Multi-Service Cloud Resource Navigator)',
        'url': b22[4],
        'liveUrl': b22[1],
        'githubUrl': b22[2],
        'docUrl': b22[3]
    })

if len(blocks) > 23:
    b23 = blocks[23]
    react_posts.append({
        'id': f"react-{len(react_posts)+1}",
        'day': 'Culinary Web App 🍲',
        'topic': 'The Ultimate Biryani Handbook (Culinary Guide & Recipe App)',
        'url': b23[1],
        'liveUrl': b23[1],
        'githubUrl': b23[2],
        'docUrl': b23[3]
    })

if len(blocks) > 24:
    b24 = blocks[24]
    react_posts.append({
        'id': f"react-{len(react_posts)+1}",
        'day': 'Developer Tool 🛠️',
        'topic': 'Smart Error Assistant (Interactive Debugging & Fix Engine)',
        'url': b24[1],
        'liveUrl': b24[1],
        'githubUrl': b24[2]
    })

for c in categories:
    c['count'] = len(c['posts'])

total_posts = sum(c['count'] for c in categories)
print(f"Total compiled posts: {total_posts}")
for c in categories:
    print(f"  {c['icon']} {c['name']} ({c['shortName']}): {c['count']} posts")

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(categories, f, indent=2)

print("Saved clean, properly structured data.json successfully!")
