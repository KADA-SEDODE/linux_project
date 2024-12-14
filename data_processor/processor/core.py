import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def display_results():
    print("Début de l'affichage des résultats...")

    # Obtenir le chemin de la racine du projet
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    # Chemin du fichier transformé
    staged_file_path = os.path.join(base_path, "archived", "staged_data.csv")
    static_dir = os.path.join(base_path, "webapp", "static")

    print(f"Chemin du fichier transformé : {staged_file_path}")

    # Lecture des données
    try:
        data = pd.read_csv(staged_file_path, sep=",")
        print("Lecture des données réussie. Aperçu :")
        print(data.head())
    except FileNotFoundError:
        print(f"ERREUR : Le fichier transformé est introuvable à {staged_file_path}.")
        return
    except Exception as e:
        print(f"ERREUR : Impossible de lire le fichier transformé. Détails : {e}")
        return

    # Créer le dossier webapp/static s'il n'existe pas
    os.makedirs(static_dir, exist_ok=True)

    # Graphiques interactifs
    
     # Graphique des déclarations par ville
    if 'Ville' in data.columns and 'Nombre_declarations_ville' in data.columns:
        print("Affichage des déclarations par ville...")
        ville_data = data[['Ville', 'Nombre_declarations_ville']].dropna()
        fig_ville = px.bar(
            ville_data,
            x="Ville",
            y="Nombre_declarations_ville",
            title="Nombre de déclarations par ville",
            labels={'Nombre_declarations_ville': 'Nombre de déclarations', 'Ville': 'Ville'},
            template="plotly_white"
        )
        fig_ville.update_traces(marker_line_color='rgb(0,0,0)', marker_line_width=1.5)
        fig_ville.write_html(os.path.join(static_dir, "graph_ville.html"))

    # Graphique des déclarations par type d'anomalie
    if 'Type d\'anomalie' in data.columns and 'Nombre_declarations_anomalie' in data.columns:
        print("Affichage des déclarations par type d'anomalie...")
        type_data = data[['Type d\'anomalie', 'Nombre_declarations_anomalie']].dropna()
        fig_type = px.bar(
            type_data,
            x="Type d'anomalie",
            y="Nombre_declarations_anomalie",
            title="Nombre de déclarations par type d'anomalie",
            labels={'Nombre_declarations_anomalie': 'Nombre de déclarations', 'Type d\'anomalie': 'Type d\'anomalie'},
            template="plotly_white"
        )
        fig_type.update_traces(marker_line_color='rgb(0,0,0)', marker_line_width=1.5)
        fig_type.write_html(os.path.join(static_dir, "graph_type.html"))
    
     # Graphique des anomalies par mois et par type
    if 'Mois' in data.columns and 'Type_d_anomalie' in data.columns and 'Nombre_declarations' in data.columns:
        print("Affichage des anomalies par mois et par type...")
        anomalies_data = data[['Mois', 'Type_d_anomalie', 'Nombre_declarations']].dropna()
        fig_anomalies = px.bar(
            anomalies_data,
            x="Mois",
            y="Nombre_declarations",
            color="Type_d_anomalie",
            title="Anomalies par mois et par type",
            labels={'Nombre_declarations': 'Nombre d\'anomalies', 'Mois': 'Mois', 'Type_d_anomalie': 'Type d\'anomalie'},
            template="plotly_white"
        )
        fig_anomalies.update_traces(marker_line_width=1.5)
        fig_anomalies.write_html(os.path.join(static_dir, "graph_mois.html"))

    print("Les graphiques interactifs ont été sauvegardés dans le dossier 'webapp/static'.")


if __name__ == "__main__":
    display_results()