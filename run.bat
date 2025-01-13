@echo off
python --version 2>nul | findstr /r "3\.[0-9]*\.[0-9]*" >nul
if errorlevel 1 (
    echo Python 3.x is not installed or not found in PATH
    echo Please download and install Python from:
    echo https://www.python.org/downloads/
    pause
) else (
    python for_dummies.py
)

pause