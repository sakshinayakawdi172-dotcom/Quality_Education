# LearnBridge — Quality Education Website

A starter educational website built with Flask, SQLite, HTML, CSS, and JavaScript.

## Features
- Responsive landing page
- Courses page with sample learning paths
- About page
- Contact form that stores submissions in SQLite

## Run on Windows
1. Install Python 3.10+ from https://www.python.org/downloads/ and enable **Add Python to PATH**.
2. Extract this ZIP and open the folder in VS Code.
3. In the terminal, run:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   py -m pip install -r requirements.txt
   py app.py
   ```

4. Open http://127.0.0.1:5000 in your browser.

If PowerShell blocks activation, run `py -m pip install -r requirements.txt` and then `py app.py` without activating the environment.

The database file `learnbridge.db` is created automatically when the app starts. Change `app.secret_key` before deploying publicly. This is a starter project, not a production-ready learning management system.
