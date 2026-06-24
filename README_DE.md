Lese auf: [English](README.md) | [Deutsch](README_DE.md)
# ecommerce-database-design

Ein standardmäßiges Backend-Datenbankdesign, das einen Online-Marktplatz für Elektronikartikel von verschiedenen Händlern simuliert.

Die aktuelle Version funktioniert wie geplant. Ich werde im Laufe der Zeit weitere geschäftsrelevante SQL-Abfragen zu den Dateien queries.md und Data_Theory.md hinzufügen,
um meine Fähigkeiten mit SQLite weiter auszubauen und zu testen.
Während die Benutzertabellen mit 1.000 eindeutigen Datensätzen gefüllt sind, sind die nachgelagerten relationalen Ebenen (wie Produkte und Bestellungen) kleiner skaliert.
Dadurch ist es gar nicht so einfach, riesige Tabellen-Joins direkt sauber auszubalancieren.
Die Produkttabelle basiert derzeit auf einer programmatischen Schleife, die aus einer kleinen Auswahl an Platzhalter-Namen und Farben besteht.
Ich suche aktuell nach einer eleganteren Lösung, um automatisch eine größere Auswahl an einzigartigen Produktmodellen zu generieren.
