from flask import Flask, render_template
import pandas as pd
import plotly.express as px

app = Flask(__name__)

@app.route("/")
def home():
    data = pd.read_csv("../../staged_data.csv")
    fig = px.bar(data, x="Ville", y="Déclarations")
    graph = fig.to_html(full_html=False)

    return render_template("index.html", graph=graph)

if __name__ == "__main__":
    app.run(debug=True)
