from flask import Flask, request, render_template
import pysolr

app = Flask(__name__)

solr_host = "localhost"
solr_port = "8983"
solr_core = "my1stcore"

solr_url = f"http://{solr_host}:{solr_port}/solr/{solr_core}"

solr = pysolr.Solr(solr_url)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def search():
    query = request.form.get("query", "")  # Suchanfrage aus dem Formular
    results = []
    if not query:
        query = "*:*"  # Alle Dokumente zurückgeben

    if query:
        params = {
            "qf": "title",
            #"qf": "title^3 authors^2 keywords^1",   # Gewichtung der Felder, die durchsucht werden
            "defType": "edismax",                   # Erweiterte DisMax-Suche
            "rows": 100,                            # maximale Anzahl der Suchergebnisse (pro Suchanfrage)
            "fl": "title, authors, publication_year, doi, abstract, score",    # Felder, die zurückgegeben werden
        }
        solr_results = solr.search(query, **params)

    return render_template("index.html", query=query, results=list(solr_results), num_of_hits=solr_results.hits)

if __name__ == "__main__":
    app.run(debug=True)