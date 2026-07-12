from flask import Flask, render_template, request, redirect, url_for, session
from db import Database
import api
import os

app = Flask(__name__)

# Enforce a secret key to sign session cookies securely
# In production, pull this from your hidden .env file: os.getenv('SECRET_KEY')
app.secret_key = os.getenv("SECRET_KEY", "super-secret-workstation-token-12345")

dbo = Database()


@app.route('/')
def index():
    # If the user is already logged in, take them straight to the hub
    if 'user' in session:
        return redirect(url_for('profile'))
    return render_template('login.html')


@app.route('/register')
def register():
    if 'user' in session:
        return redirect(url_for('profile'))
    return render_template('register.html')


@app.route('/perform_registration', methods=['POST'])
def perform_registration():
    name = request.form.get('user_ka_name')
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    if dbo.insert(name, email, password):
        return render_template('login.html', message="Registration Successful! Kindly login to proceed.")
    else:
        return render_template('register.html', message="This email address is already registered.")


@app.route('/perform_login', methods=['POST'])
def perform_login():
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    if dbo.search(email, password):
        # 🔑 Create the session state for the authenticated user
        session['user'] = email
        return redirect(url_for('profile'))
    else:
        return render_template('login.html', message="Invalid credentials. Please try again.")


@app.route('/logout')
def logout():
    # 🔓 Clear out the session data to log the user out completely
    session.pop('user', None)
    return redirect(url_for('index'))


@app.route('/profile')
def profile():
    # 🛡️ Route Guard: Block access if the user key is missing from the session
    if 'user' not in session:
        return render_template('login.html', message="Access Denied. Please log in first.")
    return render_template('profile.html')


@app.route('/dashboard/<analysis_type>')
def dashboard(analysis_type):
    # 🛡️ Route Guard: Prevent direct URL copy-pasting for dashboard views
    if 'user' not in session:
        return render_template('login.html', message="Access Denied. Please log in first.")

    display_names = {
        "sentiment": "Sentiment Analysis",
        "emotion": "Emotion Prediction",
        "ner": "Named Entity Recognition (NER)",
        "summarizer": "Smart Summarizer & TL;DR",
        "copilot": "Interactive AI Copilot",
        "grammar": "Grammar & Tone Architect",
        "abuse": "Abuse & Toxicity Detection"
    }
    title = display_names.get(analysis_type, "NLP Engine Dashboard")
    return render_template('dashboard.html', analysis_type=analysis_type, title=title)


@app.route('/analyze/<analysis_type>', methods=['POST'])
def analyze(analysis_type):
    # 🛡️ Route Guard: Protect execution endpoints from unauthorized script injections
    if 'user' not in session:
        return render_template('login.html', message="Access Denied. Please log in first.")

    text = request.form.get('input_text')
    result = api.analyze_text(text, analysis_type)

    display_names = {
        "sentiment": "Sentiment Analysis",
        "emotion": "Emotion Prediction",
        "ner": "Named Entity Recognition (NER)",
        "summarizer": "Smart Summarizer & TL;DR",
        "copilot": "Interactive AI Copilot",
        "grammar": "Grammar & Tone Architect",
        "abuse": "Abuse & Toxicity Detection"
    }
    title = display_names.get(analysis_type, "NLP Engine Dashboard")

    return render_template('dashboard.html',
                           analysis_type=analysis_type,
                           title=title,
                           input_text=text,
                           result=result)


if __name__ == '__main__':
    app.run(debug=True)