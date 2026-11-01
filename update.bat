@echo off
rem Get the newest problems (your saved code and history are not touched)
cd /d "%~dp0"
git pull --ff-only
pause
