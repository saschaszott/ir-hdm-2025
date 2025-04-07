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

Auf der GitHub-Website können wir uns den Zustand der Datei nach der Änderung ansehen (https://github.com/saschaszott/ir-hdm-2025/blob/main/2025-04-10/git-update-workflow/current-datetime.py):

```py
from datetime import datetime

def main():
    now = datetime.now()
    print("Aktuelle Systemzeit:", now.strftime("%H:%M:%S"))
    print("Aktuelles Datum:", now.strftime("%Y-%m-%d")) # <-- neue Zeile hinzugefügt

if __name__ == "__main__":
    main()
```

Aufgrund der lokalen Änderung sowie der gleichzeitigen Änderung der Datei im GitHub-Repository haben wir einen **Konflikt** erzeugt.

## Aktualisierung des lokalen Arbeitsverzeichnisses

Um die Änderung des Dozenten aus dem GitHub-Repository zu übernehmen und in das lokale Arbeitsverzeichnis zu übernehmen, kann der Befehl 

```sh
git pull
```

verwendet werden.

Aufgrund des Konflikts erhalten wir folgende Ausgabe:

```
remote: Enumerating objects: 11, done.
remote: Counting objects: 100% (11/11), done.
remote: Compressing objects: 100% (4/4), done.
remote: Total 6 (delta 1), reused 6 (delta 1), pack-reused 0 (from 0)
Unpacking objects: 100% (6/6), 1.40 KiB | 204.00 KiB/s, done.
From https://github.com/saschaszott/ir-hdm-2025
   4b7ebd7..1e342ae  main       -> origin/main
Updating 4b7ebd7..1e342ae
error: Your local changes to the following files would be overwritten by merge:
	2025-04-10/git-update-workflow/current-datetime.py
Please commit your changes or stash them before you merge.
Aborting
```

Wenn git die entfernte Änderung des Dozenten übernehmen würde, dann wäre die lokal ausgeführte Änderung verloren. Daher wird in diesem Fall der Aktualisierungsvorgang abgebrochen (`Aborting`).

Um den Konflikt aufzulösen, kann die lokale Änderung in eine Zwischenablage (Git Stash) verschoben werden. Anschließend kann `git pull` (erfolgreich) aufgerufen werden, um die entfernte Änderung zu übernehmen und auf die lokale (unveränderte) Datei zu übernehmen. Nun kann die Änderung, die in der lokalen Zwischenablage "geparkt" wurde, auf die Datei `current-datetime.py` angewendet werden. 

Durch die folgende Befehlsfolge wird das Ziel erreicht:

```sh
git stash
git pull
git stash pop
```

Im Ergebnis hat die Datei `current-datetime.py` nun folgenden Zustand (beide Änderungen, sowohl die lokale als auch die entfernte Änderung des Dozenten sind in der Datei enthalten):

```py
from datetime import datetime

def main():
    now = datetime.now()
    # Ausgabe der aktuellen Systemzeit <-- neu eingefügte Zeile
    print("Aktuelle Systemzeit:", now.strftime("%H:%M:%S"))
    print("Aktuelles Datum:", now.strftime("%Y-%m-%d")) # <-- neue Zeile hinzugefügt

if __name__ == "__main__":
    main()
```


