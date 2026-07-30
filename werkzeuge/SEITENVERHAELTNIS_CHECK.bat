@echo off
cd /d "%~dp0"
py seitenverhaeltnis_check.py 2>nul || python seitenverhaeltnis_check.py
set /p antwort="Abweichende Videos automatisch anpassen? (j/n) "
if /i "%antwort%"=="j" (py seitenverhaeltnis_check.py --fix 2>nul || python seitenverhaeltnis_check.py --fix)
pause
