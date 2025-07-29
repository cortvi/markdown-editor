@echo off
REM Markdown Editor Launcher for Windows
REM This batch file makes it easy to launch the Markdown Editor on Windows

echo.
echo ========================================
echo   Markdown Editor - Windows Launcher
echo ========================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python 3.8+ from https://python.org/downloads/windows/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo Python found: 
python --version

REM Check if we're in the right directory
if not exist "main.py" (
    echo ERROR: main.py not found in current directory
    echo.
    echo Please navigate to the markdown-editor folder and run this script
    echo Example: cd C:\path\to\markdown-editor
    echo.
    pause
    exit /b 1
)

echo Project files found: OK

REM Check if dependencies are installed
echo.
echo Checking dependencies...
python -c "import PyQt6, markdown, pymdownx" >nul 2>&1
if errorlevel 1 (
    echo.
    echo Some dependencies are missing. Installing now...
    echo.
    pip install -r requirements.txt
    if errorlevel 1 (
        echo.
        echo ERROR: Failed to install dependencies
        echo Please run manually: pip install -r requirements.txt
        echo.
        pause
        exit /b 1
    )
    echo Dependencies installed successfully!
) else (
    echo Dependencies: OK
)

echo.
echo Starting Markdown Editor...
echo.

REM Launch the application
if "%~1"=="" (
    REM No file specified, launch normally
    python main.py
) else (
    REM File specified as argument, open it
    python main.py "%~1"
)

REM Check if the application exited with an error
if errorlevel 1 (
    echo.
    echo ERROR: The application encountered an error
    echo.
    pause
)

echo.
echo Markdown Editor closed.
pause