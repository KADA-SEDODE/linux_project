Le but du projet :
Exemple : "Ce projet vise à collecter, transformer et visualiser des données Open Data."


Instructions pour exécuter le projet :

Installation avec Docker :
bash

docker build -t projet_linux .
docker run -p 5000:5000 projet_linux

Installation locale :
bash

bash install.sh
bash bin/run.sh