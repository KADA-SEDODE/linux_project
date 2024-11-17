#!/bin/bash
source ../conf/collector.conf  # charge le fichier collector.conf situé dans le dossier ../conf.

# echo "Form ID is set as: ${form_id}"  est inutile
echo "Target path is set as: ${target_path}"

python collect_data.py
