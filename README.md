# PyPulse Hub | Charan Teja's Engineering & Learning Hub 🚀

> **A curated showcase of 150+ verified engineering posts, documentation guides, and architecture breakdowns covering Core Python, Django, DRF, Flask, JavaScript, Visual Infographics, and Console Applications.**

---

## 🌟 Overview

**PyPulse Hub** is a lightweight, responsive, single-page application built strictly with **pure semantic HTML5, internal CSS3, and internal vanilla JavaScript**. No external CSS frameworks, no npm dependencies, and no build steps are required.

The application organizes, visualizes, and indexes all LinkedIn technical posts authored by **Charan Teja**, establishing an interactive portfolio for recruiters, developers, and learners.

---

## 📂 Project Structure

```text
P_D_F/
│
├── index.html                                  # Standalone web app (HTML5 + Internal CSS + Internal JS)
├── README.md                                   # Documentation & setup guide
├── PYTHON_DJANGO_FLASK Daily Learning Links.txt # Daily learning links file (Python, Django, Flask)
├── Documentation's Topics & LinkedIn Links.txt # Core web, visual guides, algorithms & project docs
├── build_all_data.py                           # Parser script combining all links into data.json
├── generate_site.py                            # Compiler script injecting parsed data into index.html
└── data.json                                   # Compiled dataset (150 technical milestones)
```

---

## 🎯 Highlights & Learning Tracks

The learning roadmap spans **150 documented posts, deep dives, and visual guides**:

| Track                            | Items / Days   | Core Focus Areas                                                                                                                                                           |
| :------------------------------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🐍 **Python 50-Day Challenge**   | **51 posts**   | Slicing, List/Set/Dict Comprehensions, Functions, File Handling, OOP (Inheritance, Abstraction, Encapsulation, Polymorphism), Decorators, Algorithms & Pattern Problems    |
| ⚡ **Django & DRF Series**       | **43 posts**   | Project Architecture, MVT & ORM, Admin Panel, Middleware, Forms & CSRF, Signals, DRF Serializers, API Endpoints, JWT Authentication, Caching & Deployment                  |
| 🧪 **Flask Mastery Series**      | **33 posts**   | Microframework setup, Jinja2 Templates & Inheritance, Static Files, SQLite DB, Flask-SQLAlchemy, CRUD, Sessions & Cookies, RESTful APIs, Error Handling & Blueprints       |
| 📜 **JavaScript & Web Core**     | **5 posts**    | JS vs TypeScript, Execution Context & Call Stack, Event Loop & Async/Await, DOM Manipulation, Modern ES6+ Features                                                         |
| 📊 **Visual Infographics & AI**  | **16 posts**   | AI Agents Explained, ChatGPT for Devs, System Architecture, Social Media Recommendation Algorithms (Instagram, YouTube, LinkedIn, Snapchat, WhatsApp), Framework Face-offs |
| 💻 **Console & System Projects** | **2 projects** | In-depth documentation of complete production console applications built in C and Python                                                                                   |

---

## ⚡ Features

- **100% Pure HTML5, Internal CSS & Vanilla JS**: Single portable file (`index.html`) that works directly in any web browser without any local server required.
- **Track Filtering**: Instantly switch between _All Tracks_, _Python_, _Django & DRF_, _Flask_, _JavaScript_, _Visual Guides & AI_, or _Console Projects_.
- **Instant Search**: Real-time live filtering by keyword, day number (e.g., `Day 10`), concept name (e.g., `JWT`, `ORM`, `AI Agents`, `Event Loop`), or topic description.
- **Sorting Options**: View posts by roadmap sequence or sort alphabetically (A-Z, Z-A).
- **Dark / Light Mode**: Seamless theme switcher preserving user preference in `localStorage`.
- **Direct LinkedIn Links**: Each card features a direct button to read the full original post on LinkedIn.
- **One-Click Link Copying**: Copy any post's direct LinkedIn link straight to the clipboard with animated toast feedback.
- **Responsive Design**: Designed for desktops, tablets, and smartphones with modern glassmorphism styling and smooth animations.

---

## 🚀 How to Run Locally

### Option 1: Direct File Opening (Simplest)

Double-click `index.html` or drag and drop it into any modern web browser (Chrome, Edge, Firefox, Safari, Brave).

### Option 2: Local HTTP Server (Optional)

```powershell
python -m http.server 8000 --bind 127.0.0.1
```

Then visit: `http://localhost:8000` in your web browser.

---

## 🛠️ Re-generating or Updating Links

If you add new links to either `PYTHON_DJANGO_FLASK Daily Learning Links.txt` or `Documentation's Topics & LinkedIn Links.txt`:

```powershell
python generate_site.py
```

This re-parses both files and updates `index.html` with the latest counts and cards.

---

## 👤 Author

- **Charan Teja**
- **LinkedIn Profile**: [linkedin.com/in/charan-teja-972aa9231](https://www.linkedin.com/in/charan-teja-972aa9231)
