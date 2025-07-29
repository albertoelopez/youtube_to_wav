@echo off
echo Starting YouTube Simple Flet App in debug mode...
echo.

:: Run with Python directly first to test
echo Testing with Python directly:
python youtube_simple_flet.py
pause

echo.
echo Now testing the executable:
if exist "dist\YouTube-Simple-Flet.exe" (
    echo Running executable with console output...
    "dist\YouTube-Simple-Flet.exe"
) else (
    echo Executable not found. Please build first using build_local.bat
)

pause