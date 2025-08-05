@echo off
echo ==========================================
echo    FFmpeg Setup Helper
echo ==========================================
echo.
echo This script will help you download and setup ffmpeg.
echo.
echo Step 1: Download ffmpeg
echo ------------------------
echo 1. Go to: https://www.gyan.dev/ffmpeg/builds/
echo 2. Click "release builds"
echo 3. Download "ffmpeg-release-essentials.zip"
echo.
echo Step 2: Extract files
echo ---------------------
echo 1. Extract the downloaded zip file
echo 2. You'll get a folder like "ffmpeg-6.x.x-essentials_build"
echo 3. Rename it to just "ffmpeg"
echo 4. Copy the entire "ffmpeg" folder to this directory
echo.
echo Your folder structure should look like:
echo   YouTube-Simple-Flet\
echo   ├── youtube_simple_flet.py
echo   ├── build.bat
echo   └── ffmpeg\
echo       ├── bin\
echo       │   └── ffmpeg.exe
echo       ├── doc\
echo       └── presets
echo.
echo Once done, run build.bat to create your executable!
echo.
pause