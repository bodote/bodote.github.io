---
title: "Test Driven Development und Test First für NueDigital"
date: 2020-07-16 // zukünftige Datum wird nicht veröffentlicht !
published: false
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
[Nürnberg Digital 2021](https://nuernberg.digital/mitmachen/veranstalter.html), 
Coding Track, 2021-07-16 - 2021-07-19
# Short Teaser:
Den „Test First“-Ansatz konsequent umzusetzen, ist schwerer als gedacht. Viele gehen daher den leichteren Weg, schreiben automatische Tests nach der Entwicklung und verschenken damit viele Vorteile.
# Long Teaser:
Selbst in großen Software-Projekten wird oft erst ganz am Ende getestet – woher aber kommt diese „Test Last“-Philosophie und warum halten so viele Entwickler so überzeugt daran fest? 
Im Vortrag gehen wir dieser Frage gemeinsam auf den Grund. Auf dem Weg zu einer Antwort klären wir außerdem, was mit Test-driven Development und Test First überhaupt gemeint ist, untersuchen anhand vieler Beispielprojekte den Status Quo und tragen mit einem Blick in Literatur sowie einschlägige Studien die vielen nachgewiesenen Vorteile dieser Entwicklungsmethoden zusammen. Wir wollen Vorurteile abbauen und die wichtigsten Fragen rund um Test-driven Development beantworten: Warum ist Test First scheinbar so schwierig? Welche Vorteile verschenken wir, wenn wir rein auf Test Last setzen?  Wird Softwarearchitektur durch Test First wirklich besser? Welchen Unterschied genau macht es, die Tests vor der Implementierung zu schreiben statt im Nachhinein? Warum hat Test First automatisch einen sehr positiven Einfluss auf meine Softwarearchitektur, Test Last aber eher weniger?  Wie kommen wir von Test Last zu Test First? Und welche Fragen hast du zu dem Thema?  
# Timestamp: 0
# Willkommen
...zu "Test-driven Development?! Na klar … aber richtig!"
# About me
Bodo Teichmann: Ich entwickle Software seit 1980, begonnen mit Basic, Assembler und C, jetzt schon lange Java und in letzter Zeit auch Javascript.
## Disclaimer
Bin ich ein TDD-Profi der von Konferenz zu Konferenz reist und sein tiefes Wissen mit immer neuen Varianten und Facetten zum Besten gibt? Nein! Dazu hab ich zu viel Zeit mit Aufgaben verbracht, bei denen ich leider keine Software schreiben durfte. 
Ich war nämlich auch mal Abteilungsleiter, bis mich Scrum, Scrumteam, Scrummaster und Product-Owner von meinem Leiden erlöst haben. 
## Warum beschäftigt mich TDD?
* Warum halte ich hier trotzdem einen Vortrag zum Thema TDD ? Weil mich das Thema schon **immer** interessiert hat, seit ich so ums Jahr 2000 das Buch "Extreme Programming" von Kent Beck gelesen habe. 
* Da war viel von den Konzepten die Rede, die später unter dem Namen "Scrum" bekannt wurden. Als ich 2003 meinem Kompangnion Joachim von dieser Vision für eine bessere Methode Software zu entwickeln überzeugen wollte, hat er nur gesagt: "Wer Visionen hat sollte zum Arzt gehn"  (nur um dann ein paar Jahre später einzusehen, dass Kent Becks Ideen doch extrem brauchbar sind)
* Also mit Scrum war erstmal nix! Aber da gab es ja noch Kapitel 18: Auf gerade mal 6 Seiten erklärte Kent Beck, dass man Software automatisch testen sollte und sogar die Tests **VOR** dem eigentlichen Teil der Software schreiben sollte.
* Zitat "We will write tests **before** we code, minute by minute. We will preserve these tests forever, and run them all together frequently. We will also derive tests from the customer's perspective."
* Das war damals echt revolutionär und für mich eine neue Idee, die ich dann gleich auch  umzusetzten versuchte. 
* Dabei hatte ich das Glück damals gerade einen neuen Job zu haben, in dem ich mir nicht nur selbst Java beibringen durfte. Sondern ich durfte auch fast 2 Jahre mehr oder weniger unbehelligt an einer neuen Text-Layout Engine programmieren, mit nur einer Hand voll Anforderungen, und weitgehend unbehelligt von unbequemen Fragen oder gar Termindruck. 
* Wer im Pubikum kennt noch *TeX* oder *Latex*? Ja, genau damit hatte ich ein paar Jahre zuvor meine Diplomarbeit geschrieben. Die Algorithmen von Latex waren in einem Buch erklärt. Das besorgte ich mich und programmierte das ganze in Java nach. Nicht 1 zu 1. Sonst hätten wir ja gleich Latex nehmen können. Das Quellformat sollte jetzt nämlich nicht die etwas kryptische Latex-Syntax sein, sondern das damals ganz moderne XML. 
* Aber genug der alten Geschichten..
## Warum TDD und Test First?
### Stabilität, Qualität
* Welches Problem will TDD und Test First eigentlich lösen ?
* In Softwareprojekten die von mehrern Entwicklern über mehrer Jahre entwickelt, weiterentwickeln und neuen Anforderungen angepasst werden, entstehen typischerweise eine Reihe von Qualitäts Problemen, die mit automatischen Tests deutlich verbessert werden können:
    * Softwarequalität, Stabilität, Zuverlässigkeit, Belastbarkeit werden früher oder später ein Thema sein
    * oft stellen die Beteiligten fest, dass je größer die Software wird und je älter, desto schwieriger und langwieriger wird es, Anpassungen und Änderungen vorzunehmen. 
    * Die Entwickler verbringen zu viel Zeit mit Bugsuche, statt neue Funktionen einzubauen.
### Softwarearchitektur 
* in größeren Softwareprojekten entsteht typischerweise noch ein weiteres Problem: 
    * Die Softwarearchitektur erodiert bis zu Unkenntlichkeit: Dadurch, dass neue Entwickler, die die ursprüngliche Architektur nicht gut genug kennen, Änderungen vornehmen, entwickelt sich die Software von dieser Architektur auch immer weiter weg, bis  dann kein architektonische Konzept erkennbar ist.
* Ok, jetzt denken vieleicht viele von euch: "ok, Softwarequalität, Stabilität, Zuverlässigkeit, da sehe ich  einen Zusammenhang zu automatischen Tests, aber was hat das mit Softwarearchitektur zu tun ?"
Stimmts?
* Also im Vertrauen, dass euch der Zusammenhang zwischen Testen und Qualität und damit auch automatischem Testen und Softwarequalität klar ist lasst mich direkt auf die Softwarearchitektur eingehen:
### Ebenen der Softwarearchitektur im Vergleich
* Vorher ein Wort zu den verschiedenen Ebenen von Softwarearchitektur: 
    * wie beim Bauen von Gebäuden gibt es ja auch verschiedenen Ebenen: also
        * Wie sieht mein Stadtteil aus in dem die Gebäude stehen, wie sind die Straßen, Gehwege, Parks und Gebäude insgesamt organisiert?
        * Wie ist die Aufteilung in den Gebäuden? z.B. Büros, große oder kleine Wohnungen 
        * Wie sind die Wohnungen aufteilt, z.b. wie groß ist das Wohnzimmer im Vergleich zur Küche
        * bis hin: welchen Bodenbelag hab ich wo, Welche Lichtschalter an dern Wand , welche Türgriffe?
    * Wenn wir diese 4 Ebenen auf Softwarearchitektur übertragen und das auf TDD anwenden, dann hilft TDD eher bei den untern beiden Ebenen, also bei der Architektur der kleineren Details, weniger bei den obern beiden Ebenen, der Architektur im ganz Großen.
### TDD und Softwarearchitektur Behauptung
* So, die Behauptung die jetzt im Raume steht, ist also, dass TDD/TestFirst bei der Softwarearchitektur der untern beiden Ebenen massiv hilft und auch hift über längere Zeiträume diese Architektur positiv beeinflusst.
* Im Gegensatz dazu, helfen nachträglich hinzugefügte automatische Tests zwar für die Softwarequalität im Sinne von Stabilität und Fehlerarmut. Nachträglich hinzugefügte automatische Tests helfen aber gar nicht für die Softwarearchitektur, für keine der 4 Ebenen
## Wie hilft TDD/TestFirst?
[hier](../_posts/2020-10-09-TDD-aber-richtig.md#test-first-ist-deswegen-entscheidend-weil)
## Beweise, Beweise
[hier](../_posts/2020-09-19-Literaturrecherche-TDD.md)

## Was ist TDD genau?
 .. und was meint Kent Beck mit  "We will write tests before we code, minute by minute."?
* Die Basis von TDD sind Unit-tests. Mit "**Unit**" ist die kleinste sinnvolle Einheit, die testbar ist gemeint. Möglichst nur eine Methode oder Klasse oder eine Gruppe von wenigen eng zusammengehörige Methoden oder Funktionen, die eine nützliche Berechnung oder Entscheidung macht. Also im besten Fall ein paar Zeilen Code, sagen wir zwischen 10 und 100 Zeilen   
* der Begriff *Unittest* meint dann einen Stück Software, welches die Korrektheit dieser einen **Unit** testet. Und nur dieser. D.h. der Test sollte nach Möglichkeit keine anderen Teile aus dem gesamten Softwareprojekt testen. Auch nicht, wenn die zu testende **Unit** eigentlich noch andere Units benötigt, um zu funktionieren. 
* Diese Test-Software sollte dabei alle möglichen Pfade in der der nützlichen **Unit** abtesten. Dabei insbesonders alle Grenzbedinungen in der **Unit** auf Korrektheit überprüfen. Das Ergebnis ist dann eine sogenannte Testabdeckung von 100%. Auf die "Testabdeckung" gehen wir später noch ein.
* Der eigentliche Witz kommt jetzt aber erst: Wir schreiben den Test **BEVOR** wir den Code für die eigentlich nützliche Unit schreiben. 
## Die wichtigen Fragen über die keiner spricht.
    * Wie geht das überhaupt ?
    * Warum findet man so wenige Programmierer die das tatsächlich tun ?
    * Warum ist das so schwer ? 
    * Wie kann ich als Softwareentwickler mich in kleinen Schritten incrementell von TestLast zu TestFirst vorarbeiten ?
* This is what we talk about today ! (wie meine Lieblings-Physikerin auf Youtube immer sagt)
# Timestamp:? Min
## Wie geht das überhaupt?
* Also, wenn man die paar Zeilen aus Kents Becks Buch einfach so versucht direkt umzusetzten, dann merkt man schnell, ganz so einfach ist das nicht. Kent Beck beschreibt auch gar nicht, wie das eigentlich praktisch umzusetzen ist.
### Zunächst klären wir ein paar Vorraussetzungen. 
Sind wir überhaupt in der Situation, TDD mit test first gerade anwenden zu können ?
    * Nehmen wir an, wir wären ein SWEntwickler in einem Team
    * irgend jemand hat sich schon über das Gesamtkonzept den Kopf zerbrochen und eine Software-Architektur entworfen und diese uns soweit erklärt, dass wir ein grobes Verständniss dafür haben.
    * Wir sollen jetzt ein neues Feature implementieren, wofür wir aller Vorraussicht mindestens eine neue Klasse, Komponente, oder Service oder ähnliches benötigen. 
    * wir müssen zwar auch bestehenden Code ändern, aber der neu zu schreibende Code überwiegt auf jeden Fall.
    * idealerweise gibt es schon irgendein Unittest-Framework im Projekt, auch wenn das bisher nur zum "Test Last" eingesetzt wurde.
### Im Gegensatz dazu: wann ist TDD nicht der richtige Ansatz?
TDD/TestFirst macht unter folgenden Vorraussetzungen eher weniger Sinn. 
Diese Punkte zu kennen , ist wichtig um Misserfolg bei der Anwendung von TestFirst zu vermeiden. 
* ein großes Projekt ohne jegliche automatischen Tests
* nur minimale Kenntnis der eingesetzten Sprache/Framework/Testframework
* Architektur ist unklar.
* die Hauptarbeit ist rauszufinden, welche 2 Parameter geändert werden sollen, damit die neue Anforderung erfüllt wird, kaum oder gar keine neuer Code zu schreiben
* sehr große Skepsis bis Ablehnung im Kollegenkreis, keine Unterstützung durch PO/Scrummaster/Architekt
### Wie gehen wir vor :
* Die Erfahrung zeigt, dass man sinnvollerweise so vorgeht:
    1. wir brauchen ein Konzept, das kann im einfachsten Fall im Kopf passieren, mit Papier und Bleistift, Oder, wer's gerne schwergewichtig mag (oder in einem großen Projekt Dokumentationspflichten hat), denn gern auch mit einer Software seiner Wahl.
    1. aus dem Konzept sollte hervorgehen, welche neuen Klassen benötig werden , wie diese heißen sollen, was deren Aufgabe und was NICHT deren Aufgabe ist. Also mit andern Worten welchen Methoden haben diese Klassen und wie heißen die Methoden?
    1. erzeugen alle Klassen mit leeren Methodenrümpfen
    1. füge die Parameter für die Methodenrümpfe hinzu 
    1. erst jetzt fange an die Unittests zu schreiben. sinnvoll ist eine 1:1 Entsprechnung von Klassen zu UnittestKlassen und eine n:1 Entsprechung von Test-Funktionen/Methoden. Also für jeden Methode in meiner Produktions-Code-Klasse brauche ich 1 oder mehrere Testfunktionen, weil ich ja verschiedene szenarien des   Produktions-Codes testen will.
    1. Identifiziere für jede Methode des Produktions-Codes welche Szenarien zu testn sind. Dazu sind  vor allem die Rand/Grenzbedingungen aus den Anforderungen wichtig.  Beispiele:
        * Rabatt, wenn Bestellsumme größer Grenzbetrag : 3 Testfälle: größer, kleiner, oder gleich
        * Eine Liste soll angezeigt werden: Testfälle: Liste ist leer, Liste ist normal Liste ist zu lang für eine Seite.
    1. Allgemein lässt sich feststellen: die Testfälle sollten sich aus den Anforderungen ergeben. Oder besser noch aus den Akzeptanzkritierien.:
        * Soll der Grenzbetrag aus obigen Beispiel variabel sein, wie, wo, von wem darf/soll dieser Festgelegt werden. Gilt der immer für einen bestimmten Zeitbereich? In dem Fall ergeben noch mehr Testfälle wie oben. z.B.  für Zeitbereich X gilt ein Rabatt - %-Zahl und für Zeitraum Y ein anderer. 2 Testfälle: die  Bestellung wird zum Zeitpunkt a innerhalb von Zeitbereich X  angelegt wird, und einmal zu Zeitpunkt b an der Grenze der Zeitbereiche X zu Y:   wie hoch muss dann der Rabattbetrag der Bestellung in beiden Fällen sein, welche Uhrzeit gilt hier ? UTC, Uhrzeit des Kunden, Uhrzeit des Servers? .
        * also je Akzeptanzkriterium mind 1 oder mehrere Testfälle
    1. Programmiere also zuerst deinen Testfall. Dieser Test müsste jetzt fehlschlagen, weil der Produktions-Code ja nur leere Methoden enthält die nix machen und höchstens "0", leere Objekte o.ä. zurückgeben.
    1. erst jetzt implementiere den eigentlichen Produktions-Code aber nur soweit , bis der Test "grün" ist, auf keinen Fall mehr!
    1. Programmiere den nächsten Testfall und erweitere deinen Produktions-Code; aber nur soweit , bis der neue Test "grün" und alle bisherigen Tests "grün" sind, auf keinen Fall mehr!
    1. hast du alle Testfälle fertig und alle sind grün: Refaktoriere den Code , bis er möglichst einfach und verständlich ist. Nutze dazu die Sicherheit die dir deine Testabgeckung gibt.
GRAFIK: Flussdiagramm ???

## Testabdeckung messen ?
* Ja, aber nur wärend des schreibens der Tests, um Lücken in der Testabdeckung zu finden.
* NEIN, um Qualitätsaussagen über die gesamte Codebasis zu machen 
    * weil es gibt Code der nicht sinnvoll zu testen ist, z.B. weil er keine Fallunterscheidungen oder Schleifen enthält. Hier nachträglich die Testabdeckung zu erhöhen macht die Codebasis  in der Regel nicht besser.
* Beispiel : ???

### noch besser: Mutation-Testing, hilft auch bei Test-Last!
* Erklärung: [](https://en.wikipedia.org/wiki/Mutation_testing)
* auch hier gilt: macht nur Sinn für die Anforderungen , an denen ich gerade arbeite, hilft mir blinde Flecken zu finden
* Beispiel: 

~~~ java
float berechnePreis(preis, rabat, bestelldatum ,rabattZeitraumBeginn ,rabattZeitraumEnde){
    if ( preis >= rabatminimum AND bestelldatum >= rabattZeitraumBeginn AND  bestelldatum <= rabattZeitraumEnde ) {
        preis = preis-(preis*rabatt)
    } 
    return preis;
}   
~~~

Mutation wird vom Testtool automatisch eingefügt  : 
```java
float berechnePreis(preis, rabat, bestelldatum ,rabattZeitraumBeginn ,rabattZeitraumEnde){
    if ( preis < rabatminimum AND bestelldatum >= rabattZeitraumBeginn AND  bestelldatum <= rabattZeitraumEnde ) {
        preis = preis-(preis*rabatt)
    } 
    return preis;
}   
```

## Ich hab noch nie TestFirst gemacht, wie komme ich dahin?
1. mache ein paar "Trockenübungen" also Übungsaufgaben abseits von realem Produktionscode, aber mit den gleich Sprachen/Tools wie deine Produktionsumgebung 
    * Beispiele ???
    * mache die Trockeübung öfters, immer wieder, bis es dir flüssig von der Hand geht.
    * du merkst: in jeder Iteration wirds du nicht nur schneller, sonder dein Code bekommt mit jeder iteration auch eine bessere Struktur, wird kürzer und besser für andere verständlich.
1. in der Produktionumgebung: fange an gute Test-Last Tests zu schreiben. Prüfe deren Testabdeckung, verwende Mutation-Testing.
1. Organisiere oder nehme teil an Coding Dojos für Test-First
1. beginne auch in Produktionumgebung mit TestFirst.

EVTL: nochmal Literaturzitate hier einbauen  ???

## Anmerkungen fürs nächste mal: Beispiele einbauen.








