from flask import Flask, render_template, request, redirect, session, url_for
from scraper.case_f import generate_captcha
import os
from db import log_query  # If you log into SQLite/Postgres
import traceback

app = Flask(__name__)
app.secret_key = 'your-secret-key'

@app.route('/')
def index():
    session['captcha'] = generate_captcha()
    return render_template('index.html')

@app.route('/case-details', methods=['POST'])
def case_details():
    user_captcha = request.form['captcha'].strip().upper()
    actual_captcha = session.get('captcha', '')

    if user_captcha != actual_captcha:
        error = "Invalid CAPTCHA. Please try again."
        session['captcha'] = generate_captcha()
        return render_template('index.html', error=error)

    court = request.form['court']
    case_type = request.form['case_type']
    case_number = request.form['case_number']
    year = request.form['year']
    
    data = fetch_case_details(case_type, case_number, year)

    log_query(case_type, case_number, year, data.get('raw_html'))


    return render_template('case_details.html',**data)


if __name__ == '__main__':
    os.makedirs('static', exist_ok=True)
    app.run(debug=True)