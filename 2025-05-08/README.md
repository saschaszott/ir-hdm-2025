# Praxisteil vom 8.5.2025 – Ranked Retrieval 

## Scoring auf Basis der Jaccard-Ähnlichkeit

Hierbei werden Dokumente und Suchanfrage als Mengen von Termen aufgefasst. Die Häufigkeit von Termen bleibt unbeachtet, ebenso die Reihenfolge des Auftretens bestimmter Termfolgen innerhalb von Dokumenten und Suchanfrage.

Die Jaccard-Ähnlichkeit zwischen einem Dokument _d_ und der Suchanfrage _q_ wird definiert als Quotient der Größe der Schnittmenge der Termmengen von _d_ und _q_ und der Größe der Vereinigungsmenge der Termmengen von _d_ und _q_.

Für die Ermittlung des Top-k-Rankings werden schließlich nur solche Dokumente betrachtet, die bezüglich der vorgegebenen Suchanfrage eine Jaccard-Ähnlichkeit größer 0 besitzen. Die übrig bleibenden Dokumente werden schließlich absteigend nach der zugehörigen Jaccard-Ähnlichkeit sortiert. Die Suchausgabe enthält maximal _k_ Dokumente.

Ausführung des Demonstrators:

```sh
python 01_jaccard-similarity.py
```

Das Programm nutzt eine definierte Menge von 5 Dokumenten _d1_ bis _d5_. Die Termmengen dieser Dokumente sind innerhalb des Programms definiert. Beim Start des Programms werdend die 5 Termmengen ausgegeben.

Beispielsitzung:

```
d1: {'system', 'information', 'retrieval'}
d2: {'science', 'information', 'search'}
d3: {'database', 'retrieval', 'data'}
d4: {'ranking', 'vector', 'retrieval', 'space'}
d5: {'sql', 'data', 'database'}
Geben Sie Ihre Suchanfrage ein: information retrieval
Top-10-Ranking der Dokumente bezüglich ihrer Jaccard-Ähnlichkeit:
d1 (J-K = 0.667)
d2 (J-K = 0.250)
d3 (J-K = 0.250)
d4 (J-K = 0.200)
```

