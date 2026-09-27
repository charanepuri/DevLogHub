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

for c in categories:
    c['count'] = len(c['posts'])

total_posts = sum(c['count'] for c in categories)
print(f"Total compiled posts: {total_posts}")
for c in categories:
    print(f"  {c['icon']} {c['name']} ({c['shortName']}): {c['count']} posts")

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(categories, f, indent=2)

print("Saved clean, properly structured data.json successfully!")
