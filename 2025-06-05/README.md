# Praxisteil am 05.06.2025 – Facettierte Suche

## Aufnahme weitere Indexfelder

Zuerst sollen drei neue Indexfelder für die facettierte Suche zum Schema hinzugefügt werden: `author_names_ss`,
`bookshelves_ss` und `subjects_ss`. In den Feldnamen wird das Suffix `_ss` verwendet. Hierdurch wird das dynamische Indexfeld `*_ss` referenziert. Dieses ist in `managed-schema.xml` wie folgt definiert:

```xml
<dynamicField name="*_ss" type="strings" indexed="true" stored="true"/>
```

Der Indexfeldtyp `strings` ist in `managed-schema.xml` wie folgt definiert:

```xml
<fieldType name="strings" class="solr.StrField" sortMissingLast="true" multiValued="true"/>
```

Hierdurch wird der Feldinhalt keiner Tokenisierung unterworfen, sondern als ein Term (der ggf. aus mehreren Wörtern bestehen kann) ohne Veränderung in das Indexfeld übernommen. 

Ein dynamisches Indexfeld verwendet stets den Platzhalter (Wildcard) `*`. Wird in einem Solr-Dokument schließlich ein Indexfeld übergeben, dessen Name auf den Namen eines dynamischen Indexfelds passt (z.B. `author_names_ss` auf `*_ss`), so wird dem Indexfeld (z.B. `author_names_ss`) die Feldkonfiguration des dynamischen Felds zugewiesen. Diese ermöglicht die dynamische Erweiterung des Indexschemas ohne das explizite Anlegen von zusätzlichen Indexfeldern.

## Erweiterung der Webanwendung gutenberg-searcher um facettierte Suche

Wir wollen die Webanwendung `gutenberg-searcher` nun um eine facettierte Suche erweitern. 
Es soll eine facettierte Suche möglich sein nach:

* Autornamen (`author_names_ss`)
* Buchregalbezeichnung (`bookshelves_ss`)
* und Schlagwort (`subjects_ss`).

In einem ersten Schritt müssen wir den Solr-Request (in `app.py`) erweitern, so dass Solr angewiesen wird eine Facettierung des Suchergebnisses nach den o.g. Attributen (Indexfeldern) vorzunehmen.

Anschließend müssen wir das HTML-Template `index.html` um die Anzeige der drei Facetten erweitern. Die Facetten sollen als Spalte links neben dem Suchergebnis angezeigt werden.

Schließlich müssen wir die Anwendung (in `app.py`) erweitern, so dass nach der Auswahl eines Facettenwertes die ursprüngliche Suchanfrage mit einer zusätzlichen **Filter Query** erweitert wird. Die Suchanfrage wird dadurch mit einer zusätzlichen Bedingung verstehen (Konjunktion), wodurch die Anzahl der Suchtreffer verkleinert wird.

Im Template `index.html` sollen schließlich die ausgewählten Facettenwerte dargestellt werden.
