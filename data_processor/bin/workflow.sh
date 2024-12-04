#!/bin/bash

# Obtenir le chemin absolu du répertoire contenant ce script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Naviguer vers le répertoire `processor` pour exécuter `core.py`
python3 "$SCRIPT_DIR/../processor/core.py"
