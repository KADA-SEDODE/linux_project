#!/bin/bash

# Obtenir le chemin absolu du dossier contenant workflow.sh
BASE_DIR=$(dirname "$(realpath "$0")")

# Appeler core.py avec le chemin absolu
python3 "$BASE_DIR/../integrator/core.py"


# En résumé, ce script est une manière simple de lancer core.py sans taper toute la commande Python.