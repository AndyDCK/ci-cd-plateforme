# Utilise une image officielle de Python comme base
FROM python:3.10-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier app.py et les éventuels fichiers de configuration requis (par exemple, requirements.txt)
COPY app.py /app/

# Si tu utilises un fichier requirements.txt, copie-le aussi
# COPY requirements.txt /app/

# Installer les dépendances nécessaires
RUN pip install --no-cache-dir prometheus_client

# Si tu utilises requirements.txt, installe aussi les dépendances du fichier
# RUN pip install --no-cache-dir -r requirements.txt

# Exposer le port sur lequel ton application va écouter
EXPOSE 8000

# Commande pour démarrer ton application Python
CMD ["python", "app.py"]
