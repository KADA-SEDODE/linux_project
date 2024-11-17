#!/bin/bash

# Exécution de tout le pipeline en arrière-plan
(cd . ; bash launch.sh >> ../log/data_pipeline.log) &
(cd ../webapp/bin; bash launch.sh >> ../../log/webapp.log )
