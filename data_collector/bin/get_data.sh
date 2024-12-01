# #!/bin/bash
# source ../conf/collector.conf  # charge le fichier collector.conf situé dans le dossier ../conf.

# # echo "Form ID is set as: ${form_id}"  est inutile
# echo "Target path is set as: ${target_path}"

# python3 collect_data.py


# #!/bin/bash

# # Obtenir le chemin absolu du répertoire contenant le script
# SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# # Charger le fichier de configuration
# source "$SCRIPT_DIR/../conf/collector.conf"

# echo "Target path is set as: ${target_path}"

# # Lancer le script Python pour collecter les données
# python3 "$SCRIPT_DIR/../collect_data.py"

#!/bin/bash

# # Obtenir le chemin absolu du répertoire contenant le script
# SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# # Charger le fichier de configuration
# source "$SCRIPT_DIR/../conf/collector.conf"

# echo "Target path is set as: ${target_path}"

# # Lancer le script Python pour collecter les données
# python3 "$SCRIPT_DIR/../collect_data.py"

#!/bin/bash

# Obtenir le chemin absolu du répertoire contenant le script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Afficher un message d'information
echo "Lancement de la collecte des données..."

# Lancer le script Python pour collecter les données
python3 "$SCRIPT_DIR/../collect_data.py"
