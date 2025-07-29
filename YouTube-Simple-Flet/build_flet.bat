@echo off
echo Building with Flet Pack (recommended for Flet apps)...
echo.

:: Install flet if not already installed
pip install flet yt-dlp

:: Clean previous builds
if exist dist rmdir /s /q dist

:: Use flet pack instead of pyinstaller
echo Building with flet pack...
flet pack youtube_simple_flet.py --name "YouTube-Simple-Flet" --add-data "ffmpeg;ffmpeg"

if exist "dist\YouTube-Simple-Flet.exe" (
    echo.
    echo Build successful with flet pack!
    echo Executable: dist\YouTube-Simple-Flet.exe
) else (
    echo.
    echo Flet pack failed, trying PyInstaller with simpler config...
    pyinstaller --onefile --windowed --name "YouTube-Simple-Flet" youtube_simple_flet.py
)

pause