#!/bin/bash
echo "Étape 1 : Collecte des données"
cd data_collector/bin && bash get_data.sh

echo "Étape 2 : Transformation des données"
cd ../../data_integrator/bin && bash workflow.sh

echo "Étape 3 : Restitution des résultats"
cd ../../data_processor/bin && bash workflow.sh

echo "Étape 4 : Lancement de l'application Flask"
cd ../../webapp && python app.py
