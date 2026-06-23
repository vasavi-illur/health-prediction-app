# MIRA Health Records

A health prediction CRUD application built for the **Junior AI/ML Developer (WFH)** technical assessment — Task 1.

Patients are registered with their basic details and three blood test values (Glucose, Haemoglobin, Cholesterol). On save, the app runs those values through a built-in AI/ML prediction engine and automatically writes a risk remark into the **Remarks** column — no manual step required.

---

## Tech stack

| Layer | Choice |
|---|---|
| Backend | Python 3 + Flask |
| Frontend | HTML, CSS, Bootstrap 5, vanilla JavaScript |
| Database | SQLite (file-based, zero setup) |
| AI/ML | Rule-based clinical reference-range model (see [AI/ML prediction approach](#aiml-prediction-approach)) |

---

## Project structure

```
health-prediction-app/
├── app/
│   ├── __init__.py          # Application factory (create_app)
│   ├── config.py            # Settings loaded from environment variables
│   ├── database.py          # SQLite connection handling + schema
│   ├── validators.py        # All input validation logic
│   ├── ai_service.py        # AI/ML health risk prediction engine
│   ├── routes.py            # All CRUD routes (Create, Read, Update, Delete)
│   ├── errors.py            # Custom 404 / 500 error pages
│   ├── static/
│   │   ├── css/style.css    # Full design system / styling
│   │   └── js/app.js        # Delete-confirmation modal wiring
│   └── templates/
│       ├── base.html        # Shared layout (header, footer, flash messages)
│       ├── index.html       # Records list + search
│       ├── form.html        # Create / edit form (shared template)
│       ├── detail.html      # Single patient detail view
│       └── error.html       # 404 / 500 page
├── instance/                # SQLite database file lives here (auto-created)
├── run.py                   # App entry point
├── seed.py                  # Optional: populate sample demo data
├── requirements.txt
├── .env.example              # Template for environment variables
├── .gitignore
└── README.md
```

---

## 1. Prerequisites

- Python 3.9 or newer
- pip

Check your version:
```bash
python3 --version
```

---

## 2. Setup instructions

### Step 1 — Clone or unzip the project, then move into it
```bash
cd health-prediction-app
```

### Step 2 — Create a virtual environment (recommended)
```bash
python3 -m venv venv

# Activate it:
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Configure environment variables
```bash
cp .env.example .env
```
The app runs out of the box with the defaults in `.env.example`. You only need to edit `.env` if you want to set a custom `SECRET_KEY` or plug in a real external `HEALTH_API_KEY` (see [AI/ML prediction approach](#aiml-prediction-approach)).

### Step 5 — Run the application
```bash
python run.py
```
You should see:
```
* Running on http://127.0.0.1:5000
```
The SQLite database and the `patients` table are created automatically on first run — there is no manual database setup step.

Open **http://127.0.0.1:5000** in your browser.

### (Optional) Step 6 — Load sample data
To see the app populated with five example patients spanning all three risk levels:
```bash
python seed.py
```

---

## 3. Testing CRUD operations manually

1. **Create** — Click **New record**, fill in the form, and submit.
   - Try submitting with an invalid email, a future date of birth, or non-numeric lab values to see validation errors.
   - On a valid submit, you're redirected to the list and the new row appears with an AI-generated risk pill (Low / Moderate / High) already filled in.
2. **Read** — The home page lists every record. Use the search box to filter by name or email. Click the eye icon on any row to see the full detail view, including the complete AI remark text.
3. **Update** — Click the pencil icon on any row, change any field (e.g. raise the glucose value), and save. The risk remark recalculates automatically based on the new values.
4. **Delete** — Click the trash icon, confirm in the dialog that appears, and the record is removed.

If you prefer the command line, the project also exposes a read-only JSON endpoint for spot-checking data:
```bash
curl http://127.0.0.1:5000/api/patients/1
```

---

## 4. Validation rules implemented

| Field | Rule |
|---|---|
| Full name | Required, max 120 characters |
| Date of birth | Required, must be a real date, **cannot be in the future** |
| Email | Required, must match a standard `name@domain.tld` pattern |
| Glucose / Haemoglobin / Cholesterol | Required, must be **numeric**, cannot be negative |

All validation lives in `app/validators.py` and is shared by both the create and edit routes, so the rules can never drift apart between the two flows.

---

## 5. AI/ML prediction approach

The brief allows either an external AI/ML or Health API, **or** a simple ML/rule-based model if no suitable free API is available. I chose the second option deliberately, for a reason worth explaining in the interview:

Most free public "health prediction" APIs either require paid clinical licensing, are aimed at a completely different use case (e.g. drug lookup, not lab-value risk scoring), or have unstable uptime — none of which I wanted this assessment to depend on. So `app/ai_service.py` implements a transparent **rule-based scoring model** grounded in widely published general-adult reference ranges (fasting glucose, haemoglobin, total cholesterol):

- Each of the three lab values is scored independently against its normal range.
- The three scores are summed into a single risk level: **Low**, **Moderate**, or **High**.
- A plain-English remark is generated explaining *why* (e.g. "Glucose in the prediabetes range; monitor diet and recheck.").

This is wrapped behind one function, `predict_health_risk()`, with a clearly marked extension point (`_call_external_health_api`) where a real third-party API key could be dropped in later — `HEALTH_API_KEY` is already wired through `.env` → `config.py` → `routes.py` for that purpose. Swapping in a real API later would require changing only `app/ai_service.py`; no other file would need to change.

**Disclaimer shown in the app:** this model is for demonstration purposes only and is explicitly not medical advice — this is stated in the footer of every page.

---

## 6. Uploading to GitHub

```bash
# From inside the project folder
git init
git add .
git commit -m "Initial commit: MIRA health prediction CRUD app"

# Create a new repository on GitHub first (via github.com), then:
git remote add origin https://github.com/<your-username>/<your-repo-name>.git
git branch -M main
git push -u origin main
```

**Before pushing**, double-check no secrets are committed:
```bash
git status        # .env should NOT appear in the list of tracked files
cat .gitignore     # confirm .env and instance/*.db are listed
```
The `.env` file and the SQLite database file are already excluded via `.gitignore`. Only `.env.example` (which contains no real secrets) is tracked.

---

## 7. Running in production (optional, for reference)

The built-in `python run.py` server is for local development only. For an always-on deployment, use a production WSGI server such as gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 "run:app"
```

---

## Notes on design choices

- **SQLite over a heavier database** — for a single-table take-home project, SQLite needs zero setup (no separate server to install or configure) while still being a real, persistent, queryable relational database, not a flat file or in-memory dict.
- **Raw SQL over an ORM** — with one table and a handful of queries, parameterised raw SQL (see `app/database.py`) is easier for a reviewer to read top-to-bottom and verify there's no injection risk, without needing to know an ORM's query API first.
- **Application factory pattern** (`create_app()`) — keeps configuration, database setup, and route registration cleanly separated, which is the standard Flask pattern for any project expected to grow past a single file.
