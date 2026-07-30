@echo off
cd /d "%~dp0"
start "" pythonw werkstatt.py 2>nul || py werkstatt.py || python werkstatt.py
