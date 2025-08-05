import sqlite3
from datetime import datetime

DB_FILE = 'court_logs.db'

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS case_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            case_type TEXT,
            case_number TEXT,
            filing_year TEXT,
            query_time TEXT,
            timestamp TEXT,
            raw_response TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_query(case_type, case_number, filing_year, raw_response):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO case_logs (case_type, case_number, filing_year, timestamp, raw_response)
        VALUES (?, ?, ?, ?, ?)
    ''', (case_type, case_number, filing_year, datetime.now().isoformat(), raw_response))
    conn.commit()
    conn.close()
