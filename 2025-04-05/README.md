# Ausführung von Apache Solr in einem Docker Container

## Installation der erforderlichen Infrastruktur

Es wird vorausgesetzt, dass auf Ihrem Rechner / Laptop ein Docker Daemon läuft. Wir nutzen in der Vorlesung zur Vereinfachung der Installation die Software **Docker Desktop**. 

Für Docker Desktop stehen Installationsdateien für alle gängigen Betriebssysteme zur Verfügung:

* Docker Desktop für **Windows** (10 und 11) unter https://docs.docker.com/desktop/setup/install/windows-install/
* Docker Desktop für **MacOS** unter https://docs.docker.com/desktop/setup/install/mac-install/
* Docker Desktop für **Linux** unter https://docs.docker.com/desktop/setup/install/linux/

Bitte stellen Sie sicher, dass Sie eine aktuelle Version (4.36.0 oder höher) von Docker Desktop installieren.

Wir benötigen zudem die Software **Docker Compose**. Docker Compose ist in der aktuellen Version von Docker Desktop bereits enthalten, so dass keine zusätzliche Installation erforderlich ist.

Nach der Installation von Docker Desktop können Sie testweise einen Container starten, der `Hello from Docker!` auf der Kommandozeile ausgibt. Starten Sie dazu ein Terminal / die Kommandozeile und geben Sie anschließend folgenden Befehl ein:

```sh
docker run hello-world
```

Die erfolgreiche Ausführung des Befehls sollte folgende Ausgabe ergeben (die Ausgabe kann je nach Host-Betriebssytem leicht variieren):

