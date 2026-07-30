#!/bin/bash
cd "$(dirname "$0")"
python3 video_komprimieren.py "$@"
read -p "Fertig. Enter zum Schliessen."
