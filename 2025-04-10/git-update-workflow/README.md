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

Die lokale Änderung ist weiterhin über den Befehl `git status` ersichtlich, der folgende Ausgabe liefert:

```
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   current-datetime.py

no changes added to commit (use "git add" and/or "git commit -a")
```

## Gelingt `git stash pop` immer?

Es kann Fälle geben, in denen der obige Ansatz versagt. Nehmen wir an, dass auch der Dozent zwischen Zeile 4 und Zeile 5 einen Kommentar einfügt und die Änderung mit einem Commit übernimmt, so dass die Datei im entfernten GitHub-Repository des Dozenten folgende Struktur hat:

```py
from datetime import datetime

def main():
    now = datetime.now()
    # ein Kommentar, der vom Dozenten eingefügt wurde <-- weitere Änderung
    print("Aktuelle Systemzeit:", now.strftime("%H:%M:%S"))
    print("Aktuelles Datum:", now.strftime("%Y-%m-%d")) # <-- neue Zeile hinzugefügt

if __name__ == "__main__":
    main()
```

Wir wissen bereits, dass die Ausführung von `git pull` aufgrund der lokalen Änderung in der Datei `current-datetime.py` mit einem Fehler abbricht. Daher wenden wir erneut die Befehlskaskade `git stash` - `git pull` - `git stash pop` an.

Die ersten beiden Befehle werden erfolgreich ausgeführt.

Bei der Ausführung von `git stash pop` kommt es nun aber zu einer Fehlermeldung:

```
Auto-merging 2025-04-10/git-update-workflow/current-datetime.py
CONFLICT (content): Merge conflict in 2025-04-10/git-update-workflow/current-datetime.py
On branch main
Your branch is up to date with 'origin/main'.

Unmerged paths:
  (use "git restore --staged <file>..." to unstage)
  (use "git add <file>..." to mark resolution)
	both modified:   current-datetime.py

no changes added to commit (use "git add" and/or "git commit -a")
The stash entry is kept in case you need it again.
```

git kann in diesem Fall die beiden Änderungen in der Datei `current-datetime.py` nicht zusammenführen, da sie sich auf die gleiche Zeile beziehen. git vermerkt die nicht auflösbaren Konflikte direkt in der Datei:

```py
from datetime import datetime

def main():
    now = datetime.now()
<<<<<<< Updated upstream
    # ein Kommentar, der vom Dozenten eingefügt wurde <-- weitere Änderung
=======
    # Ausgabe der aktuellen Systemzeit <-- neu eingefügte Zeile
>>>>>>> Stashed changes
    print("Aktuelle Systemzeit:", now.strftime("%H:%M:%S"))
    print("Aktuelles Datum:", now.strftime("%Y-%m-%d")) # <-- neue Zeile hinzugefügt

if __name__ == "__main__":
    main()
```

Zuerst wird die Änderung des Dozenten im entfernten GitHub-Repository ausgegeben (im Bereich zwischen `<<<<<<< Updated upstream` und `=======`). Direkt darauffolgend wird die lokale Änderung ausgegeben (zwischen `=======` und `>>>>>>> Stashed changes`).

Der Konflikt muss nun von Ihnen manuell aufgelöst werden. Dazu entfernen Sie entweder den ersten Teil (mit der entfernten Änderung) oder alternativ den zweiten Teil (mit ihrer lokalen Änderung).

### Variante 1: Entscheidung für die Remote-Änderung des Dozenten

Um die entfernte Änderung des Dozenten in der Datei `current-datetime.py` zu übernehmen, entfernen Sie den Teil zwischen `=======` und `>>>>>>> Stashed changes` (z.B. in VS Code), so dass die Datei schließlich folgende Struktur aufweist:

```py
from datetime import datetime

def main():
    now = datetime.now()
    # ein Kommentar, der vom Dozenten eingefügt wurde <-- weitere Änderung
    print("Aktuelle Systemzeit:", now.strftime("%H:%M:%S"))
    print("Aktuelles Datum:", now.strftime("%Y-%m-%d")) # <-- neue Zeile hinzugefügt

if __name__ == "__main__":
    main()
```

Anschließend führen Sie die folgenden git Befehle aus:

```sh
git add current-date.py
git commit -m "Konflikt gelöst: Remote-Version des Dozenten behalten"
```

Die Ausgabe von `git status` zeigt keine Konflikte mehr an:

```
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```

In der Zwischenablage (Git Stash) ist die lokale Änderung allerdings immer noch vorhanden. Sie sollte daher noch entfernt werden, um später nicht mit anderen zwischengespeicherten Änderungen durcheinanderzukommen. Mit dem folgenden Befehl wird der oberste Stash-Eintrag entfernt:

```sh
git stash drop
```

Anschließend sollte der Stash leer sein, so dass der folgende Befehl ein leeres Ergebnis liefert:

```sh
git stash list
```

### Variante 2: Entscheidung für ihre lokale Änderung

Um ihre lokale Änderung in der Datei `current-datetime.py` zu übernehmen, entfernen Sie den Teil zwischen `<<<<<<< Updated upstream` und `=======` (z.B. in VS Code), so dass die Datei schließlich folgende Struktur aufweist:

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

