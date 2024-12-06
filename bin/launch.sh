#!/bin/bash

# Lancer la collecte des données
echo "Lancement de la collecte des données..."
bash /mnt/c/Users/kadas/Desktop/projet_linux/data_collector/bin/run.sh \
  && echo "Collecte terminée"

# Lancer l'intégration des données
echo "Lancement de l'intégration des données..."
bash /mnt/c/Users/kadas/Desktop/projet_linux/data_integrator/bin/workflow.sh \
  && echo "Intégration des données terminée"

# Lancer le traitement des données
echo "Lancement du traitement des données..."
bash /mnt/c/Users/kadas/Desktop/projet_linux/data_processor/bin/workflow.sh \
  && echo "Traitement des données terminé"

# Lancer la webapp
echo "Lancement de l'application web..."
bash /mnt/c/Users/kadas/Desktop/projet_linux/webapp/bin/launch.sh \
  && echo "Application web démarrée"
