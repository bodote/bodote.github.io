---
title: "TDD und Architektur?"
date: 2021-09-08
published: true
visible: true
categories:
  - Blog
tags:
  - Testing
  - TestFirst
  - Talk
toc: true
classes: wide
---

# Teil 2: Softwarearchitektur und TDD

## Ebenen der Softwarearchitektur im Vergleich

Zunächst ein Wort zu den verschiedenen Ebenen von Softwarearchitektur:
Wie beim Bauen von Gebäuden gibt es ja auch in der Software oder allgemein in der IT-System-Architektur verschiedenen Ebenen, die ich jetzt vollkommen willkürlich so definiere:

1. Ebene:

   - Bauwesen: Wie sieht mein Stadtteil aus in dem die Gebäude stehen, wie sind die Straßen, Gehwege, Parks und Gebäude insgesamt organisiert?
   - Softwarearchitektur: das ist Ebene auf der vor allem die Organisations- oder Standort übergreifenden IT-Strukturen (Hardware und Software) definiert und dokumentiert werden

2. Ebene:

   - Bauwesen: Wie schaut die Fassade aus, und wie ist die Aufteilung in den Gebäuden? z.B. Büros, große oder kleine Wohnungen
   - Softwarearchitektur: auf dieser Ebene werden IT-Struktur (Hardware und Software) innerhalb der Organisation definiert und dokumentiert.

3. Ebene:

   - Bauwesen: Wie ist die Raumaufteilung der Wohn-/Büro-Einheiten, wo sind Fenster und Türen,wie groß ist das Wohnzimmer im Vergleich zur Küche etc.
   - Softwarearchitektur: auf dieser Ebene wird grobe Stuktur einer Softwarelösung definiert und dokumentiert (hauptsächlich Software, in Sonderfällen auch Hardwarekomponenten) .

4. Ebene:

   - Bauwesen: welchen Bodenbelag hab ich wo, Welche Lichtschalter an der Wand , welche Türgriffe?
   - Softwarearchitektur: hier geht es um Module und Klassen und deren Interaktion (wenn wir von ObjectOrientierten Sprachen sprechen).

Wenn wir diese 4 Ebenen auf Softwarearchitektur übertragen und das auf TDD anwenden, dann hilft TDD eher bei den untern beiden Ebenen 3 und 4, also bei der Architektur der kleineren Details, weniger bei den obern beiden Ebenen 1 und 2, der Architektur im ganz Großen.

Die Ebenen 1 und 2 sind in der IT-Systemarchitektur (Hard- und Software) auch meist gar nicht das Problem. Denn hier ist zum einen meist recht gute Dokumentation vorhanden und die IT-Systemarchitektur entspricht auch der Planung, wie diese dokumentiert ist.
Denn diese oberen beiden Ebenen ändern sich auch nur viel langsamer als die unteren Ebenen.

Genau das ist aber in den untern beiden Ebenen oft nicht so: wenig Doku, und wenn überhaupt vorhanden meist hoffnungslos veraltet und entspricht nicht mehr der Realität. Die ursprünglich vielicht guten Ideen der Architekten sind bis zur Unkenntlichkeit verändert.

## TDD und Softwarearchitektur Behauptung

So, die Behauptung die jetzt im Raume steht, ist also, dass TDD/TestFirst bei der Softwarearchitektur der untern beiden Ebenen massiv hilft und auch hift über längere Zeiträume diese Architektur positiv beeinflusst.

Im Gegensatz dazu, helfen nachträglich hinzugefügte automatische Tests zwar für die Softwarequalität im Sinne von Stabilität und Fehlerarmut. Nachträglich hinzugefügte automatische Tests helfen aber gar nicht für die Softwarearchitektur, für keine der 4 Ebenen.

## Probleme der Softwarearchitektur ohne TDD

Bei Software die von mehrköpfigen Teams gebaut werden, ist es wichtig, dass nicht nur der ursprüngliche Autor eine Methode oder Klasse leicht versteht, und auch nach Wochen und Monate noch versteht.

Denn Software, die wirklich benutzt wird, muss eben immer wieder an neue Anforderungen angepasst werden und weiterentwickelt werden, da erzähle ich ja niemandem was neues.

Wenn ich aber Softwareteile anpassen und erweitern muss, muss ich erstmal verstehen, was da bisher steht. Und zwar möglichst schnell.

