#!/bin/bash

echo "Lancement de l'application Flask..."
cd "$(dirname "$0")/../"  # Naviguer vers le dossier racine de webapp
# python3 app.py
python3 app.py > ../log/webapp.log 2>&1
