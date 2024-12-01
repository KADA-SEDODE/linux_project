#!/bin/bash

echo "Lancement de l'application Flask..."
cd "$(dirname "$0")/../"  # Naviguer vers le dossier racine de webapp
python3 app.py
