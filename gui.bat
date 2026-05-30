@echo off
REM WhatsApp AutoMessenger GUI Launcher
echo Starting WhatsApp AutoMessenger GUI...
".venv\Scripts\python.exe" gui.py
if %errorlevel% neq 0 (
    echo.
    echo Error: Failed to start the GUI. Make sure you run setup.bat first to set up the virtual environment.
    pause
)
