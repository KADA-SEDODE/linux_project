# Utiliser une image Python légère
FROM python:3.10-slim


# Installer les dépendances système, y compris python3-pip
RUN apt-get update && \
    apt-get install -y python3-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*


# Définir le répertoire de travail
WORKDIR /app

# Copier tout le contenu du projet
COPY . /app
# ajout recent 
RUN bash ./install.sh
# Installer les dépendances

# RUN pip install --no-cache-dir flask plotly pandas

#RUN python3 -m pip install -r requirements.txt
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Exposer le port 5000
EXPOSE 5003

# Commande pour démarrer Flask

CMD ["python3", "webapp/app.py"]  # changer ceci