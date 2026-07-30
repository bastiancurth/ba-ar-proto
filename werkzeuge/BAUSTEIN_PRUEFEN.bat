@echo off
cd /d "%~dp0"
py baustein_pruefen.py 2>nul || python baustein_pruefen.py
pause
