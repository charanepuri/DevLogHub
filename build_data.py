import re
import json

with open('PYTHON_DJANGO_FLASK Daily Learning Links.txt', 'r', encoding='utf-8') as f:
    text = f.read()

sections = re.split(r'-{10,}', text)

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
        'shortName': 'Python',
        'tagline': 'Core Fundamentals, Data Structures, OOP Mastery & Problem Solving',
        'badge': '50 Days Complete',
        'accent': '#38bdf8',
        'gradient': 'linear-gradient(135deg, #0284c7 0%, #38bdf8 100%)',
        'icon': '🐍',
        'count': 0,
        'posts': []
    },
    {
        'id': 'django',
        'name': 'Django & DRF 40-Day Series',
        'shortName': 'Django',
        'tagline': 'Enterprise Full-Stack Architecture, ORM, REST APIs & Production Deployment',
        'badge': '40 Days Complete',
        'accent': '#10b981',
        'gradient': 'linear-gradient(135deg, #047857 0%, #10b981 100%)',
        'icon': '⚡',
        'count': 0,
        'posts': []
    },
    {
        'id': 'flask',
        'name': 'Flask Daily Learning Series',
        'shortName': 'Flask',
        'tagline': 'Lightweight Microservices, Dynamic Templating, DB Integration & APIs',
        'badge': '33 Days Complete',
        'accent': '#a855f7',
        'gradient': 'linear-gradient(135deg, #7c3aed 0%, #c084fc 100%)',
        'icon': '🧪',
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
        if not line:
            continue
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

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(categories, f, indent=2)

print("Exported data.json successfully!")
for c in categories:
    print(f"- {c['name']}: {c['count']} posts")
