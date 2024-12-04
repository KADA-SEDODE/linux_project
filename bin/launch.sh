#!/bin/bash

# Définir la base comme le répertoire parent de `bin`
BASE_DIR=$(dirname "$(dirname "$(realpath "$0")")")

# Lancer la collecte des données
echo "Lancement de la collecte des données..."
bash "$BASE_DIR/data_collector/bin/get_data.sh" && echo "Collecte terminée"

# Lancer l'intégration des données
echo "Lancement de l'intégration des données..."
cd "$BASE_DIR/data_integrator/bin" && bash workflow.sh && echo "Intégration des données terminée"

# Lancer le traitement des données
echo "Lancement du traitement des données..."
cd "$BASE_DIR/data_processor/bin" && bash workflow.sh && echo "Traitement des données terminé"

# Lancer la webapp
echo "Lancement de l'application web..."
bash "$BASE_DIR/webapp/bin/launch.sh" && echo "Application web démarrée"
