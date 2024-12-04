import os
import pandas as pd


def create_indicators():
    print("Début de la création des indicateurs...")

    # Obtenir le chemin de la racine du projet
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # Construire les chemins absolus
    raw_file_path = os.path.join(base_path, "data", "raw", "raw_data.csv")
    staged_file_path = os.path.join(base_path, "archived", "staged_data.csv")

    print(f"Chemin du fichier brut : {raw_file_path}")
    print(f"Chemin du fichier transformé : {staged_file_path}")

    # Vérifier si le fichier brut existe
    if not os.path.exists(raw_file_path):
        print(f"ERREUR : Le fichier {raw_file_path} n'existe pas.")
        return

    # Lecture des données brutes
    try:
        raw_data = pd.read_csv(raw_file_path, sep=None, engine="python")  # Auto-détection du séparateur
        print("Lecture des données brutes réussie. Aperçu :")
        print(raw_data.head())
    except Exception as e:
        print(f"ERREUR : Impossible de lire le fichier brut. Détails : {e}")
        return
    # Transformation des données
    try:
        # Nombre de déclarations par ville
        declarations_per_city = raw_data['ville'].value_counts().reset_index()
        declarations_per_city.columns = ['Ville', 'Nombre_declarations_ville']

        # Nombre de déclarations par type d'anomalie
        declarations_per_type = raw_data['type'].value_counts().reset_index()
        declarations_per_type.columns = ['Type d\'anomalie', 'Nombre_declarations_anomalie']

        # Nombre de déclarations par mois
        declarations_per_month = raw_data['mois_annee_decla'].value_counts().reset_index()
        declarations_per_month.columns = ['Mois', 'Nombre_declarations_mois']

        # Créer un DataFrame proprement
        staged_data = pd.concat(
            [declarations_per_city, declarations_per_type, declarations_per_month],
            axis=1
        )

        # Sauvegarde des données transformées
        os.makedirs(os.path.dirname(staged_file_path), exist_ok=True)
        staged_data.to_csv(staged_file_path, index=False)
        print(f"Données transformées enregistrées dans {staged_file_path}")

    except Exception as e:
        print(f"ERREUR : Échec de la transformation des données. Détails : {e}")

if __name__ == "__main__":
    create_indicators()



# import os
# import pandas as pd

# def create_indicators():
#     print("Début de la création des indicateurs...")

#     # Obtenir le chemin de la racine du projet
#     base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#     # Construire les chemins absolus
#     raw_file_path = os.path.join(base_path, "data", "raw", "raw_data.csv")
#     staged_file_path = os.path.join(base_path, "archived", "staged_data.csv")

#     print(f"Chemin du fichier brut : {raw_file_path}")
#     print(f"Chemin du fichier transformé : {staged_file_path}")

#     # Vérifier si le fichier brut existe
#     if not os.path.exists(raw_file_path):
#         print(f"ERREUR : Le fichier {raw_file_path} n'existe pas.")
#         return

#     # Lecture des données brutes
#     try:
#         raw_data = pd.read_csv(raw_file_path, sep=None, engine="python")  # Auto-détection du séparateur
#         print("Lecture des données brutes réussie. Aperçu :")
#         print(raw_data.head())
#     except Exception as e:
#         print(f"ERREUR : Impossible de lire le fichier brut. Détails : {e}")
#         return

#     # Transformation des données
#     try:
#         # Conversion des dates
#         raw_data['datedecl'] = pd.to_datetime(raw_data['datedecl'], errors='coerce')
#         raw_data = raw_data.dropna(subset=['datedecl'])

#         # Extraire le mois et l'année
#         raw_data['mois_annee_decla'] = raw_data['datedecl'].dt.to_period('M')

#         # Nombre de déclarations par ville
#         declarations_per_city = raw_data['ville'].value_counts().reset_index()
#         declarations_per_city.columns = ['Ville', 'Nombre_declarations_ville']

#         # Nombre de déclarations par type d'anomalie
#         declarations_per_type = raw_data['type'].value_counts().reset_index()
#         declarations_per_type.columns = ['Type_d_anomalie', 'Nombre_declarations_anomalie']

#         # Nombre de déclarations par mois
#         declarations_per_month = raw_data['mois_annee_decla'].value_counts().reset_index()
#         declarations_per_month.columns = ['Mois', 'Nombre_declarations_mois']

#         # Moyenne mensuelle des anomalies par type
#         anomalies_by_month_type = raw_data.groupby(['mois_annee_decla', 'type']).size().reset_index(name='Nombre_declarations')
#         monthly_avg_anomalies = anomalies_by_month_type.groupby('type')['Nombre_declarations'].mean().reset_index()
#         monthly_avg_anomalies.columns = ['Type_d_anomalie', 'Moyenne_mensuelle_declarations']

#         # Nombre de déclarations par jour de la semaine
#         raw_data['Jour_de_la_semaine'] = raw_data['datedecl'].dt.day_name()
#         declarations_by_day = raw_data['Jour_de_la_semaine'].value_counts().reset_index()
#         declarations_by_day.columns = ['Jour_de_la_semaine', 'Nombre_declarations']

#         # Créer un DataFrame proprement
#         staged_data = pd.concat(
#             [
#                 declarations_per_city,
#                 declarations_per_type,
#                 declarations_per_month,
#                 monthly_avg_anomalies,
#                 declarations_by_day
#             ],
#             axis=1
#         )

#         # Sauvegarde des données transformées
#         os.makedirs(os.path.dirname(staged_file_path), exist_ok=True)
#         staged_data.to_csv(staged_file_path, index=False)
#         print(f"Données transformées enregistrées dans {staged_file_path}")

#     except Exception as e:
#         print(f"ERREUR : Échec de la transformation des données. Détails : {e}")

# if __name__ == "__main__":
#     create_indicators()
