@echo off
echo ==========================================
echo    YouTube Simple Flet - Build Script
echo ==========================================
echo.

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

:: Clean previous build environment
echo [1/6] Cleaning previous build environment...
if exist youtube_build_env (
    rmdir /s /q youtube_build_env
)
if exist build (
    rmdir /s /q build
)
if exist dist (
    rmdir /s /q dist
)

:: Create fresh virtual environment
echo [2/6] Creating fresh virtual environment...
python -m venv youtube_build_env
if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    pause
    exit /b 1
)

:: Activate virtual environment and install dependencies
echo [3/6] Installing dependencies...
call youtube_build_env\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

:: Check if ffmpeg folder exists
echo [4/6] Checking ffmpeg...
if not exist ffmpeg (
    echo WARNING: ffmpeg folder not found!
    echo Please download ffmpeg and extract it to the 'ffmpeg' folder
    echo Download from: https://www.gyan.dev/ffmpeg/builds/
    pause
    echo Continuing anyway...
)

:: Build executable
echo [5/6] Building executable...
pyinstaller YouTube-Simple-Flet.spec
if errorlevel 1 (
    echo ERROR: Build failed
    pause
    exit /b 1
)

:: Clean up build environment
echo [6/6] Cleaning up...
deactivate
rmdir /s /q youtube_build_env

echo.
echo ==========================================
echo           BUILD COMPLETED!
echo ==========================================
echo.
echo Your executable is ready at:
echo   dist\YouTube-Simple-Flet.exe
echo.
echo You can now distribute this single file
echo to users - no Python installation required!
echo.
pause