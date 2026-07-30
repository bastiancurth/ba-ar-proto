@echo off
cd /d "%~dp0"
start "" pythonw cockpit_basti.py 2>nul || py cockpit_basti.py || python cockpit_basti.py
