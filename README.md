# 🚀 NLP Workstation Hub

A high-performance, secure Python Web Application built with the Flask framework and powered by the modern Google GenAI SDK architecture. This workstation provides an executive-grade interface to interact with advanced natural language processing vectors, allowing users to execute linguistic data transformations seamlessly.

🔗 **Live Deployment:** [nlp-web-app-flask.onrender.com](https://nlp-web-app-flask.onrender.com)

---

## 🧭 Architecture & Core Features

The engine is structured as a protected data pipeline. All processing interfaces are behind an active security perimeter, ensuring endpoints cannot be bypassed via direct URL injections.

*   **🛡️ Secure Session Routing:** Implements cryptographically signed session guards across all analytical dashboards to protect data integrity and restrict access to authenticated users.
*   **📊 Sentiment Analysis:** Evaluates textual variants to extract exact negative, neutral, and positive confidence metrics.
*   **🎭 Emotion Prediction:** Maps complex semantic structures across emotional parameters including Joy, Fear, Surprise, Sadness, and Anger.
*   **🔍 Named Entity Matrix (NER):** Isolates key operational entities like geographic locations, profiles, dates, and corporate brands.
*   **📝 Smart Summarizer & TL;DR:** Generates quick-read metrics, core takeaways, and high-impact structural summaries.
*   **✍️ Grammar & Tone Architect:** Normalizes syntax properties and scales custom text inputs into a polished business persona.
*   **🔒 Abuse & Toxicity Detection:** Screens inputs for hazardous keywords, aggressive language, and flags risk severity matrices (Low/Medium/High).

---

## 💻 Tech Stack & Engineering Core

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Backend Engine** | Python 3 / Flask | Core routing, business logic, and session state management. |
| **Linguistic Model** | Google GenAI SDK (`gemini-2.5-flash`) | Contextual reasoning and structured text generation. |
| **Frontend UI** | HTML5 / Tailwind CSS | Responsive, dark-mode terminal layout optimized for desktop viewports. |
| **Database Layer** | JSON File-System DB | Local dynamic file-based user profile persistence. |
| **Production Server** | Gunicorn | High-concurrency WSGI application server wrapper. |

---

## 📁 Repository Structure

```text
NLP-Web-App-Flask/
│
├── templates/               # Frontend structural UI elements
│   ├── login.html           # System access interface
│   ├── register.html        # New profile onboarding
│   ├── profile.html         # Main Pipeline Control Hub
│   └── dashboard.html       # Split-screen analytical workbench
│
├── api.py                   # Modern Google GenAI API client configuration
├── app.py                   # Core Flask application, security guards, and routing
├── db.py                    # JSON Database engine with cloud auto-initialization
├── requirements.txt         # Production library dependency locks
└── .gitignore               # Excludes environment tokens and local databases
