# Utiliser une image Python légère
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier tout le contenu du projet
COPY . /app

# Installer les dépendances
RUN pip install --no-cache-dir flask plotly pandas

# Exposer le port 5000
EXPOSE 5000

# Commande pour démarrer Flask
CMD ["python", "webapp/app.py"]
