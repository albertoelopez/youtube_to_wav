# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['youtube_simple_flet.py'],
    pathex=[],
    binaries=[],
    datas=[('ffmpeg', 'ffmpeg')],
    hiddenimports=[
        'flet', 
        'flet.fastapi',
        'flet.page',
        'flet.control',
        'flet.utils',
        'engineio.async_drivers.threading',
        'uvicorn',
        'uvicorn.lifespan.on',
        'watchdog',
        'watchdog.observers',
        'watchdog.events'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='YouTube-Simple-Flet',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
