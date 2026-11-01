#!/bin/sh
# Mac / Linux launcher
cd "$(dirname "$0")" || exit 1
python3 -m pip install -q -r requirements.txt || python3 -m pip install -q --user -r requirements.txt
echo "Open http://127.0.0.1:5000"
python3 app.py
