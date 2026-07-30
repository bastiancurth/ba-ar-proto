@echo off
cd /d "%~dp0"
py video_komprimieren.py %* 2>nul || python video_komprimieren.py %*
pause
