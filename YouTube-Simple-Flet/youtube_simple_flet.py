#!/usr/bin/env python3
import flet as ft
import os
import sys
import configparser
import yt_dlp

def get_ffmpeg_path():
    """Get the path to bundled ffmpeg or system ffmpeg"""
    if getattr(sys, 'frozen', False):
        # Running as PyInstaller executable
        base_path = sys._MEIPASS
    else:
        # Running as script
        base_path = os.path.dirname(os.path.abspath(__file__))
    
    # Check for bundled ffmpeg
    bundled_ffmpeg = os.path.join(base_path, "ffmpeg", "ffmpeg.exe")
    if os.path.exists(bundled_ffmpeg):
        return bundled_ffmpeg
    
    # Fallback to system ffmpeg
    return "ffmpeg"

def main(page: ft.Page):
    page.title = "Simple YouTube Converter"
    page.window_width = 700
    page.window_height = 500
    
    # Settings file path
    settings_file = os.path.join(os.path.expanduser("~"), ".youtube_simple_settings.ini")
    
    def load_last_directory():
        try:
            config = configparser.ConfigParser()
            if os.path.exists(settings_file):
                config.read(settings_file)
                if 'Settings' in config and 'last_directory' in config['Settings']:
                    last_dir = config['Settings']['last_directory']
                    if os.path.exists(last_dir):
                        return last_dir
        except Exception:
            pass
        return os.path.expanduser("~/Downloads")
    
    def save_last_directory(directory):
        try:
            config = configparser.ConfigParser()
            if os.path.exists(settings_file):
                config.read(settings_file)
            if 'Settings' not in config:
                config.add_section('Settings')
            config['Settings']['last_directory'] = directory
            with open(settings_file, 'w') as f:
                config.write(f)
        except Exception:
            pass
    
    url_field = ft.TextField(label="YouTube URL", expand=True)
    filename_field = ft.TextField(label="Custom Filename (optional)", expand=True, hint_text="Leave empty for auto-generated name")
    output_dir_field = ft.TextField(label="Output Directory", value=load_last_directory(), expand=True, read_only=True)
    status_text = ft.Text("Ready", color="green")
    
    def browse_directory(e):
        def get_directory_result(e: ft.FilePickerResultEvent):
            if e.path:
                output_dir_field.value = e.path
                save_last_directory(e.path)
                page.update()
        
        get_directory_dialog = ft.FilePicker(on_result=get_directory_result)
        page.overlay.append(get_directory_dialog)
        page.update()
        get_directory_dialog.get_directory_path(dialog_title="Select Output Directory")

    def convert_click(e):
        url = url_field.value.strip()
        if not url:
            status_text.value = "Please enter a URL"
            status_text.color = "red"
            page.update()
            return
        
        output_dir = output_dir_field.value.strip()
        if not output_dir:
            output_dir = os.path.expanduser("~/Downloads")
            output_dir_field.value = output_dir
            
        if not os.path.exists(output_dir):
            try:
                os.makedirs(output_dir, exist_ok=True)
            except Exception as e:
                status_text.value = f"Cannot create directory: {str(e)}"
                status_text.color = "red"
                page.update()
                return
            
        status_text.value = "Converting..."
        status_text.color = "orange"
        page.update()
        
        try:
            # Get custom filename or use auto-generated
            custom_filename = filename_field.value.strip()
            if custom_filename:
                # Sanitize filename
                invalid_chars = '<>:"/\\|?*'
                for char in invalid_chars:
                    custom_filename = custom_filename.replace(char, '_')
                custom_filename = custom_filename.strip(' .')
                output_template = os.path.join(output_dir, f"{custom_filename}.%(ext)s")
            else:
                output_template = os.path.join(output_dir, "%(title)s.%(ext)s")
            
            # yt-dlp options with bundled ffmpeg
            ffmpeg_path = get_ffmpeg_path()
            ydl_opts = {
                'format': 'bestaudio/best',
                'extractaudio': True,
                'audioformat': 'wav',
                'outtmpl': output_template,
                'noplaylist': True,
                'ffmpeg_location': ffmpeg_path,
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            
            status_text.value = "Success! File saved to output directory"
            status_text.color = "green"
        except yt_dlp.DownloadError as e:
            status_text.value = f"Download failed: {str(e)}"
            status_text.color = "red"
        except Exception as e:
            import traceback
            status_text.value = f"An unexpected error occurred:\n{traceback.format_exc()}"
            status_text.color = "red"
        
        page.update()
    
    convert_btn = ft.ElevatedButton("Convert to WAV", on_click=convert_click)
    browse_btn = ft.ElevatedButton("Browse", on_click=browse_directory)
    
    page.add(
        ft.Column([
            ft.Text("Simple YouTube to WAV Converter", size=20, weight=ft.FontWeight.BOLD),
            ft.Divider(),
            url_field,
            filename_field,
            ft.Row([
                output_dir_field,
                browse_btn
            ], spacing=10),
            ft.Divider(),
            convert_btn,
            status_text
        ], spacing=15, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

if __name__ == "__main__":
    ft.app(target=main)
