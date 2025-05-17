from flask import Flask, request, render_template
import pysolr

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
def search():
    query = request.form.get("query", "")  # Suchanfrage aus dem Formular
    results = []
    if not query:
        query = "*:*"  # Alle Dokumente zurückgeben

    if query:
        params = {
            "qf": "title^5 author_names^3 summaries^2 fulltext subjects", # Gewichtung der Felder, die durchsucht werden
            "defType": "edismax", # erweiterte DisMax-Suche            
            "fl": "*,score", # Felder, die zurückgegeben werden
            "debugQuery": "true"
        }

        solr_results = solr.search(query, **params)
        explanations = solr_results.raw_response.get('debug', {}).get('explain', {})
        
        for solr_result in solr_results.docs:
            result = solr_result
            result['explanation'] = explanations.get(result['id'], "Keine Erklärung verfügbar.")
            results.append(result)

    return render_template("index.html", query=query, results=results, num_of_hits=solr_results.hits)

if __name__ == "__main__":
    app.run(debug=True)