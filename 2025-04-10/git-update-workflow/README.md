# Demo zum Git Update Workflow

## Ausgangszustand

Zuerst holen wir die Änderungen aus dem Remote Repository:

```sh
git pull
```

Wir finden nun im Verzeichnis `2025-04-10` das Unterverzeichnis `git-update-workflow`. In diesem Verzeichnis liegt ein Python-Script `current-datetime.py`, das die aktuelle Uhrzeit auf der Kommandozeile ausgibt.

## Ausführung einer lokalen Änderung

Wir werden nun die Datei `current-datetime.py` lokal ändern. Dazu führen wir zwischen Zeile 4 und Zeile 5 einen Kommentar ein, so dass die Datei anschließend wie folgt aussieht:

```py
from datetime import datetime

def main():
    now = datetime.now()
    # Ausgabe der aktuellen Systemzeit <-- neu eingefügte Zeile
    print("Aktuelle Systemzeit:", now.strftime("%H:%M:%S"))

if __name__ == "__main__":
    main()
```

Wir können uns die lokal ausgeführten Änderungen mit dem folgenden Befehl auflisten lassen:

```sh
git status
```

In diesem Fall sollte bei Ihnen folgende Ausgabe erscheinen:

```
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   current-datetime.py

no changes added to commit (use "git add" and/or "git commit -a")
```

## Ausführung einer Änderung durch den Dozenten

Nun wird der Dozent die Datei `current-datetime.py` im Remote-Repository (bei GitHub) ändern.

Der Dozent fügt hierzu nach Zeile 5 eine neue Zeile in die Datei ein:

```py
print("Aktuelles Datum:", now.strftime("%Y-%m-%d"))
```

