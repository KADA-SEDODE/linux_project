# import pandas as pd

# def create_indicators():
#     raw_file_path = "/mnt/c/Users/kadas/Desktop/projet_linux/raw_data.csv"
#     staged_file_path = "/mnt/c/Users/kadas/Desktop/projet_linux/archived/staged_data.csv"

#     raw_data = pd.read_csv(raw_file_path)
#     print("Lecture des données brutes réussie.")

#     # Transformation des données
#     indicators = {
#         "Ville": raw_data['ville'].value_counts(),
#         "Type d'anomalie": raw_data['type'].value_counts(),
#         "Mois": raw_data['mois_annee_decla'].value_counts().sort_index()
#     }

#     pd.DataFrame(indicators).to_csv(staged_file_path, index=False)
#     print(f"Données transformées et enregistrées dans {staged_file_path}")


import os
import pandas as pd

def create_indicators():
    print("Début de la création des indicateurs...")
    
    # Ajustez les chemins des fichiers si nécessaire
    raw_file_path = "/mnt/c/Users/kadas/Desktop/projet_linux/raw_data.csv"
    staged_file_path = "/mnt/c/Users/kadas/Desktop/projet_linux/archived/staged_data.csv"

    print(f"Chemin du fichier brut : {raw_file_path}")
    print(f"Chemin du fichier transformé : {staged_file_path}")

    # Lecture des données
    if not os.path.exists(raw_file_path):
        print("ERREUR : Le fichier raw_data.csv n'existe pas.")
        return

    raw_data = pd.read_csv(raw_file_path)
    print("Lecture des données brutes réussie. Aperçu :")
    print(raw_data.head())

    # Transformation des données
    print("Transformation des données en cours...")
    indicators = {
        "Ville": raw_data['ville'].value_counts(),
        "Type d'anomalie": raw_data['type'].value_counts(),
        "Mois": raw_data['mois_annee_decla'].value_counts().sort_index()
    }

    print("Indicateurs générés. Aperçu :")
    for key, value in indicators.items():
        print(f"{key} :")
        print(value)

    # Sauvegarde des données transformées
    print("Sauvegarde des données transformées...")
    pd.DataFrame(indicators).to_csv(staged_file_path, index=False)
    print(f"Données transformées enregistrées dans {staged_file_path}")

if __name__ == "__main__":
    create_indicators()
