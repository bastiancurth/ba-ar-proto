@echo off
cd /d "%~dp0"
py einrichten.py 2>nul || python einrichten.py
pause
