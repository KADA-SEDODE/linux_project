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

RUN python3 -m pip install -r requirements.txt

# Exposer le port 5000
EXPOSE 5000

# Commande pour démarrer Flask

# CMD ["python", "webapp/app.py"]  # changer ceci

# par 

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "webapp.app:app"]
