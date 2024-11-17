# Utiliser une image Python légère
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le contenu du projet dans le conteneur
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir flask plotly pandas

# Exposer le port 5000
EXPOSE 5000

# Commande pour démarrer Flask
CMD ["python", "app.py"]
