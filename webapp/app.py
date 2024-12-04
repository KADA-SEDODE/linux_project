import os 
from flask import Flask, render_template, send_from_directory, send_file

app = Flask(__name__)

# Route pour la page d'accueil
@app.route("/")
def home():
    return render_template("index.html")

# Route pour afficher le graphique des déclarations par ville
@app.route("/graph_ville")
def graph_ville():
    return send_from_directory("static", "graph_ville.html")

# Route pour afficher le graphique des déclarations par type d'anomalie
@app.route("/graph_type")
def graph_type():
    return send_from_directory("static", "graph_type.html")

# Route pour afficher le graphique des déclarations par mois
@app.route("/graph_mois")
def graph_mois():
    return send_from_directory("static", "graph_mois.html")

@app.route("/download")
def download():
    # Utilisez un chemin absolu pour plus de fiabilité
    file_path = os.path.join(os.path.dirname(__file__), "..", "archived", "staged_data.csv")
    print(f"Chemin absolu utilisé : {file_path}")
    try:
        # Vérifiez si le fichier existe
        if os.path.exists(file_path):
            return send_file(file_path, as_attachment=True)
        else:
            return "Erreur : Fichier introuvable", 404
    except Exception as e:
        return f"Erreur : {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)
    app.logger.setLevel('DEBUG')


