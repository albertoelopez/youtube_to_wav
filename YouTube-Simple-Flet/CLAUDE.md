# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Flet-based desktop application that converts YouTube videos to WAV audio files. The application is designed to be distributed as a single, self-contained Windows executable using PyInstaller.

## Architecture

The application follows a single-file architecture with these key components:

- **Main Application** (`youtube_simple_flet.py`): Flet GUI application with embedded yt-dlp library calls
- **FFmpeg Integration**: Bundled ffmpeg binaries for audio conversion (located in `ffmpeg/` directory)
- **Settings Persistence**: User preferences stored in `~/.youtube_simple_settings.ini`
- **Build System**: Automated PyInstaller-based build process with dependency isolation

### Key Design Decisions

- **yt-dlp as Library**: Uses yt-dlp programmatically via Python API instead of subprocess calls to eliminate external dependencies
- **FFmpeg Path Resolution**: `get_ffmpeg_path()` function handles both bundled (PyInstaller) and development scenarios
- **Dependency Bundling**: PyInstaller spec includes explicit hidden imports for yt-dlp modules and bundles ffmpeg directory

## Build Commands

### Development
```bash
# Run the application directly
python youtube_simple_flet.py

# Create development virtual environment 
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### Production Build
```bash
# Automated build (recommended)
build.bat

# Manual build steps
python -m venv youtube_build_env
youtube_build_env\Scripts\activate
pip install -r requirements.txt
pyinstaller YouTube-Simple-Flet.spec
```

### FFmpeg Setup (One-time)
```bash
# Interactive setup helper
setup_ffmpeg.bat

# Manual: Download from https://www.gyan.dev/ffmpeg/builds/
# Extract to project_root/ffmpeg/ directory
```

## Critical Files

- `YouTube-Simple-Flet.spec`: PyInstaller configuration with ffmpeg bundling and yt-dlp hidden imports
- `requirements.txt`: Pinned dependency versions for reproducible builds
- `build.bat`: Automated build script that creates isolated environment
- `ffmpeg/`: Directory containing ffmpeg binaries (must be manually downloaded)

## Build Dependencies

The application requires these exact versions (pinned in requirements.txt):
- flet==0.24.1 (GUI framework)
- yt-dlp==2024.12.13 (YouTube download library)
- pyinstaller==6.6.0 (Executable packaging)

## Common Issues

**FFmpeg Path Resolution**: The `get_ffmpeg_path()` function handles both PyInstaller bundled paths (`sys._MEIPASS`) and development paths. When modifying, ensure both scenarios work.

**yt-dlp Integration**: Uses library API with `yt_dlp.YoutubeDL(ydl_opts)` instead of subprocess. This requires explicit hidden imports in the PyInstaller spec.

**Build Environment Isolation**: The build process creates a fresh virtual environment to avoid system Python conflicts. Don't bypass this isolation when troubleshooting build issues.

**Antivirus Interference**: PyInstaller executables commonly trigger false positives. The build script includes guidance for handling this.