Genau hier kommt die Softwarearchitektur der unteren beiden Detailebenen ins Spiel.

- ist die Softwarearchitektur für einen Entwickler schnell verständlich oder nicht ?
- ist die Softwarearchitektur flexibel und leicht änderbar ?

### Beispiel Zoo

Wir haben in unserer Zooverwaltungssoftware bisher die Klassen "Ente", "Fisch", "Zebra":

Der Zoodirektor möchte aber jetzt auch Pferde anschaffen.
"Zebra" ist ja ein naher verwanter des Pferdes und kann rennen. Für eine schnelle Quick-and-Dirty Lösung könnte man ja die Klasse "Zebra" einfach in "Huftiere" umbenennen. Das funktioniert auch erstmal.

Später fällt dann unserem Zoodirektor ein , dass Pferde ja regelmäßig beschlagen werden müssen, somit müssen wir ein Datum fürs nächsten Beschlagen erfassen und auswerte.

- was ist jetzt mit dem Zebra?
- wir wollen wissen, wann das Pferd neu beschlagen werden muss. Das ist aber für Zebras irrelevant.

In all diesen Fällen bauen wir nicht nur neue Eigenschaften in die Klassen ein, sondern mit diesen Eigenschaften werden auch Ergebnisse berechnet. Da wir jetzt zu viele verschiedenen Tiere miteinander vermischt haben, haben wir jetzt innerhalb der Klassen komplexe Fallunterscheidungen. z.B. was geben wir als Ergebnis zurück wann wir bei Huftieren (wenn wir Zebras und Pferde jetzt so nenen wollen) neu Behufen müssen. Also: was ist das Datum für die Beschlagung bei einem Zebra ? : 1. Jan. 2099 ? in der Hoffnung das das Zebra bis dahin tot ist ?

Die Richtige Antwort ist: für Zebras darf es diese Methode gar nicht geben. Wir hätten die Huftiere in weitere Unterklassen aufteilen müssen und so schon über die Klasse die Unterscheidung treffen können. Das wäre dann bessere Architektur.
In realen Projekten sieht man aber solche Änderunge oft nicht, oder zumindest nicht rechtzeitig.

Das ist nur ein Beispiel wie Architektur verfällt und erodiert und **SOLID**-Prinzipien[^2] verletzt.

Nach SOLID ist z.B. das **Single Responsibility Prinzip** (SRP) eines von 5 Architekturprinzipien oder Architekturregeln das besagt, dass niemals mehr als einen Grund geben sollte eine Klasse zu ändern.

### Beispiel Report

Noch ein Beispiel dazu:

Wir haben ein Modul , das einen Report zusammenstellt und drucken soll. So ein Modul kann aus 2 Gründen gändert werden müssen. 1. der Inhalt des Reports ändert sich 2. das Format des Reports ändert sich
Das sind 2 verschiedenen Gründe . Das Single Responsibility (SRP) sagt nun, dass diese 2 verschiedenen Verantwortlichkeiten sind, die in verschiedenen klassen oder Modulen behandelt werden sollten.

Der Grund, warum es so wichtig ist eine Klasse auf einen Aspekt zu fokusieren ist, dass das die Klasse robuster machen.
z.B . wenn es nur eine Änderung in der Reportzusammenstellung gibt, ist das Risiko dabe versehentlich die Formatierung bei Drucken zu zerstören geringer. und umgekehrt.

Es ist auch weniger Riskant, wenn beides geändert werden muss und die Aufgabe auf 2 Teams verteilr wird.

Fazit: es gibt viele gute Ratschläge und Konzepte für gute Softwarearchitektur, aber

- erstens ist nicht allen Entwickler das zu jeder Zeit bewußt und zweites gibt es nicht zu jeder Zeit den Willen die Regeln auch immer Anzuwenden.
- zweitens muss, oder besser "müsste" die Architkur in der Hinsicht immer wieder überprüft werden , was aber im Rahmen des Tagegeschäfts (einbauen neuer Funktionen) immer wieder in den Hintergrund rückt.
- drittens fällt die Verletzung der Regeln nicht immer gleich auf und sticht nicht sofort ins Auge .

Hier hilft TDD

## Wie hilft TDD/TestFirst bei der Softwarearchitektur?

