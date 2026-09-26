import io
import sys
import re
import json

# Ensure utf-8 output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 1. Parse PYTHON_DJANGO_FLASK Daily Learning Links.txt
with open('PYTHON_DJANGO_FLASK Daily Learning Links.txt', 'r', encoding='utf-8') as f:
    pdf_text = f.read()

sections = re.split(r'-{10,}', pdf_text)

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
        'id': 'python',
        'name': 'Python 50-Day Challenge',
        'shortName': 'Python 50D',
        'tagline': 'Core Fundamentals, Data Structures, OOP Mastery & Problem Solving',
        'badge': '50 Days',
        'accent': '#38bdf8',
        'icon': '🐍',
        'count': 0,
        'posts': []
    },
    {
        'id': 'django',
        'name': 'Django & DRF 40-Day Series',
        'shortName': 'Django & DRF',
        'tagline': 'Enterprise Full-Stack Architecture, ORM, REST APIs & Production Deployment',
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
        'id': 'javascript',
        'name': 'JavaScript & Web Fundamentals',
        'shortName': 'JavaScript & Web',
        'tagline': 'Execution Context, Event Loop, DOM Manipulation, ES6+ & TypeScript',
        'badge': 'Core Web',
        'accent': '#facc15',
        'icon': '📜',
        'count': 0,
        'posts': []
    },
    {
        'id': 'infographics',
        'name': 'Visual Infographics & Tech Breakdowns',
        'shortName': 'Visual Tech & AI',
        'tagline': 'Visual Architectural Guides: AI Agents, System Architecture, Algorithms & Tool Comparisons',
        'badge': 'Infographics',
        'accent': '#f43f5e',
        'icon': '📊',
        'count': 0,
        'posts': []
    },
    {
        'id': 'console-projects',
        'name': 'Console & System Projects',
        'shortName': 'Console Projects',
        'tagline': 'In-depth Documentation of Complete C & Python Console-based Real-world Applications',
        'badge': 'Project Docs',
        'accent': '#fb923c',
        'icon': '💻',
        'count': 0,
        'posts': []
    }
]

# Section order in text file: 0 is Flask, 1 is Django, 2 is Python
cat_mapping = [categories[2], categories[1], categories[0]]

for idx, sec in enumerate(sections):
    cat = cat_mapping[idx]
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
    cat['count'] = len(cat['posts'])

# 2. Parse Documentation's Topics & LinkedIn Links.txt
with open("Documentation's Topics & LinkedIn Links.txt", "rb") as f:
    doc_raw = f.read().decode('utf-8', errors='replace')

doc_lines = [l.strip() for l in doc_raw.split('\n')]

current_doc_group = "JS"
for i, line in enumerate(doc_lines):
    if not line:
        continue
    if "Django" in line and "🐍" in line:
        current_doc_group = "Django-Doc"
        continue
    elif "Photo's" in line:
        current_doc_group = "Infographics"
        continue
    elif "Other Documentation's" in line:
        current_doc_group = "Other-Docs"
        continue

    if line.startswith('http'):
        # find the preceding title
        title = "Resource"
        for p in range(i-1, -1, -1):
            if doc_lines[p]:
                title = doc_lines[p]
                break
        
        # Clean title special chars
        title = title.replace('', '–')

        if current_doc_group == "JS":
            categories[3]['posts'].append({
                'id': f"js-{len(categories[3]['posts'])+1}",
                'day': f"Doc #{len(categories[3]['posts'])+1}",
                'topic': title,
                'url': line
            })
        elif current_doc_group == "Django-Doc":
            # Add to Django track as Architecture Documentation
            categories[1]['posts'].append({
                'id': f"django-doc-{len(categories[1]['posts'])+1}",
                'day': "Core Doc 📑",
                'topic': f"Django Deep-Dive: {title}",
                'url': line
            })
        elif current_doc_group == "Infographics":
            categories[4]['posts'].append({
                'id': f"info-{len(categories[4]['posts'])+1}",
                'day': f"Visual Guide #{len(categories[4]['posts'])+1}",
                'topic': title,
                'url': line
            })
        elif current_doc_group == "Other-Docs":
            categories[5]['posts'].append({
                'id': f"proj-{len(categories[5]['posts'])+1}",
                'day': "Full Project 💼",
                'topic': title,
                'url': line
            })

for c in categories:
    c['count'] = len(c['posts'])

total = sum(c['count'] for c in categories)
print(f"Total compiled posts across all categories: {total}")
for c in categories:
    print(f"  {c['icon']} {c['name']}: {c['count']} posts")

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(categories, f, indent=2)

print("Saved combined data.json successfully!")
