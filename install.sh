# #!/bin/bash
# mkdir -p log archived/raw archived/staged
# pip install -r requirements.txt

# #!/bin/bash
# echo "Installation des dépendances..."
# pip install -r requirements.txt
#!/bin/bash
echo "Installation des dépendances..."
if ! pip install -r requirements.txt; then
    echo "Erreur : Échec de l'installation des dépendances"
    exit 1
fi