Ok, jetzt denken vieleicht viele von euch: "ok, Softwarequalität, Stabilität, Zuverlässigkeit, da sehe ich einen Zusammenhang zu automatischen Tests, aber was hat das mit Softwarearchitektur zu tun ?"

TDD und Test first...

- .. zwingt **vor** dem Schreiben des eigentlich Code und der eigentlichen Unittests dazu, sich **sehr** **klar**, **sehr** **klar**, über die **Anforderungen** und das Softwaredesign und zwar auf Klassen/Interface- Ebene Gedanken zu machen.

- .. trägt dann auf fast schon magische Weise automatisch zu einer **klareren Softwarearchitektur** auf Klassen/Interface- Ebene bei.

- .. zu schreiben geht aber **nur**, wenn ich nicht nur die **fachlichen** Anforderungen genau verstanden sondern, wenn ich auch **genau** verstanden habe wie sich mein neuer Code in den bestehenden einfügen soll. Ich bin also mehr **gezwungen**, mir **vor** der ersten Codezeile, die ich schreibe, mit ein **durchdachtes Konzept** zu machen.

- Programm-Code der so entstanden ist, braucht meiner Erfahrung nach **weniger** späteres **Refactoring** (also Refactoring dessen Notwendigkeit erst in einem späteren Entwicklungszyklus offensichtlich wird)

- .. führt zu **kleineren** Klassen und Methoden, fördert automatisch das **[Single-Responsibility-Prinzip](https://de.wikipedia.org/wiki/Single-Responsibility-Prinzip)**, damit meine ich, kleinere Klassen und kleinere Methode, die von weniger anderen Klassen abhängen. **Damit** wird die Software leichter **verständlich** und auch **leichter** und damit billiger **anpassbar**.

- Durch Test first fällt die Verletzung des **SOLID** Prinzips (RESERVE-FOLIE: SOLID: Single Responsibility (SRP), Open/Close, Liskov's Substitution, Interface Segregation, and Dependency Inversion.) schneller auf, weil die Tests andernfalls schnell komplex und groß würden und man z.B. sehr viele Mock-Objekte[^3] benötigt.

Ich hoffe euch ist klar, dass das was sehr gutes ist. TDD spart, im richtigen Context eingesetzt (dazu mehr im Teil 3), am Ende halt doch Zeit und liefert **höhere Code-Qualität**.

[zurück zum Teil 1](../TDD-TestFirst-Teil1-Warum)

[weiter zu Teil 3: TDD Beweise,Beweise](../TDD-TestFirst-Teil3-Beweise)

# Fußnoten:

[^1]: Kent Beck: Extreme Programming Explained. Embrace Change., Addison-Wesley, 2000, ISBN 0-201-61641-6. Kapitel 18 https://books.google.de/books?id=G8EL4H4vf7UC&lpg=PR9&ots=jbvErnnRBq&dq=%22We%20will%20write%20tests%20before%20we%20code%2C%20minute%20by%20minute.%22&hl=de&pg=PA115#v=onepage&q=%22We%20will%20write%20tests%20before%20we%20code,%20minute%20by%20minute.%22&f=false
[^2]:
    SOLID steht für : Single Responsibility (SRP), Open/Close, Liskov's Substitution, Interface Segregation, and Dependency Inversion.
    The SOLID concepts are:
    The **Single-responsibility principle**: "There should never be more than one reason for a class to change."In other words, every class should have only one responsibility.
    The **Open–closed principle**: "Software entities ... should be open for extension, but closed for modification."
    The **Liskov substitution principle**: "Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it". See also design by contract.
    The **Interface segregation principle**: "Many client-specific interfaces are better than one general-purpose interface."
    The **Dependency inversion principle**: "Depend upon abstractions, [not] concretions."
    The SOLID acronym was introduced later, around 2004, by Michael Feathers.
    [Quelle und Zitate](https://en.wikipedia.org/wiki/Single-responsibility_principle)

[^3]: für die Nicht-Entwicker: Mockobjecte sind quasi das , was im Crashtests von Autos die Dummys sind, man testet zwar mit Echte Autos (also analog unser zu testender Code), aber nicht mit echten **Menschen** (bei uns andere Klassen/Methode, die für das durchlaufen des eigentlichen Testcodes nötig sind) . Man könnte einen eigenen Vortrag über Mocks machen, aber das lassen wir hier mal absichtlich bei Seite.
