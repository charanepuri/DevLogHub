# PyPulse Hub | Charan Teja's Daily Learning Hub 🚀

> **A curated showcase of 125+ daily engineering posts covering Core Python, Django, Django REST Framework (DRF), and Flask.**

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
├── PYTHON_DJANGO_FLASK Daily Learning Links.txt # Raw daily learning links file
├── build_data.py                               # Parser script to process raw text into structured JSON
└── generate_site.py                            # Generator script to inject compiled data into index.html
```

---

## 🎯 Highlights & Learning Tracks

The learning roadmap spans **125 documented posts and milestones**:

| Track                          | Days / Milestones                      | Core Focus Areas                                                                                                                                                            |
| :----------------------------- | :------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 🐍 **Python 50-Day Challenge** | **51 posts** (50 Days + Milestone)     | Slicing, List/Set/Dict Comprehensions, Functions, File Handling, OOP (Inheritance, Abstraction, Encapsulation, Polymorphism), Decorators, Algorithms & Pattern Problems     |
| ⚡ **Django & DRF Series**     | **41 posts** (40 Days + Retrospective) | Project Architecture, Routing & Views, MVT & ORM, Admin Customization, Middleware, Forms, Signals, DRF Serializers, API Endpoints, JWT Authentication, Caching & Deployment |
| 🧪 **Flask Daily Learning**    | **33 posts** (33 Days)                 | Microframework setup, Jinja2 Templates & Inheritance, Static Files, SQLite DB, Flask-SQLAlchemy, CRUD, Sessions & Cookies, RESTful APIs, Error Handling & Blueprints        |

---

## ⚡ Features

- **100% Pure HTML5, Internal CSS & Vanilla JS**: Single portable file (`index.html`) that works right in any web browser without any local server required.
- **Track Filtering**: Instantly switch between _All Tracks_, _Python 50 Days_, _Django & DRF_, and _Flask Mastery_.
- **Instant Search**: Real-time live filtering by keyword, day number (e.g., `Day 10`), concept name (e.g., `JWT`, `ORM`, `Inheritance`), or topic description.
- **Sorting Options**: View posts by roadmap sequence or sort alphabetically (A-Z, Z-A).
- **Dark / Light Mode**: Seamless theme switcher preserving user preference in `localStorage`.
- **Direct LinkedIn Links**: Each card features a direct button to read the full original post on LinkedIn.
- **One-Click Link Copying**: Copy any post's direct LinkedIn link straight to the clipboard with animated toast feedback.
- **Responsive Design**: Designed for desktops, tablets, and smartphones with modern glassmorphism styling and smooth animations.

---

## 🚀 How to Run

### Option 1: Direct File Opening (Simplest)

Double-click `index.html` or drag and drop it into any modern web browser (Chrome, Edge, Firefox, Safari, Brave).

### Option 2: Local HTTP Server (Optional)

If you prefer running via a local server:

```powershell
# Using Python's built-in HTTP server
python -m http.server 8000
```

Then visit: `http://localhost:8000` in your web browser.

---

## 🛠️ Re-generating or Updating Links

If you add new links to `PYTHON_DJANGO_FLASK Daily Learning Links.txt`, update the application by running:

```powershell
python generate_site.py
```

This parses the file and updates `index.html` with the latest data and counts.

---

## 👤 Author

- **Charan Teja**
- **LinkedIn Profile**: [linkedin.com/in/charan-teja-972aa9231](https://www.linkedin.com/in/charan-teja-972aa9231)
