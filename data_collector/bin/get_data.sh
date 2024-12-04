# #!/bin/bash
# Obtenir le chemin absolu du répertoire contenant le script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Afficher un message d'information
echo "Lancement de la collecte des données..."

# Lancer le script Python pour collecter les données
python3 "$SCRIPT_DIR/../collect_data.py"
