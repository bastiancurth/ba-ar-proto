#!/bin/bash
cd "$(dirname "$0")"
python3 sync_medien.py "$@"
read -p "Fertig. Enter zum Schliessen."
