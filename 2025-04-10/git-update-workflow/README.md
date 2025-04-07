# Demo zum Git Update Workflow

## Ausgangszustand

Zuerst holen wir die Änderungen aus dem Remote Repository:

```sh
git pull
```

Wir finden nun im Verzeichnis `2025-04-10` das Unterverzeichnis `git-update-workflow`. In diesem Verzeichnis liegt ein Python-Script `current-datetime.py`, das die aktuelle Uhrzeit auf der Kommandozeile ausgibt.

## Ausführung einer lokalen Änderung

Wir werden nun die Datei `current-datetime.py` lokal ändern. Gleichzeitig wird der Dozent diese Datei im Remote-Repository (bei GitHub) ändern.
