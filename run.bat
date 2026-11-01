@echo off
cd /d "%~dp0"
python --version >nul 2>nul || (
    echo Python was not found. Install it from https://www.python.org/downloads/
    echo and tick "Add python.exe to PATH" in the installer, then try again.
    pause
    exit /b 1
)
python -m pip install -q -r requirements.txt || (
    echo Installing Flask/psutil failed. Check your internet connection and try again.
    pause
    exit /b 1
)
echo Open http://127.0.0.1:5000 in your browser. Close this window to stop the judge.
start "" http://127.0.0.1:5000
python app.py
pause
