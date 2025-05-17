from flask import Flask, request, render_template
import pysolr
import math
app = Flask(__name__)

solr_host = "localhost"
solr_port = "8983"
solr_core = "gutenberg"

solr_url = f"http://{solr_host}:{solr_port}/solr/{solr_core}"

solr = pysolr.Solr(solr_url)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/", methods=["POST"])
@app.route("/search", methods=["GET"])
def search():
    query = request.form.get("query", "")  # Suchanfrage aus dem Formular
    page = int(request.args.get("page", 1)) # Page-Nummer aus den URL-Parametern
    results = []
    if not query:
        query = "*:*"  # Alle Dokumente zurückgeben

    if query:
        params = {
            "qf": "title^5 author_names^3 summaries^2 fulltext subjects", # Gewichtung der Felder, die durchsucht werden
            "defType": "edismax", # erweiterte DisMax-Suche            
            "fl": "*,score", # Felder, die zurückgegeben werden
            "debugQuery": "true",
            "bf": "log(download_count)^2",
            "start": (page - 1) * 10, # Start-Offset für die Paginierung
        }

        solr_results = solr.search(query, **params)
        explanations = solr_results.raw_response.get('debug', {}).get('explain', {})
        total_pages = math.ceil(solr_results.hits / 10)
        
        for solr_result in solr_results.docs:
            result = solr_result
            result['explanation'] = explanations.get(result['id'], "Keine Erklärung verfügbar.")
            results.append(result)

    return render_template("index.html", query=query, results=results, num_of_hits=solr_results.hits, page=page, total_pages=total_pages, explanations=explanations)

if __name__ == "__main__":
    app.run(debug=True)