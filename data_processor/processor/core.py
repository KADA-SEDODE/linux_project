import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def display_results():
    print("Début de l'affichage des résultats...")
    os.makedirs("output", exist_ok=True)

    # Définir le chemin du fichier transformé
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    staged_file_path = os.path.join(base_path, "archived", "staged_data.csv")
    
    print(f"Chemin du fichier transformé : {staged_file_path}")

    # Lecture des données
    try:
        data = pd.read_csv(staged_file_path, sep=";")
        print("Lecture des données réussie. Aperçu :")
        print(data.head())
    except Exception as e:
        print(f"ERREUR : Impossible de lire le fichier transformé. Détails : {e}")
        return

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
        fig_ville.write_html("output/graph_ville.html")
        # fig_ville.write_html("webapp/static/graph_ville.html")

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
        fig_type.write_html("output/graph_type.html")
        # fig_type.write_html("webapp/static/graph_type.html")

    # Graphique des déclarations par mois
    if 'Mois' in data.columns and 'Nombre_declarations_mois' in data.columns:
        print("Affichage des déclarations par mois...")
        mois_data = data[['Mois', 'Nombre_declarations_mois']].dropna()
        fig_mois = go.Figure()
        fig_mois.add_trace(go.Scatter(
            x=mois_data['Mois'],
            y=mois_data['Nombre_declarations_mois'],
            mode='lines+markers',
            marker=dict(size=8, color='rgb(0,128,0)'),
            line=dict(width=2, color='rgb(0,128,0)')
        ))
        fig_mois.update_layout(
            title="Nombre de déclarations par mois",
            xaxis_title="Mois",
            yaxis_title="Nombre de déclarations",
            template="plotly_white"
        )
        fig_mois.write_html("output/graph_mois.html")
        # fig_mois.write_html("webapp/static/graph_mois.html")

    print("Les graphiques interactifs ont été sauvegardés dans le dossier 'output'.")

if __name__ == "__main__":
    display_results()
