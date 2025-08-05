# YouTube Simple Flet - Build Instructions

## Quick Start

1. **Setup ffmpeg** (one-time only):
   ```cmd
   setup_ffmpeg.bat
   ```
   Follow the instructions to download and extract ffmpeg.

2. **Build the executable**:
   ```cmd
   build.bat
   ```
   This creates a fully self-contained `dist\YouTube-Simple-Flet.exe`

## What the build script does

1. ✅ Cleans any previous builds
2. ✅ Creates fresh Python virtual environment  
3. ✅ Installs exact dependency versions
4. ✅ Bundles everything with PyInstaller
5. ✅ Creates single executable file
6. ✅ Cleans up temporary files

## Requirements

- Python 3.11+ installed
- Internet connection (for downloading dependencies)
- ffmpeg folder in project directory

## Troubleshooting

**"Python is not installed"**
- Install Python from https://python.org
- Make sure "Add Python to PATH" is checked

**"ffmpeg folder not found"**
- Run `setup_ffmpeg.bat` and follow instructions
- Or manually download from https://www.gyan.dev/ffmpeg/builds/

**Build fails with antivirus error**
- Temporarily disable Windows Defender real-time protection
- Add project folder to antivirus exclusions

## Distribution

The final `dist\YouTube-Simple-Flet.exe` is completely standalone:
- No Python installation required on target machines
- No pip dependencies needed
- Works on any Windows 10/11 system
- Single file distribution

## File Structure

```
YouTube-Simple-Flet/
├── youtube_simple_flet.py      # Main application code
├── YouTube-Simple-Flet.spec    # PyInstaller configuration  
├── requirements.txt            # Python dependencies
├── build.bat                   # Automated build script
├── setup_ffmpeg.bat           # FFmpeg setup helper
├── ffmpeg/                     # FFmpeg binaries (you add this)
│   └── bin/ffmpeg.exe
└── dist/                       # Final executable (created by build)
    └── YouTube-Simple-Flet.exe
```