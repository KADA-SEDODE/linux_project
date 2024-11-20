# from flask import Flask, send_from_directory
# import os

# app = Flask(__name__)

# # Dossier contenant les graphiques
# OUTPUT_FOLDER = os.path.join(os.getcwd(), 'output')

# @app.route('/')
# def index():
#     return '''
#     <h1>Bienvenue sur l'application de visualisation</h1>
#     <ul>
#         <li><a href="/graph/graph_ville.html">Graphique des déclarations par ville</a></li>
#         <li><a href="/graph/graph_type.html">Graphique des déclarations par type d'anomalie</a></li>
#         <li><a href="/graph/graph_mois.html">Graphique des déclarations par mois</a></li>
#     </ul>
#     '''

# @app.route('/graph/<filename>')
# def show_graph(filename):
#     return send_from_directory(OUTPUT_FOLDER, filename)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)
# from flask import Flask, render_template, send_from_directory
# import os

# app = Flask(__name__)

# # Route pour la page d'accueil
# @app.route("/")
# def home():
#     return render_template("index.html")

# # Route pour les fichiers statiques (graphiques)
# @app.route("/graph/<path:filename>")
# def serve_graph(filename):
#     return send_from_directory("static", filename)

# if __name__ == "__main__":
#     # Lancer l'application Flask
#     app.run(debug=True, host="0.0.0.0", port=5000)

from flask import Flask, render_template, send_from_directory
from flask import send_file

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/graph/<filename>")
# def serve_graph(filename):
#     return send_from_directory("static", filename)

# if __name__ == "__main__":
#     app.run(debug=True)
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
    file_path = os.path.abspath("archived/staged_data.csv")
    try:
        # Vérifiez si le fichier existe
        if os.path.exists(file_path):
            return send_file(file_path, as_attachment=True)
        else:
            return "Erreur : Fichier introuvable", 404
    except Exception as e:
        return f"Erreur : {e}", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
