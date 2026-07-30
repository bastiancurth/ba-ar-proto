@echo off
cd /d "%~dp0"
py sync_medien.py  2>nul || python sync_medien.py 
pause
