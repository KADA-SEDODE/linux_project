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

# Exécuter le script d'installation
RUN bash ./install.sh

# Installer les dépendances Python
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Exposer le port 5003
EXPOSE 5003

# Commande pour démarrer Flask
CMD ["sh", "-c", "python3 webapp/app.py"]