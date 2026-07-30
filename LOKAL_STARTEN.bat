@echo off
cd /d "%~dp0"
echo Lokaler Server auf http://localhost:8000  (Beenden: Strg+C)
start msedge "http://localhost:8000/index_v2.html" 2>nul || start "" "http://localhost:8000/index_v2.html"
py werkzeuge\lokal_server.py || python werkzeuge\lokal_server.py
pause
