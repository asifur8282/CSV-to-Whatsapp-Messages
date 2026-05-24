@echo off
REM WhatsApp AutoMessenger - Windows Setup Script
REM This script helps set up the WhatsApp AutoMessenger

echo.
echo ========================================
echo  WhatsApp AutoMessenger Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.14 or higher from https://www.python.org
    pause
    exit /b 1
)

echo Step 1: Installing dependencies...
REM Create virtual environment
python -m venv .venv
if %errorlevel% neq 0 (
    echo Error: Failed to create virtual environment
    pause
    exit /b 1
)

REM Activate virtual environment and install packages
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

echo Step 2: Checking ChromeDriver...
python check_chromedriver.py
if %errorlevel% neq 0 (
    echo Warning: ChromeDriver setup needs attention
    echo Please download ChromeDriver from https://chromedriver.chromium.org/
    echo matching your Chrome browser version
)

echo.
echo ========================================
echo Setup complete!
echo ========================================
echo.
echo To run the WhatsApp AutoMessenger:
echo   .venv\Scripts\python.exe main.py
echo.
pause
