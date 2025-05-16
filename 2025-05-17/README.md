# Praxisteil am 17.5.2025

## Scoring auf Basis der Kosinus-Ähnlichkeit und Jaccard-Ähnlichkeit

Die Grundlagen der Jaccard-Ähnlichkeit und der Kosinus-Ähnlichkeit wurden in Vorlesung vermittelt. 

Wir wollen uns nun den Unterschied zwischen Jaccard-Ähnlichkeit und Kosinus-Ähnlichkeit in einem konkreten Beispiel genauer ansehen.

Um das Programm `01_cosine-similarity-binary-weights.py` ausführen zu können, muss das Paket **scikit-learn** installiert werden

```sh
pip install scikit-learn
```

Aus dem scikit-learn Paket verwenden wir die Funktion für die Berechnung der Kosinus-Ähnlichkeit, so dass wir die Berechnung nicht selbst implementieren müssen.

Das Programm umfasst eine Beispielkollektion von 5 Dokumenten. Das Term Dictionary besteht aus 20 Termen.

Wir betrachten eine binäre Termgewichtung, d.h. in der Term-Dokument-Matrix steht im Eintrag _i,j_ (in der _i_-ten Zeile und _j_-ten Spalte) genau dann eine 1, wenn im _i_-ten Dokument der _j_-te Term existiert; andernfalls eine 0.

Die binäre Term-Dokument-Matrix mit 5 Zeilen und 20 Spalten hat für die 5 Dokumente folgende Struktur:

```
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 1 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
```

Wir betrachten eine Suchanfrage, die 3 Anfrageterme besitzt, die im Term Dictionary existieren. Der Termvektor der Suchanfrage hat daher folgende Struktur (hier als Zeilen- und nicht als Spaltenvektor notiert):

```
[1 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0]
```

Das Programm berechnet für die 5 Dokumente und die Suchanfrage das Top-5-Ranking auf Basis der Jaccard- als auch der Kosinusähnlichkeit.

Für die 5 Dokumente ergeben sich folgende Score-Werte:

```
Dokument | Jaccard-Ähnlichkeit | Kosinus-Ähnlichkeit
---------|---------------------|---------------------
   d1    |  0.15               |  0.39
   d2    |  0.33               |  0.52
   d3    |  0.33               |  0.58
   d4    |  0.00               |  0.00
   d5    |  0.20               |  0.33
```

Nach der Berechnung aller Score-Werte können die Dokumente absteigend nach ihrem Score-Wert sortiert werden. Dokumente mit dem Score-Wert 0 bleiben im Ranking unberücksichtigt.

Die sortierte Rangfolge der Dokumente wird als Top-_k_-Ranking bezeichnet. In diesem Beispiel ist _k_=5, so dass vom Programm als Ergebnis der Suchanfrageverarbeitung ein Top-5-Ranking ausgegeben wird. Dieses Ranking besteht aus bis zu 5 Dokumenten (falls tatsächlich alle 5 Dokumente echt positive Score-Werte besitzen).

Das Programm gibt die ermittelten Top-5-Rankings aus:

```
Top-5-Ranking nach Jaccard-Ähnlichkeit:
 [2 3 5 1]

Top-5-Ranking nach Kosinusähnlichkeit:
 [3 2 1 5]
 ```

 In beiden Varianten erhält das Dokument d4 den Score-Wert 0, so dass es nicht im Top-5-Ranking enthalten ist.

 Wie sind die Unterschiede in den beiden Rankings zu bewerten?