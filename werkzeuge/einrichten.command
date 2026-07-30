#!/bin/bash
cd "$(dirname "$0")"
python3 einrichten.py "$@"
read -p "Fertig. Enter zum Schliessen."
