@echo off
cd /d "%~dp0"
py marker_erstellen.py %* 2>nul || python marker_erstellen.py %*
pause
