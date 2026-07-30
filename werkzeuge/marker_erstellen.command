#!/bin/bash
cd "$(dirname "$0")"
python3 marker_erstellen.py "$@"
read -p "Fertig. Enter zum Schliessen."
