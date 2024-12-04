Titre : Visualisation des Anomalies Urbaines avec Dans Ma Rue

1. Introduction
Ce projet vise à collecter, intégrer et visualiser des anomalies signalées dans l'espace public via l'application Dans Ma Rue de la ville de Paris. L'application permet de signaler des problèmes tels que la propreté, les graffitis, les encombrants ou encore les anomalies liées au mobilier urbain.

Les données couvrent une période de 13 mois glissants, allant de J-16 mois à J-3 mois. Ces données, fournies par l'API de la ville de Paris, sont utilisées pour créer des visualisations interactives et des rapports synthétiques accessibles via une application web.

2. Guide d'installation

-Clonez le projet depuis le dépôt GitHub :

git clone https://github.com/KADA-SEDODE/linux_project.git
cd linux_project

-Lancez le script d'installation pour configurer l'environnement (installation de dépendances et préparation de Docker) :
bash install.sh

Assurez-vous que Docker est installé et en cours d'exécution.

3. Guide d'exécution

-Démarrez l'application avec le script launch.sh 
bash bin/launch.sh

-Une fois le script exécuté, accédez à l'application web via l'URL suivante http://23.100.8.30:5003

4. Structure des fichiers

-data_collector/: Contient les scripts pour collecter les données via l'API de la ville de Paris.
-data_integrator/: Contient les scripts pour transformer les données collectées en un format exploitable.
-data_processor/: Contient les scripts pour analyser et enrichir les données.
-webapp/: Contient les fichiers relatifs à l'application web, notamment les fichiers HTML, CSS et les graphiques.
-bin/: Contient les scripts principaux pour automatiser l'exécution (launch.sh, install.sh).
-archived/: Stocke les fichiers de données transformées.
-log/: Contient les journaux d'exécution.

5. Prérequis

OS : Ubuntu 20.04 ou tout système Linux compatible avec Docker.
Python : 3.8.10 ou supérieur.
Dépendances principales : Flask, Pandas, Urllib3.
Docker : Pré-installé sur la machine.

6. Liens utiles
API utilisée : [Dans Ma Rue - Ville de Paris.](https://opendata.paris.fr/explore/dataset/dans-ma-rue/information/?disjunctive.type&disjunctive.soustype&disjunctive.code_postal&disjunctive.arrondissement&disjunctive.conseilquartier&disjunctive.prefixe&disjunctive.intervenant)

Documentation Flask : https://flask.palletsprojects.com/