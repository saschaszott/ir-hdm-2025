import requests
import json
from pathlib import Path

SOLR_CORE_NAME = "gutenberg"
SOLR_URL = f"http://localhost:8983/solr/{SOLR_CORE_NAME}"

def index_content():
    # alle JSON-Dateien mit Metadaten im Verzeichnis metadata
    # durchlaufen und Inhalt ausgewählter Metadatenfelder in
    # neu angelegte Indexfelder (mehrwertig) einfügen für facettierte Suche
    metadata_dir = Path("../2025-05-17/metadata")
    for file in metadata_dir.iterdir():
        if not file.is_file():
            continue
        if not file.name.endswith(".json"):
            continue
        with open(file, "r") as json_file:
            metadata = json.load(json_file)
            id = metadata.get("id")
            doc = {
                "id": id,
                "author_names_ss": {
                    "set": metadata.get("author_names")
                },
                "bookshelves_ss": {
                    "set": metadata.get("bookshelves")
                },
                "subjects_ss": {
                    "set": metadata.get("subjects")
                },
            }
            headers = { "Content-Type": "application/json" }
            resp = requests.post(f"{SOLR_URL}/update?commit=true", headers=headers, json=[doc])
            if resp.status_code == 200:
                print(f"Solr-Dokument mit ID {id} erfolgreich aktualisiert.")
            else:
                print(f"Fehler bei Solr-Update für Dokument mit ID {id}: {resp.text}")

if __name__ == "__main__":
    index_content()
