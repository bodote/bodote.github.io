---
title: "TDD Beweise"
date: 2021-09-07
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

# Teil 3: Beweise, Beweise

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

[^1]: Kent Beck: Extreme Programming Explained. Embrace Change., Addison-Wesley, 2000, ISBN 0-201-61641-6. Kapitel 18 https://books.google.de/books?id=G8EL4H4vf7UC&lpg=PR9&ots=jbvErnnRBq&dq=%22We%20will%20write%20tests%20before%20we%20code%2C%20minute%20by%20minute.%22&hl=de&pg=PA115#v=onepage&q=%22We%20will%20write%20tests%20before%20we%20code,%20minute%20by%20minute.%22&f=false
[^2]:
    SOLID steht für : Single Responsibility (SRP), Open/Close, Liskov's Substitution, Interface Segregation, and Dependency Inversion.
    The SOLID concepts are:
    The **Single-responsibility principle**: "There should never be more than one reason for a class to change."[5] In other words, every class should have only one responsibility.[6]
    The **Open–closed principle**: "Software entities ... should be open for extension, but closed for modification."[7]
    The **Liskov substitution principle**: "Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it".[8] See also design by contract.[8]
    The **Interface segregation principle**: "Many client-specific interfaces are better than one general-purpose interface."[9][4]
    The **Dependency inversion principle**: "Depend upon abstractions, [not] concretions."[10][4]
    The SOLID acronym was introduced later, around 2004, by Michael Feathers.[11]
