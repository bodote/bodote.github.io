---
title: "Test Driven Development und Test First für NueDigital"
date: 2021-05-20 // zukünftige Datum wird nicht veröffentlicht !
published: false
visible: true
categories:
  - Blog
tags:
  - Testing
  - TestFirst
  - Talk
toc: true
#classes: wide
---

[Nürnberg Digital 2021](https://nuernberg.digital/mitmachen/veranstalter.html),
Coding Track, 2021-07-16 - 2021-07-19

# Short Teaser:

Den „Test First“-Ansatz konsequent umzusetzen, ist schwerer als gedacht. Viele gehen daher den leichteren Weg, schreiben automatische Tests nach der Entwicklung und verschenken damit viele Vorteile.

# Long Teaser:

Selbst in großen Software-Projekten wird oft erst ganz am Ende getestet – woher aber kommt diese „Test Last“-Philosophie und warum halten so viele Entwickler so überzeugt daran fest?
Im Vortrag gehen wir dieser Frage gemeinsam auf den Grund. Auf dem Weg zu einer Antwort klären wir außerdem, was mit Test-driven Development und Test First überhaupt gemeint ist, untersuchen anhand vieler Beispielprojekte den Status Quo und tragen mit einem Blick in Literatur sowie einschlägige Studien die vielen nachgewiesenen Vorteile dieser Entwicklungsmethoden zusammen. Wir wollen Vorurteile abbauen und die wichtigsten Fragen rund um Test-driven Development beantworten: Warum ist Test First scheinbar so schwierig? Welche Vorteile verschenken wir, wenn wir rein auf Test Last setzen? Wird Softwarearchitektur durch Test First wirklich besser? Welchen Unterschied genau macht es, die Tests vor der Implementierung zu schreiben statt im Nachhinein? Warum hat Test First automatisch einen sehr positiven Einfluss auf meine Softwarearchitektur, Test Last aber eher weniger? Wie kommen wir von Test Last zu Test First? Und welche Fragen hast du zu dem Thema?

# Timestamp: 0

# Short Teaser2:

## Ganz Gallien ist ...

## Die ganze Softwarewelt ist

.. von Agilität und Scrum besetzt! Wirklich ? Nur ein kleines scheinbar unbedeutendes Kapitel in Kent Becks Buch aus dem Jahr 2000, in dem er die Grundlagen zu Scrum gelegt hat, wiedersetzt sich nach wie vor der wirklich großen Verbreitung. Das Kapitel beschreibt Test Driven Development.
Warum ist das so ? Ist TDD wirklich eine so gute Idee? Warum wird es dann nicht überall eingesetzt? In welchem Umfeld steigert es die Produktivität der Softwareentwicklung, in welchem Umfeld vieleicht ist es sogar contraproduktiv ?

Genau darüber werden wir heute sprechen!

# Mein Name..

ist Bodo. Ich bin Co-Founter von BRANDAD Group AG (früher bekannt als BRANDAD-System AG). 1980 begann ich mit meinem ersten Computer Sinclair ZX80 Software zu entwicklen.
Zunächst in Basic und Assember, später dann C, jetzt schon lange Java und in letzter Zeit auch Javascript.

# Willkommen

...zu "Test-driven Development?! Na klar … aber richtig!"

## Mein Ziel (Folie 5):

ist, dass jeder von euch nach dem Vortrag rausgeht und sich sagt: hey, über dieses TDD muss ich mehr lernen, und ich muss gleichzeitig rausfinden, wo TDD angebracht ist, und wo nicht.

- (Folie weiter lesen)

  - Warum Testautomatisierung nicht TDD ist
    - Manche denken sich vieleicht: Ok, langweilig, Testautomatisierung machen wir doch schon lange! Jaaaaa, aber **Testautomatisierung ist eben nicht TestDrivenDevelopement**.
    - Denn wie kann das Schreiben eines Tests dein "Development" treiben wenn du die die Test erst im nachhinein schreibtst , also **"test-last"** arbeitst?
    - Der Name TestDrivenDevelopement meint das wirklich wörtlich. Und das bedeutet: du schreibst den TEST BEVOR du den eigentlich Code schreibts.
    - **Wer von euch** hat das schonmal gemacht? ehrlich ?
  - TDD bringt wirklich 50% weniger Bugs als Test-Last? Ich kann das beweisen
  - Wie funktioniert TDD mit Unittests? Praktisches Beispiel
  - In welchen Kontexten TDD passt, in welchem nicht.

- TDD ist ein großes Thema über das schon viele Bücher geschrieben wurde. Wir wollen uns heute anschaun,
  - was unterscheidet TDD von anderen Arten der Testautomatisierung,
  - welche Argumente sprechen dafür
  - wo kann TDD helfen,
  - und wer setzt es ein?
  - Wie funktoniert das konkret?

## Warum beschäftigt mich TDD? (Folie 6)

### (Kent Beck, "Extreme Programming")

- Das Thema beschäftigt mich, seit ich so ums Jahr **2000** das Buch "Extreme Programming" von Kent Beck gelesen habe.

- In dem Buch war viel von den **Konzepten** die Rede, die später unter dem Namen "**Scrum**" bekannt wurden.

- Dazu muss man wissen: Kent Beck ist nicht **irgendein** Fachbuchautor, er ist einer DER Fachbuchautoren, Speaker auf allen einschlägigen Konferenze.

  - Vor allem aber ist er **anerkannt** als einer DER Vordenker der Softwareindustrie.
  - Er hat die Art und Weise wie wir heute Software entwickeln wie kaum ein Anderer beeinfluss.
  - Er war maßgeblich am **"Agile Manifest"** beteiligt, das **2001** publiziert wurde und damit eine wahre **Revolution** in der Softwarebranche ausgelöst hat.
  - Also, er ist tatsächlich einer der "**Erfinder**" von Scrum, wenn du so willst. Und inzwischen arbeitet praktisch **jeder** in der Softwareindustrie weltweit nach der Methode, oder zumindest **behaupet** praktisch jeder, dass er nach Scrum arbeite würde.

- Also 2000 hatte ich das Buch gelesen. Aber der Inhalt war genau , was der Titel versprach. Nämlich **Extrem**. Für die meisten damals war es es vor allem aber **extreme** Unsinn. Wer hatte denn sowas schon mal gehört: die Entwickler sollten **paarweise** am gleichen Problem gemeinsam arbeiten!
  Mit kam das auch zumindest ungewöhnlich und überraschend vor. Aber ich hatte schon genügend Probleme in meinen damals 5 Jahren Berufserfahrung gesehen, dass ich für neue Lösungsansätze sehr offen war. Kent Becks Ideen fand ich jedenfalls sehr spannend.

- Aber in 2003 also 3 Jahre später: Als ich damals meinem **Kompangnion Joachim** von dieser Vision für eine bessere Methode der Softwareentwicklung erzählt habe und Ihn überzeugen wollte von der Vision, hat er nur gesagt: "Wer **Visionen** hat sollte zum Arzt gehn" (nur um dann ein paar Jahre später einzusehen, dass Kent Becks Ideen doch **extrem** brauchbar sind)

- Also mit Scrum war erstmal **nix**, Anfang der 2000er Jahre! Die Zeit wahr noch nicht reif. Aber da gab es ja noch Kapitel 18: Auf gerade mal **6 Seiten** erklärte Kent Beck, dass man Software automatisch testen sollte und sogar die Tests **VOR** dem **eigentlichen** Teil der Software schreiben sollte.

## Folie 7 **before** we code

- Zitat "We will write tests **before** we code, minute by minute. We will preserve these tests forever, and run them all together frequently. We will also derive tests from the customer's perspective."

  - Dazu wiederhole ich nochmal: Kent Beck ist **nicht irgendwer**, sondern einer **der** ganz großen **Vordenker** der **agilen Bewegung** und der Softwarebranche insgesamt.
  - So, und wenn einer DER großen Vordenker der letzten 20 Jahre in der Branche eine Konzept wie TDD vorschlägt, dann darf man das auf jeden Fall **sehr ernst nehmen**, und es lohnt sich sicher, sich damit näher aueinanderzusetzten, oder?

- **Zurück** zu mir ins Jahr **2000**. **Damals** war das allerdings alles andere als offensichtlich und Kent Beck war mit seinem Buch **einer unter vielen**, der halt ein paar **verrückt klingende Ideen** hatte.

- Trotzdem das damals echt revolutionär und **für mich völlig neu** war, wollte ich das gleich ausprobieren. Irgendwie war ich auch auf der Suche nach Ideeen, wie man besser als **bisher** Software entwickeln könnte. Denn ich hatte in meiner bisherigen Berufserfahrung natürlich auch eine Reihe von Problem in Softwareentwicklungsprojekten gesehen, für die ich Lösungen suchte.

- Dabei hatte ich das Glück, dass ich damals gerade einen **neuen Job** hatte, in dem ich mir erstmal selbst selbst Java beibringen durfte. Java war damals ja auch noch einigermaßen neu.

# timestamp 8 min

## Folie 8

- Noch besser aber war: ich durfte auch fast 2 Jahre mehr oder weniger **unbehelligt** an eine Projekt programmieren, mit nur einer Hand voll Anforderungen, und weitgehend unbehelligt von unbequemen Fragen oder gar Termindruck. Mein Damaliger Chef verbrachte nämlich die meiste Zeit auf Jamaika mit seiner heißen jamaikanischen Freundin und war deshalb nur 2 mal im Jahr überhaupt anwesend.
  Außerdem warn wir eine RisikoKapital finanziertes Startup, die Internetblase war damals noch voll am Aufblähen und Geld spielte Keine Rolle. Die Startups waren froh wenn sie überhaupt Softwareentwickler finden konnten.

- Die Aufgabe war ein Typesetting Engine für ein (**Web2Print**) System zu entwicklen. Web2Print sagt euch was ? Im Grunde ist die Idee aus den Eingaben in ein Webformular ein Druckreifes PDF zu produzieren. Z.B. fürs Marketing. Das Webformular kann im Prinzip Sekretärin vom Chef ausfüllen und mit dem System ein 100% perfektes CI-konforme Werbeanzeige für die Tageszeitung produzieren. Man spart quasi den Graphiker ein.

- Genau das machen wir bei BRANDAD Systems nach wie vor. Nur dass wir die Idee jetzt natürlich auch auf alle möglichen Social Media Kanäle ausgedehnt haben. Print verliert naturgemäß immer mehr Anteile, obwohl gerade die Regionalen Tageszeitungen für die Regionale Werbung natürlich nach wie vor wichtig sind.

- Wer im Pubikum kennt noch _TeX_ oder _Latex_? Ja, genau! Damit hat man damals Diplomarbeiten, Wissenschaftliche Paper, usw. geschrieben. Vor allem im naturwissenschaftlichen - technischen - mathematischen Bereich . Denn **MS-Word** war damals für sowas ziemlich **unbrauchbar**, und ist es zum Teil heute noch.

- Jedenfalls: Ein paar Jahre früher hatte ich damit meine Diplomarbeit geschrieben. Daher kann ich Latex. Die **Algorithmen von Latex** , also wie die Buchstaben genau auf dem Papier positioniert werden müssen, damit das Typographisch korrekt aussieht, waren in einem Buch erklärt. Das besorgte ich mir und programmierte das ganze in Java nach. Nicht 1 zu 1. Sonst hätten wir ja gleich Latex nehmen können. Das Quellformat , also die Beschreibungssprache, sollte jetzt eben nicht die auf der Latex-Syntax basieren, sondern auf dem damals **ganz modernen XML**. Die Idee hatten andere auch schon , daher gabs bereits eine standardisierte Layout Beschreibungssprache genannt XSLT/FormatingObjects.

- Die Idee war also eine Typestting Engine mit den Ideen aus Latex und XSLT/Formatting Objekts in Java zu entwickeln.

- Und da ich wie gesagt keine weiteren Vorgaben hatte , und auch keinen wirklichen Zeitdruck, nahm ich mir vor das ganze mit dem TestDriven Development Ansatz zu entwickeln. und Weil ich das Projekt auch ganz allein entwicklen durfte, musste ich mich mit niemandem absprechen. Mein Chef war ja sowieso in Jamaika , also weit weg.

- Was soll ich sagen: für mich hat das damals prima funktioniert. Seit dem bin ich ein großer Fan von TestDrivenDevelopemt.

- Aber genug der alten Geschichten.. **der Punkt ist**, dass ich damit **TestDrivenDevelopment** mit Hilfe der 6 Seite aus Kent Becks Buch recht **erfolgreich** gelernt und praktisch **angewendet** habe.

# timestamp 13 min

## Warum TDD und Test First?

https://youtu.be/FlJN6_4yI2A?t=1595 26:35

- **Welches Problem** will TDD und "Test First" eigentlich lösen ?
  But: https://youtu.be/FlJN6_4yI2A?t=3084 51:26

### Stabilität, Qualität (Folie 9)

- In Softwareprojekten die von mehrern Entwicklern über mehrer Jahre entwickelt, weiterentwickeln und neuen Anforderungen angepasst werden, entstehen typischerweise eine Reihe von Qualitäts Problemen. Und wie die meisten aus der Branche inzwischen auch gelernt haben: Mit automatischen Tests lässt sich die Qualität nicht nur deutlich verbessern, da sind wir uns sicher einig. Sondern ausreichende Testabgeckung vorrausgesetzt, kann man damit dann auch ein bestimmtes Qualitätsniveau auf Dauer halten.

- Ich hoffe, bis jetzt hab ich euch nix neues erzählt...
- Das Besondere an TDD und Test first ist aber dass die Bugraten nochmal um 50% oder mehr gesenkt werden kann im Vergleich zu Test-Last
- Ich glaubt das nicht ? Ich dann das beweisen , wie wir später noch sehen werden.

- Softwarequalität, Stabilität, Zuverlässigkeit, Belastbarkeit sind früher oder später ein Thema in praktisch jedem Projekt, aber es gibt noch weitere Probleme die in Softwareprojekten typischerweise mit der Zeit auftauchen :

- Also im Vertrauen, dass euch der Zusammenhang zwischen Testen und Qualität und damit auch automatischem Testen und Softwarequalität klar ist, lasst mich direkt auf die Softwarearchitektur eingehen:

### Softwarearchitektur (Folie 10)

in größeren Softwareprojekten entsteht typischerweise noch ein weiteres Problem:

- Die Entwickler brauchen immer länger um Funktionen einzubauen.

  - oft stellen die Beteiligten fest, dass je größer die Software wird und je älter, desto schwieriger und langwieriger wird es, Anpassungen und Änderungen vorzunehmen.
    - viele nehmen das als Gott-gegeben hin, aber das muss nicht so sein.
  - Warum ist das aber oft so ?
  - Ursprüngliche Architektur war noch klar strukturiert, Architekt und/oder die ERsten Entwickler hatten ein gutes Konzept und das auch so umgesetzt
  - dann aber setzt Fluktuation der Entwickler ein oder die Entwickler werden mit der Zeit auch nachlässiger.
  - es gibt neue Anforderungen die eigentlich eine Anpassung der Architektur erfordern würden.
  - statt dessen wird versucht mit zunächst minimalem Aufwand hier und dort ein paar Kleinigkeiten dazuzustückeln.
  - saubere Architektur tritt in den Hintergrund, alle wollen möglichst schnell neue Features einbauen.
  - das gelingt auch zunächste. Gleichzeitige erordiert aber die Architektur immer mehr.
  - neue Entwickler kommen dazu , erkennen die geplante Architektur kaum noch und machen das ganze noch viel schlimmer.
  - Die Softwarearchitektur erodiert **Folie 10** bis zu Unkenntlichkeit: Dadurch, dass neue Entwickler, die die ursprüngliche Architektur nicht gut genug kennen, Änderungen vornehmen, entwickelt sich die Software von dieser Architektur auch immer weiter weg, bis dann kein architektonische Konzept erkennbar ist.

- Warum ist die Architektur so wichtig ?

  - Ich als Entwickler möchte nicht, dass Änderungen an Komponente A keine Überraschende Wirkung in Komponenten B nach sich zieht
  - Beispiel : ich baue hier in die Wand einen anderen Lichtschalter ein, der funktioniert auch zunächst. Aber plötzlich entsteht in der Wand gegenüber ein Kurzschluss und die ganze Wand brennt ab. Jetzt bin ich natürlich tagelang damit beschäftigt die Überraschung erstmal zu verstehen und dann das Problem notdürftig zu flicken.

- TDD verspricht das Architekturproblem auf Ebene 3 und 4 zu lösen. Aber was sind die Ebenen 3 und 4 überhaupt

# Timestamp 13 + 6 = 19 min

### Ebenen der Softwarearchitektur im Vergleich (Folien 11-19)

- Vorher ein Wort zu den verschiedenen Ebenen von Softwarearchitektur:
  - wie beim Bauen von Gebäuden gibt es ja auch in der Software oder allgemein IT-Sytsem-Architektur verschiedenen Ebenen: also
    - Wie sieht mein Stadtteil aus in dem die Gebäude stehen, wie sind die Straßen, Gehwege, Parks und Gebäude insgesamt organisiert?
    - Wie schaut die Fassade aus, und wie ist die Aufteilung in den Gebäuden? z.B. Büros, große oder kleine Wohnungen
    - Wie sind die Wohnungen aufteilt, z.b. wie groß ist das Wohnzimmer im Vergleich zur Küche
    - bis hin: welchen Bodenbelag hab ich wo, Welche Lichtschalter an dern Wand , welche Türgriffe?
  - Wenn wir diese 4 Ebenen auf Softwarearchitektur übertragen und das auf TDD anwenden, dann hilft TDD eher bei den untern beiden Ebenen, also bei der Architektur der kleineren Details, weniger bei den obern beiden Ebenen, der Architektur im ganz Großen.

### TDD und Softwarearchitektur Behauptung

- So, die Behauptung die jetzt im Raume steht, ist also, dass TDD/TestFirst bei der Softwarearchitektur der untern beiden Ebenen massiv hilft und auch hift über längere Zeiträume diese Architektur positiv beeinflusst.

- Im Gegensatz dazu, helfen nachträglich hinzugefügte automatische Tests zwar für die Softwarequalität im Sinne von Stabilität und Fehlerarmut. Nachträglich hinzugefügte automatische Tests helfen aber gar nicht für die Softwarearchitektur, für keine der 4 Ebenen

### Probleme ohne TDD (Wdh. nochmal anders erklärt)

- Bei Software die von mehrköpfigen Teams gebaut werden, ist es wichtig, dass nicht nur der ursprüngliche Autor eine Methode oder Klasse leicht versteht, und auch nach Wochen und Monate noch versteht.

- Denn Software, die wirklich benutzt wird, muss eben immer wieder an neue Anforderungen angepasst werden und weiterentwickelt werden, da erzähle ich ja niemandem was neues.

- Wenn ich aber Softwareteile anpassen und erweitern muss, muss ich erstmal verstehen, was da bisher steht. Und zwar möglichst schnell.

- Genau hier kommt die Softwarearchitektur der unteren beiden Detailebenen ins Spiel.

  - ist die Softwarearchitektur für einen Entwickler schnell verständlich oder nicht ?
  - ist die Softwarearchitektur flexibel und leicht änderbar ?

- Beispiel: "Duck", "Fisch", "Zebra" offensichtlich.

  - wir sollen jetzt auch Pferde berücksichtigen
  - "Zebra" ist ja ein naher verwanter des Pferdes und kann rennen.

- neue Anforderung:
  - später fällt dann unserem PO ein , dass Pferde ja regelmäßig beschlagen werden müssen, somit müssen wir ein Datum fürs nächsten Beschlagen erfassen und auswerte.
    - was ist jetzt mit dem Zebra?
    - wir wollen wissen wann das Pferd neu beschlagen werden muss. Ist aber für Zebras irrelevant
- In all diesen Fällen bauen wir nicht nur neue Eigenschaften in die Klassen ein, sondern mit diesen Eigenschaften werden auch Ergebnisse berechnet. Da wir jetzt zu viele verschiedenen Tiere miteinander vermischt haben, haben wir jetzt innerhalb der Klassen komplexe Fallunterscheidungen. z.B. was geben wir als Ergebnis zurück wann wir bei Huftieren (wenn wir Zebras und Pferde jetzt so nenen wollen) neu Behufen müssen. Ich mein: was ist das Erbebniss bei einem Zebra in form eines Gültigen Datums ? : 1. Jan. 2099 ? in der Hoffnung das das Zebra bis dahin tot ist ?

- Die Richtige Antwort ist: für Zebras darf es diese Methode gar nicht geben. Wir hätten die Huftiere in weitere Unterklassen aufteilen müssen und so schon über die Klasse die Unterscheidung treffen können. Das wäre dann bessere Architektur.
  In realen Projekten sieht man aber solche Änderunge oft nicht, oder zumindest nicht rechtzeitig.

- Das ist nur ein Beispiel wie Architektur verfällt und erodiert und das SOLID-Prinzip verletzt. Nach SOLID ist das Single Responsibility (SRP) das ersten von 5 Architekturprinzipien oder Architekturregeln.

- (RESERVE-FOLIE: SOLID: Single Responsibility (SRP), Open/Close, Liskov's Substitution, Interface Segregation, and Dependency Inversion.)

  - "A class should have only one reason to change."
  - The SOLID concepts are:
    - The Single-responsibility principle: "There should never be more than one reason for a class to change."[5] In other words, every class should have only one responsibility.[6]
    - The Open–closed principle: "Software entities ... should be open for extension, but closed for modification."[7]
    - The Liskov substitution principle: "Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it".[8] See also design by contract.[8]
    - The Interface segregation principle: "Many client-specific interfaces are better than one general-purpose interface."[9][4]
    - The Dependency inversion principle: "Depend upon abstractions, [not] concretions."[10][4]
    - The SOLID acronym was introduced later, around 2004, by Michael Feathers.[11]

- Als anderes Beispiel:

  - wir haben ein Modul , das einen Report zusammenstellt und drucken soll. So ein Modul kann aus 2 Gründen gändert werden müssen.
    1. der INhalt des Reports ändert sich
    2. das Format des Reports ändert sich
  - Das sind 2 verschiedenen Gründe . Das Single Responsibility (SRP) sagt nun, dass diese 2 verschiedenen Verantwortlichkeiten sind, die in verschiedenen klassen oder Modulen behandelt werden sollten.

  - Der Grund, warum es so wichtig ist eine Klasse auf einen Aspekt zu fokusieren ist, dass das die Klasse robuster machen.
    z.B . wenn es nur eine Änderung in der Reportzusammenstellung gibt, ist das Risiko dabe versehentlich die Formatierung bei Drucken zu zerstören geringer. und umgekehrt.

  - Es ist auch weniger Riskant, wenn beides geändert werden muss und die Aufgabe auf 2 Teams verteilr wird.

- Fazit: es gibt viele gute Ratschläge und Konzepte für gute Softwarearchitektur, aber

  - erstens ist nicht allen Entwickler das zu jeder Zeit bewußt und zweites gibt es nicht zu jeder Zeit den Willen die Regeln auch immer Anzuwenden.
  - Man muss die Architkur in der HInsicht immer wieder überprüfen , was aber im Rahmen des Tagegeschäfts (einbauen neuer Funktionen) immer wieder in den Hintergrund rückt.
  - Weil die Verletzung der Regeln fällt nicht immer gleich auf und sticht nicht sofort ins Auge .

- Hier hilft TDD

# Timestamp 19 + 13 = 32

## Wie hilft TDD/TestFirst bei der Softwarearchitektur?

- Ok, jetzt denken vieleicht viele von euch: "ok, Softwarequalität, Stabilität, Zuverlässigkeit, da sehe ich einen Zusammenhang zu automatischen Tests, aber was hat das mit Softwarearchitektur zu tun ?"
  Stimmts?

**Test first..**:

- .. zwingt **vor** dem Schreiben des eigentlich Code und der eigentlichen Unittests dazu, sich **sehr** **klar**, **sehr** **klar**, über die **Anforderungen** und das Softwaredesign und zwar auf Klassen/Interface- Ebene Gedanken zu machen.

- .. trägt dann auf fast schon magische weise automatisch zu einer **klareren Softwarearchitektur** auf Klassen/Interface- Ebene bei.

- .. zu schreiben geht aber **nur**, wenn ich nicht nur die **fachlichen** Anforderungen genau verstanden sondern, wenn ich auch **genau** verstanden habe wie sich mein neuer Code in den bestehenden einfügen soll. Ich bin also mehr **gezwungen**, mir **vor** der ersten Codezeile, die ich schreibe, mit ein **durchdachtes Konzept** zu machen.

- - Programm-Code der so entstanden ist, braucht meiner Erfahrung nach **weniger** späteres Refactoring (also Refactoring dessen Notwendigkeit erst in einem späteren Entwicklungszyklus offensichtlich wird)

- .. führt zu **kleineren** Klassen und Methoden, fördert automatisch das **[Single-Responsibility-Prinzip](https://de.wikipedia.org/wiki/Single-Responsibility-Prinzip)**, damit meine ich, kleinere Klassen und kleinere Methode, die von weniger anderen Klassen abhängen. **Damit** wird die Software leichter **verständlich** und auch **leichter** und damit billiger **anpassbar**.

- Durch Test first fällt die Verletzung des **SOLID** Prinzips (RESERVE-FOLIE: SOLID: Single Responsibility (SRP), Open/Close, Liskov's Substitution, Interface Segregation, and Dependency Inversion.) schneller auf, weil die Tests andernfalls schnell komplex und groß würden und man viele Mock-Objekte benötigt.

(Mockobjecte sind quasi das , was im Crashtests von Autos die Dummys sind, man testet zwar mit Echte Autos (also analog unser zu testender Code), aber nicht mit echten **Menschen** (bei uns andere Klassen/Methode, die für das durchlaufen des eigentlichen Testcodes nötig sind) . Man könnte einen eigenen Vortrag über Mocks machen, aber das lassen wir hier mal absichtlich bei Seite)

Ich hoffe euch ist klar, dass das was sehr gutes ist.

- .. spart am Ende halt doch Zeit und liefert **höhere Code-Qualität**.

[mehr findest du hier](../_posts/2020-10-09-TDD-aber-richtig.md#test-first-ist-deswegen-entscheidend-weil)

## Beweise, Beweise Folie 20

So jetzt könnt ihr sagen: Der Teichmann kann uns ja viel erzählen, stimmt das denn überhaupt und funktioniert das in der Praxis ?

Die Frage ist, lassen sich meine Behauptungen belegen, welche Erfahrungen haben andern mit TDD/TestFirst gemacht?
Da findet man doch eine Menge Indizien, die dafür sprechen.

- Bücher über TDD selbst, werden immer wieder neu herausgebracht. Kent Becks Buch ist also beweitem nicht das einzige zu dem Thema.

- Bücher über Softwarearchitektur z.B.

- eine Reihe von wissenschaftlichen Studien, z.T. sogar richtige Vergleichsstudien

- eine Reihe von systematischen Erfahrungsberichten aus verschiedenen großen Unternehmen.

- sogar einige Metastudien zu dem Thema konnte ich finden.

- Zitat: "Das Spring Team unterstützt und beführwortet TestDrivenDevelopment. ["The Spring team advocates test-driven development,TDD ."](https://docs.spring.io/spring-framework/docs/current/reference/html/testing.html)

- Zitat: "Wir praktizieren selbst TestDrivenDeveopment. Da heißt, bevor wir die Arbeit an einem neuen Feature beginnen, schreiben wir zuerst einen Test, der das gewünschte Verhalten genau beschreibt." ["At VMware Pivotal Labs, we practice test-driven development (TDD). That means before we begin work on a new feature, we first write a test that describes the behavior we want to add to our software.](https://tanzu.vmware.com/content/blog/go-faster-write-tests-first)

### Ergebnisse:

- [IBM: Assessing test-driven development](https://collaboration.csc.ncsu.edu/laurie/Papers/MAXIMILIEN_WILLIAMS.PDF) : **50% weniger Bugs** als bei "test last", minimaler geringere Produktivität

- [Microsoft: Evaluating the Efficacy of Test-Driven Development: Industrial Case Studies](https://d1wqtxts1xzle7.cloudfront.net/36509027/fp17288-bhat.pdf?1423032149=&response-content-disposition=inline%3B+filename%3DEvaluating_the_Efficacy_of_Test_Driven_D.pdf&Expires=1599907639&Signature=RuaKEjh7AbrkimLa5LGjb6zOpojv18srJrYQO7ONLNjWm586g6nxlDjGnYgubwIFYYp5fNkQulFn6YD3wpvud5bBhvwkO4nOOFMYyhATLdvHjHtW3vzm6ncsuqgwYTIKtrxbxAd7lQiEiue~D300FsgSLK6ZUk9DOssTqS0NZry6syc9I6IQYR6H2BRcnzf9oxvCTBWPzjSEBPi2cqYpyKbF1Y322XtLj7fdNTu8IVkmUULxwH3R1GVsEZrdpOAOJpM0b1ZAsJZEI0K3hiv~ENiV79hUjoyRu5xLaDeDWA4Nhg4Q-J8Zu8UQ18hQEjl0dOZnq7o4Xq~2-8jbuzDxIQ__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA) : **Bugrate sinkt mit TDD um 62%-77%** , 15% -35% mehr Zeit für TDD notwendig.

- [Metastudie, die 6 unterschiedliche andere Studien ausgewertet hat](https://digitalcommons.calpoly.edu/cgi/viewcontent.cgi?article=1027&context=csse_fac): Ergebnis: deutlich **Positiv, auch bezüglich Software-Architektur**

- [An Experimental Evaluation of the Effectiveness and Efficiency of the Test Driven Development](https://ieeexplore.ieee.org/abstract/document/4343756) : **deutlich bessere Gesamt-Produktivität und Codequalität**

- [noch eine Metastudie](https://www.researchgate.net/profile/Burak_Turhan/publication/258126622_How_Effective_is_Test_Driven_Development/links/54e794320cf27a6de10a8afe/How-Effective-is-Test-Driven-Development.pdf) : Gesamturteil deutlich positiv, aber Hinweis: schwer zu meistern , **Fazit: Empfehlung für TDD**

- [Empirische Studie zu Test-Driven Development](https://link.springer.com/book/10.1007%2F978-3-642-04288-1) : "test first" ist **besser** darin, **lose gekoppelte** Softwarekomponenten hervorzubringen als "test last". "lose gekoppelt" bewirkt zum Beispiel bessere Wartbarkeit, verständlichkeit für die Entwickler, ist also was sehr gutes.

[mehr Details hier](../_posts/2020-09-19-Literaturrecherche-TDD.md)

## Was ist TDD genau? Folie 22-31

.. und was meint Kent Beck mit "We will write tests before we code, minute by minute."?
Folien 22 -31 erklären

### nochmal wiederholen mit anderen Worten:

...und nochmal zu den Folien zurückgehen

- Die Basis von TDD sind Unit-tests. Mit "**Unit**" ist die kleinste sinnvolle Einheit, die testbar ist gemeint. Möglichst nur eine Methode oder Klasse oder eine Gruppe von wenigen eng zusammengehörige Methoden oder Funktionen, die eine nützliche Berechnung oder Entscheidung machen.

- Also im besten Fall ein paar Zeilen Code, sagen wir zwischen 10 und 100 Zeilen

- der Begriff _Unittest_ meint dann einen Stück Software, welches die Korrektheit dieser einen **Unit** testet. Und nur dieser. D.h. der Test sollte nach Möglichkeit **keine anderen Teile** aus dem Softwareprojekt testen.

- Der Unittest soll **NICHT** andere Teile des Codes testen, auch nicht, wenn die zu testende **Unit** eigentlich noch andere Units benötigt, um zu funktionieren. Dafür benutzen wir dann sog. **"Mocks"** oder "Mockobjekte" und **Spys**. Diese Thema sprengt aber den heutigen Vortrag.
  Also kurz gesagt: **Mocks** sind quasi **"TestDummys"** z.B. : hält der Testdummy überhaupt den **Aufprall** auf dem Luftsack auf oder noch besser: **bläst** sich der Prallsack **schnell genug** auf als der Kopf vom Dummy darauf einschlägt?

- Der **Unit-Test-Code** sollte dabei **alle** möglichen Pfade in der der nützlichen **Unit** abtesten. Dabei insbesonders alle **Grenzbedinungen** in der **Unit** auf Korrektheit überprüfen.

- Das Ergebnis ist dann eine sogenannte Testabdeckung von 100%. Auf die "Testabdeckung" gehen wir später noch ein.

- Der eigentliche Witz ist aber vor allem: Wir schreiben den Test **BEVOR** wir den Code für die eigentlich nützliche Unit schreiben.

### ABER:

leider sieh man an so einem einfachen Beispiel noch nicht, wie sich TestFirst auf die Softwarearchitektur auswirkt. Das offenbart sich nach meiner Erfahrung erst dann, wenn man wirklich komplexte Anforderungen programmiert und der Code einen gewissen umfang an Verschiedenen Klassen hat.

Das heißt für euch: wenn Ihr selbst die Erfahrung machen wollt, dann müsst ihr leider den langen Weg gehen. Es gibt keine Abkürzung Dazu passt auch prima das Zitat aus dem "Test-Driven Java Developmeht" - Buch unten.

Meine Überzeugung ist, das den sehr guten Softwareentwickler von den Gewinner der Championsleague (um mal einen Vergleich aus dem Fußball zu bemühen) unterscheidet, ist, unter anderem TDD zu beherschen.

## Die wichtigen Fragen.

### Warum findet man so wenige Programmierer die das tatsächlich tun ?

oder anders gefragt: **Warum ist das eigentlich sooo schwer?**
Ist es wirklich sooo schwer ? Eindeutig ja!

- Zitat aus aus [Large-Scale Scrum >>LeSS<<](https://less.works/de/less/technical-excellence/test-driven-development):

  - "Wir treffen **selten** Entwickler, die in der Lage ware, sich TDD/TestFirst selbst beizubringen. Die meisten Entwickler brauchen **tage- oder gar wochenlanges** Pair-Programming, bis sie es können." und weiter :
  - "Test-Driven Development ist vermutlich die **schwierigste** agile Praxis, aber TDD ist gleichzeitig die einer der **größten Gelegenheiten** die Qualität und das Design des Codes zu verbessern.

- [Metastudie: How Effective is Test-Driven Development?](https://www.researchgate.net/profile/Burak_Turhan/publication/258126622_How_Effective_is_Test_Driven_Development/links/54e794320cf27a6de10a8afe/How-Effective-is-Test-Driven-Development.pdf) :

  - "Fast alle \[Studien\] sind sich einig, dass **TDD schwierig zu lernen** ist.

- Aus [Test-Driven Java Development - Second Edition](https://www.packtpub.com/product/test-driven-java-development-second-edition/9781788836111)
  - "It\'s not an easy thing to master TDD. Even after learning all the theory and going through best practices and anti-patterns, the journey is only just beginning. **TDD requires time and a lot of practice**. It\'s a long trip that does not stop with this book.

### Wie kann ich als Softwareentwickler mich in kleinen Schritten incrementell von TestLast zu TestFirst vorarbeiten ?

# Timestamp:

#### Zunächst klären wir ein paar Vorraussetzungen.

Sind wir überhaupt in der Situation, TDD mit 'test first' gerade anwenden zu können ?
_ Nehmen wir an, wir wären ein SWEntwickler in einem Team
_ irgend jemand hat sich schon über das Gesamtkonzept den Kopf zerbrochen und eine Software-Architektur entworfen und diese uns soweit erklärt, dass wir ein grobes Verständniss dafür haben.
_ Wir sollen jetzt ein neues Feature implementieren, wofür wir aller Vorraussicht mindestens eine neue Klasse, Komponente, oder Service oder ähnliches benötigen.
_ wir müssen zwar auch bestehenden Code ändern, aber der neu zu schreibende Code überwiegt auf jeden Fall. \* idealerweise gibt es schon irgendein Unittest-Framework im Projekt, auch wenn das bisher nur zum "Test Last" eingesetzt wurde.

### Im Gegensatz dazu: wann ist TDD nicht der richtige Ansatz?

TDD/TestFirst macht unter folgenden Vorraussetzungen eher weniger Sinn.
Diese Punkte zu kennen , ist wichtig um Misserfolg bei der Anwendung von TestFirst zu vermeiden.

- ein großes Projekt ohne jegliche automatischen Tests

- nur minimale Kenntnis der eingesetzten Sprache/Framework/Testframework

- Architektur ist unklar.

- die Hauptarbeit ist rauszufinden, welche 2 Parameter geändert werden sollen, damit die neue Anforderung erfüllt wird, kaum oder gar keine neuer Code zu schreiben

- oder ganz banal: wir schreiben nur HTML oder verändern nur Parameter des schon vorhandenen und hoffentlich mit Unittest versehenen Codes

  - bei Oberflächen, speziell HTML: evtl. besser 'test last' mit snapshot testing (echtes 'test first' kann (muss aber nicht) hier overkill sein)

- sehr große Skepsis bis Ablehnung im Kollegenkreis, keine Unterstützung durch PO/Scrummaster/Architekt

### Ich hab noch nie TestFirst gemacht, wie komme ich dahin?

Nach der Vorwarnung gilt trotzdem: mit hinreichender Motivation kann man TDD sich durchaus selbst beibringen. Wichtig ist nur entweder große Neugierde, oder die feste Überzeugung, dass es sich auszahlen wird.
Daher hier eine Schritt für Schritt Anleitung:

1. mache ein paar "Trockenübungen" also Übungsaufgaben abseits von realem Produktionscode, aber mit den gleich Sprachen/Tools wie deine Produktionsumgebung
   - Suche die eine kleine Übungsaufgabe, die du in höchtens 1 stunde lösen kannst. [Ideen hier](https://www.freecodecamp.org/news/the-10-most-popular-coding-challenge-websites-of-2016-fb8a5672d22f/)
   - notfalls, wenn du noch gar keine Plan für Test-First hast, fang mit Test-Last an und lerne wie man überhaupt Unittests schreibt.
   - wenn du fertig bis, lösche alles und fang mit der selben Aufgabe ganz von vorn an, diesmal aber test-first
   - mache diese Übung ein paar mal, immer wieder, bis du für die Lösung mehr googlen musst und bis es es dir sehr flüssig von der Hand geht,
   - du wirst feststellen: in jeder Iteration wirst du nicht nur schneller, sondern dein Code bekommt mit jeder Iteration auch eine bessere Struktur, wird kompakter, gleichzeitg leichter für andere verständlich.
1. in der Produktionumgebung: fange an gute Test-Last Tests zu schreiben. Prüfe deren Testabdeckung, verwende Mutation-Testing. Baue Know How auf, wie du überhaupt Unittests in deinem Projekt schreiben kannst.
1. Organisiere oder nehme Teil an Coding Dojos für Test-First
1. beginne auch in Produktionumgebung mit TestFirst.

# Timestamp 40 min

# Bonus Content:

## Testabdeckung messen ?

- Ja, aber nur wärend des schreibens der Tests, um Lücken in der Testabdeckung zu finden. ![testCoverage](/assets/images/testCoverage.png){:height="360px" width="360px"}

- NEIN, um Qualitätsaussagen über die gesamte Codebasis zu machen

  - weil es gibt Code der nicht sinnvoll zu testen ist, z.B. weil er keine Fallunterscheidungen oder Schleifen enthält. Hier nachträglich die Testabdeckung zu erhöhen macht die Codebasis in der Regel nicht besser.

- Beispiel : ???

### noch besser: Mutation-Testing, hilft auch bei Test-Last!

- [Mutation-Testing](https://en.wikipedia.org/wiki/Mutation_testing)

- hilft vor allem blinde Flecken zu finden, sehr gut auch für "test-last"

- Konkret:
  - [javascript (including angular)](https://stryker-mutator.io/docs/stryker-js/) getting-started
  - [java](https://pitest.org)

```java
float berechnePreis(preis, rabat, bestelldatum ,rabattZeitraumBeginn ,rabattZeitraumEnde){
    if ( preis >= rabatminimum AND bestelldatum >= rabattZeitraumBeginn AND  bestelldatum <= rabattZeitraumEnde ) {
        preis = preis-(preis*rabatt)
    }
    return preis;
}
```

Mutation wird vom Testtool automatisch eingefügt :

```java
float berechnePreis(preis, rabat, bestelldatum ,rabattZeitraumBeginn ,rabattZeitraumEnde){
    if ( preis < rabatminimum AND bestelldatum >= rabattZeitraumBeginn AND  bestelldatum <= rabattZeitraumEnde ) {
        preis = preis-(preis*rabatt)
    }
    return preis;
}
```

## Anmerkungen fürs nächste mal: Beispiele einbauen. Einfluss auf SoftwareArchitektur nachweisen

https://www.youtube.com/watch?v=UWtEVKVPBQ0 :
Wenn Tests schwer zu schreiben sind, dass sagt das was aus über die Qualität unserer Softwarearchitektur: das stimmt was nicht!
https://web.archive.org/web/20100105084725/http://blog.james-carr.org/2006/11/03/tdd-anti-patterns/

https://www.javacodegeeks.com/2018/02/developers-dont-use-tdd.html

zum Ende des Vortrages UMFRAGE für Feedback!
