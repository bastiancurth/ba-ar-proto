#!/bin/bash
cd "$(dirname "$0")"
python3 seitenverhaeltnis_check.py "$@"
read -p "Fertig. Enter zum Schliessen."
