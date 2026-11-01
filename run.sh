#!/bin/sh
# Mac / Linux launcher. Installs Flask and psutil into a private .venv folder
# (newer Ubuntu and Homebrew Python block installing into the system Python).
cd "$(dirname "$0")" || exit 1

if [ ! -x .venv/bin/python ]; then
    echo "First run: setting up .venv ..."
    if ! python3 -m venv .venv; then
        echo "Could not create a virtual environment."
        echo "On Ubuntu/Debian run:  sudo apt install python3-venv   and try again."
        rm -rf .venv
        exit 1
    fi
fi
.venv/bin/python -m pip install -q -r requirements.txt || exit 1

echo "Open http://127.0.0.1:5000 in your browser (Ctrl+C here to stop)"
.venv/bin/python app.py "$@"
