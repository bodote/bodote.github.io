---
title: "Warum ECHTES Test Driven Development und Wie komme ich dahin?"
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
classes: wide
---

# Teil 2 Softwarearchitektur und TDD

## Ebenen der Softwarearchitektur im Vergleich

Zunächst ein Wort zu den verschiedenen Ebenen von Softwarearchitektur:
Wie beim Bauen von Gebäuden gibt es ja auch in der Software oder allgemein in der IT-Sytsem-Architektur verschiedenen Ebenen, die ich jetzt willkürlich so definiere: 1. Ebene: Wie sieht mein Stadtteil aus in dem die Gebäude stehen, wie sind die Straßen, Gehwege, Parks und Gebäude insgesamt organisiert? 2. Ebene: Wie schaut die Fassade aus, und wie ist die Aufteilung in den Gebäuden? z.B. Büros, große oder kleine Wohnungen 3. Ebene: Wie sind die Wohnungen aufteilt, z.b. wie groß ist das Wohnzimmer im Vergleich zur Küche 4. Ebene: bis hin: welchen Bodenbelag hab ich wo, Welche Lichtschalter an der Wand , welche Türgriffe?

- Wenn wir diese 4 Ebenen auf Softwarearchitektur übertragen und das auf TDD anwenden, dann hilft TDD eher bei den untern beiden Ebenen 3 imd 4, also bei der Architektur der kleineren Details, weniger bei den obern beiden Ebenen 1 und 2, der Architektur im ganz Großen.

## TDD und Softwarearchitektur Behauptung

- So, die Behauptung die jetzt im Raume steht, ist also, dass TDD/TestFirst bei der Softwarearchitektur der untern beiden Ebenen massiv hilft und auch hift über längere Zeiträume diese Architektur positiv beeinflusst.

- Im Gegensatz dazu, helfen nachträglich hinzugefügte automatische Tests zwar für die Softwarequalität im Sinne von Stabilität und Fehlerarmut. Nachträglich hinzugefügte automatische Tests helfen aber gar nicht für die Softwarearchitektur, für keine der 4 Ebenen.

## Probleme der Softwarearchitektur ohne TDD

- Bei Software die von mehrköpfigen Teams gebaut werden, ist es wichtig, dass nicht nur der ursprüngliche Autor eine Methode oder Klasse leicht versteht, und auch nach Wochen und Monate noch versteht.

- Denn Software, die wirklich benutzt wird, muss eben immer wieder an neue Anforderungen angepasst werden und weiterentwickelt werden, da erzähle ich ja niemandem was neues.

- Wenn ich aber Softwareteile anpassen und erweitern muss, muss ich erstmal verstehen, was da bisher steht. Und zwar möglichst schnell.

- Genau hier kommt die Softwarearchitektur der unteren beiden Detailebenen ins Spiel.

  - ist die Softwarearchitektur für einen Entwickler schnell verständlich oder nicht ?
  - ist die Softwarearchitektur flexibel und leicht änderbar ?

Ein einfaches Beispiel: Wir haben in unserer Zooverwaltungssoftware bisher die Klassen "Ente", "Fisch", "Zebra".

- Der Zoodirektor möchte aber jetzt auch Pferde anschaffen.
- "Zebra" ist ja ein naher verwanter des Pferdes und kann rennen. Für eine schnelle Quick-and-Dirty Lösung könnte man ja die Klasse "Zebra" einfach in "Huftiere" umbenennen. Das funktioniert auch erstmal.
- später fällt dann unserem Zoodirektor ein , dass Pferde ja regelmäßig beschlagen werden müssen, somit müssen wir ein Datum fürs nächsten Beschlagen erfassen und auswerte.
  - was ist jetzt mit dem Zebra?
  - wir wollen wissen, wann das Pferd neu beschlagen werden muss. Das ist aber für Zebras irrelevant.

In all diesen Fällen bauen wir nicht nur neue Eigenschaften in die Klassen ein, sondern mit diesen Eigenschaften werden auch Ergebnisse berechnet. Da wir jetzt zu viele verschiedenen Tiere miteinander vermischt haben, haben wir jetzt innerhalb der Klassen komplexe Fallunterscheidungen. z.B. was geben wir als Ergebnis zurück wann wir bei Huftieren (wenn wir Zebras und Pferde jetzt so nenen wollen) neu Behufen müssen. Also: was ist das Datum für die Beschlagung bei einem Zebra ? : 1. Jan. 2099 ? in der Hoffnung das das Zebra bis dahin tot ist ?

Die Richtige Antwort ist: für Zebras darf es diese Methode gar nicht geben. Wir hätten die Huftiere in weitere Unterklassen aufteilen müssen und so schon über die Klasse die Unterscheidung treffen können. Das wäre dann bessere Architektur.
In realen Projekten sieht man aber solche Änderunge oft nicht, oder zumindest nicht rechtzeitig.

Das ist nur ein Beispiel wie Architektur verfällt und erodiert und das SOLID-Prinzip verletzt. Nach SOLID ist das Single Responsibility (SRP) das ersten von 5 Architekturprinzipien oder Architekturregeln.

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

# Teil 3: Beweise, Beweise Folie 20

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

## Im Gegensatz dazu: wann ist TDD nicht der richtige Ansatz?

Wo macht TDD weniger Sinn ?
https://youtu.be/FlJN6_4yI2A?t=3084 51:26

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

# Fußnoten:

[^1] Kent Beck: Extreme Programming Explained. Embrace Change., Addison-Wesley, 2000, ISBN 0-201-61641-6. Kapitel 18 https://books.google.de/books?id=G8EL4H4vf7UC&lpg=PR9&ots=jbvErnnRBq&dq=%22We%20will%20write%20tests%20before%20we%20code%2C%20minute%20by%20minute.%22&hl=de&pg=PA115#v=onepage&q=%22We%20will%20write%20tests%20before%20we%20code,%20minute%20by%20minute.%22&f=false
