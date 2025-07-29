@echo off
echo Building YouTube Simple Flet App...
echo.

:: Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

:: Install requirements
echo Installing Python packages...
pip install flet pyinstaller yt-dlp

:: Clean previous builds
echo Cleaning previous builds...
if exist dist rmdir /s /q dist
if exist build rmdir /s /q build

:: Build the application
echo Building executable...
pyinstaller YouTube-Simple-Flet.spec

:: Check if build was successful
if exist "dist\YouTube-Simple-Flet.exe" (
    echo.
    echo Build successful! Executable created at: dist\YouTube-Simple-Flet.exe
    echo.
    echo You can now run the executable.
) else (
    echo.
    echo Build failed! Check the output above for errors.
)

pause