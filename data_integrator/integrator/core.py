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
        
        # **Nouvel indicateur : Nombre d'anomalies par mois et par type**
        anomalies_by_month_and_type = raw_data.groupby(['mois_annee_decla', 'type']) \
                                             .size() \
                                             .reset_index(name='Nombre_declarations')
        anomalies_by_month_and_type.columns = ['Mois', 'Type_d_anomalie', 'Nombre_declarations']


        # Créer un DataFrame proprement
        staged_data = pd.concat(
            [declarations_per_city, declarations_per_type, anomalies_by_month_and_type],
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