```
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
c9c5fd25a1bd: Pull complete
Digest: sha256:7e1a4e2d11e2ac7a8c3f768d4166c2defeb09d2a750b010412b6ea13de1efb19
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (arm64v8)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

### Kurze Erklärung der ausgeführten Aktionen

Docker ist eine Plattform zur Container-Virtualisierung, die es ermöglicht, Anwendungen samt ihrer Abhängigkeiten in einer isolierten Umgebung – einem sogenannten **Container** – auszuführen. Im Gegensatz zu klassischen virtuellen Maschinen (VMs) sind Container leichtgewichtiger.

Wir werden Docker verwenden, um einen Solr-Server in einem Docker Container auszuführen. Der Docker Container stellt hierbei sicher, dass alle für die Ausführung des Solr-Servers erforderlichen Komponenten (z.B. Java) zur Verfügung stehen. Für Sie wird dadurch der Installationsaufwand deutlich reduziert.

Ein **Docker-Image** ist eine Art Vorlage oder Bauplan für einen Docker-Container. Es enthält alle benötigten Dateien, Programme und Programmbibliotheken sowie Konfigurationen, um eine gewünschte Anwendung ausführen zu können. Ein Container ist eine laufende Instanz eines Images, vergleichbar mit einem Programm, das aus einer ausführbaren Datei gestartet wird.

Normalerweise müsste Solr manuell installiert, konfiguriert und mit den richtigen Abhängigkeiten versehen werden. Mit Docker genügt ein einzelner Befehl, um Solr in einer standardisierten Umgebung zu starten – unabhängig vom Betriebssystem des Hosts. Das macht die Nutzung für alle Studierenden einheitlich und vermeidet typische Installationsprobleme.

Nun erklären wir kurz, was nach der Eingabe des Befehls `docker run hello-world` passiert ist. Zunächst überprüft Docker, ob das benötigte Docker Image mit dem Namen `hello-world` bereits auf dem Rechner vorhanden ist. Ist das nicht der Fall, so wird das Docker Image automatisch aus **Docker Hub** heruntergeladen. Docker Hub ist ein öffentliches Repository für Container-Images. Aus Sicherheitsgründen sollten Sie darauf achten, nur vertrauenswürdige Docker Images aus dem Docker Hub herunterzuladen. Vertrauenswürdige Images erkennen Sie z.B. an dem Zusatz _Docker Official Image_.

Nachdem das Docker Image heruntergeladen wurde, startet Docker anschließend einen Container, d.h. eine isolierte Umgebung, in der das Image ausgeführt wird.

Das Docker Image `hello-world` enthält ein kleines Programm, das lediglich eine Begrüßungsnachricht ausgibt. Sobald der Container gestartet ist, führt er dieses Programm aus und zeigt die Meldung `Hello from Docker!` an. Damit bestätigt Docker, dass die Installation erfolgreich ist und korrekt funktioniert. Nachdem die Nachricht ausgegeben wurde, beendet sich der Container automatisch, da er seine Aufgabe erfüllt hat.

## Installation von Solr in einem Docker Container

Wir wechseln in das Unterverzeichnis `solr` und führen folgenden Befehl aus, um einen Docker Container mit dem Namen `solr-server` zu erzeugen, in dem schließlich ein Solr Server gestartet wird:

```sh
cd solr
docker compose up -d
```

Der `docker compose` Befehl liest die Datei `docker-compose.yml` ein. In dieser Datei sind die Dienste (Services) definiert, die beim Start (`up`) in einzelnen Docker Containern gestartet werden. In unserem Fall steht in der Datei nur ein Service mit dem Namen `solr`. Dazu wird zuerst das offizielle Docker Image `solr:9.8.1` aus dem Docker Hub heruntergeladen. Anschließend wird ein Docker Container mit dem Namen `solr-server` erzeugt, in dem schließlich ein Solr-Server gestartet wird. Die Option `-d` im obigen Befehl führt dazu, dass der Container im Hintergrund ausgeführt wird und nach der Beendigung des Befehls weiterhin ausgeführt wird. 

Damit haben wir unser Ziel erreicht.

Nachdem die Befehlsausführung beendet wurde, sollten Sie folgende Meldung sehen:

```sh
 ✔ Container solr-server  Started  
 ```

Anschließend können Sie auf ihrem Rechner die Web-Admin-Oberfläche des Solr-Servers im Browser unter der URL

```
http://localhost:8983
```

aufrufen. Schauen Sie sich in der Admin-Oberfläche etwas um. Wir werden im Praxistag intensiv mit der Oberfläche arbeiten.

## Basisbefehle für das Arbeiten mit dem Docker Container

Nun möchte ich Ihnen noch einige Befehle vorstellen, die Sie für die Verwaltung des Docker Containers nutzen können.

Zum **Stoppen** des Docker Containers `solr-server` können Sie folgenden Befehl verwenden:

```sh
docker stop solr-server
```

Anschließend lässt sich der Container wieder hochfahren mittels:

```sh
docker start solr-server
```

Um zu prüfen, ob der Container `solr-server` bereits ausgeführt wird, kann folgender Befehl genutzt werden:

```sh
docker ps -f "name=solr-server"
```

Wenn der Container nicht ausgeführt wird, so kann folgender Befehl genutzt werden (um zu prüfen, ob der Container gestoppt wurde):

```sh
docker ps -a -f "name=solr-server"
```

Nach der Änderung von Konfigurationsdateien im Solr-Server muss der Solr-Server ggf. neu gestartet werden. Dies kann in einem Befehl erreicht werden:

```sh
docker restart solr-server
```

Der Docker Container `solr-server` kann entfernt werden mittels

```sh
docker compose down
```

Das lokale Verzeichnis `solr/solrdata` wird beim Entfernen des Docker Containers **nicht** entfernt, da es als Bind Mount eingebunden ist (siehe unten).

Ein neuer Docker Container kann erzeugt werden mittels

```sh
docker compose up -d
```

## Bind Mounts

Docker-Container sind isolierte Umgebungen, und standardmäßig gehen alle darin gespeicherten Daten verloren, sobald der Container gelöscht wird. Um Daten persistent zu speichern, nutzt man **Docker Volumes** oder **Bind Mounts** (Volumes eher für Produktivszenarien; Bind Mounts für lokale Entwicklungsumgebungen).

Ein **Bind Mount** ermöglicht es, ein Verzeichnis oder eine Datei vom Docker Host direkt in einen Docker-Container einzubinden. Anders als **Docker Volumes**, die von Docker verwaltet werden, nutzt ein Bind Mount einen festen Pfad im Dateisystem des Docker Host. Alle Änderungen in diesem Verzeichnis wirken sich sowohl im Docker Container als auch auf dem Docker Host aus. Ein Bind Mount ist praktisch für die lokale Entwicklung, da Änderungen an Dateien (Quellcode, Konfigurationsdateien), die auf dem Docker Host erfolgen, sofort im Container verfügbar sind. Ferner erlaubt ein Bind Mount den Zugriff auf Konfigurationsdateien oder Protokolldatein (Log-Files) von Diensten, die im Docker Container ausgeführt wird, außerhalb des Containers.

In der Datei `docker-compose.yml` ist ein Bind Mount definiert:


```yml
    volumes:
      - ./solrdata:/var/solr
```

Dadurch wird das Verzeichnis `solrdata` (innerhalb des Verzeichnisses, in dem die Datei `docker-compose.yml` gespeichert ist) des Docker Host mit dem Verzeichnis `/var/solr` im Docker Container verbunden. Alle Änderungen, die innerhalb dieses Verzeichnisses (auch in Unterverzeichnissen) ausgeführt werden, sind im Docker Host und Container sichtbar. Werden z.B. vom Solr-Server (der im Container ausgeführt wird) Dateien in diesem Verzeichnis gespeichert, so können Sie im Docker Host ebenfalls auf diese Dateien zugreifen.

Im Unterverzeichnis `solrdata/logs` werden die Protkolldateien (Log-Files) des Solr-Servers gespeichert. Die wichtigste Logdatei eines Solr-Servers heißt `solr.log`. Falls unerwartete Probleme beim Betrieb eines Solr-Servers bzw. bei Indexierung oder Suche auftreten, kann man dort nach möglichen Fehlerursachen suchen. 

Die Logdatei wird automatisch rotiert (`solr.log.1` usw.).

Die Logausgabe des Solr-Servers kann auch mit folgenden Befehl (ausgeführt auf dem Docker Host) fortlaufend ausgegeben werden:

```sh
docker logs -f solr-server
```

Alternativ kann die Datei `solrdata/logs/solr.log` im Dateisystem des Docker Hosts aufgerufen werden, um die Lognachrichten des Solr-Servers einzusehen.
