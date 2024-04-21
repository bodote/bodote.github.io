---
title: "TDD Blog Teil 3: Beweise etc."
date: 2021-09-09
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

Siehe auch:

[TDD Teil 1: Warum Test Driven Development?](../TDD-TestFirst-Teil1-Warum)

[TDD Teil 2: Architektur und Test Driven Development](../TDD-TestFirst-Teil2-Architektur)

# Beweise, Beweise!

So jetzt könnt ihr sagen: Der Teichmann kann uns ja viel erzählen, stimmt das denn überhaupt und funktioniert das in der Praxis ?

Ich hoffe, dem Leser ist klar, dass es Beweise im streng mathematischen Sinn nicht geben kann. Also sorry für diese Clickbait-mäßig Überschrift.

Trotzdem: Die Frage ist, lassen sich meine Behauptungen belegen? Welche Erfahrungen haben andere mit TDD/TestFirst gemacht?
Da findet man doch eine Menge Indizien, die dafür sprechen:

Es gibt da ganz verschiedene Arten von Belegen, wie gut TDD und Test - First wirklich in der Praxis ist:

- Bücher über TDD selbst, werden immer wieder neu herausgebracht. Kent Becks Buch ist also beweitem nicht das einzige zu dem Thema.

- Bücher über Softwarearchitektur z.B.

- eine Reihe von wissenschaftlichen Studien, z.T. sogar richtige Vergleichsstudien

- eine Reihe von systematischen Erfahrungsberichten aus verschiedenen großen Unternehmen.

- sogar einige Metastudien zu dem Thema konnte ich finden.

## Die Indizien

Im Folgenden nur ein Auszug aus den interessantesten Fundstellen, die ich recherchiert habe. Die vollständige Liste aller meiner Fundstellen findet sich [hier](../Literaturrecherche-TDD.)

- ["The Spring team advocates test-driven development,TDD ."](https://docs.spring.io/spring-framework/docs/current/reference/html/testing.html)

  > "Das Spring Team unterstützt und beführwortet TestDrivenDevelopment.

- ["VMware Pivotal Labs Website](https://tanzu.vmware.com/content/blog/go-faster-write-tests-first)

  > "Wir praktizieren selbst TestDrivenDeveopment. Da heißt, bevor wir die Arbeit an einem neuen Feature beginnen, schreiben wir zuerst einen Test, der das gewünschte Verhalten genau beschreibt."

- [IBM: Assessing test-driven development](https://collaboration.csc.ncsu.edu/laurie/Papers/MAXIMILIEN_WILLIAMS.PDF)

  > **50% weniger Bugs** als bei "test last", minimaler geringere Produktivität

- [Microsoft: Evaluating the Efficacy of Test-Driven Development: Industrial Case Studies](https://d1wqtxts1xzle7.cloudfront.net/36509027/fp17288-bhat.pdf?1423032149=&response-content-disposition=inline%3B+filename%3DEvaluating_the_Efficacy_of_Test_Driven_D.pdf&Expires=1599907639&Signature=RuaKEjh7AbrkimLa5LGjb6zOpojv18srJrYQO7ONLNjWm586g6nxlDjGnYgubwIFYYp5fNkQulFn6YD3wpvud5bBhvwkO4nOOFMYyhATLdvHjHtW3vzm6ncsuqgwYTIKtrxbxAd7lQiEiue~D300FsgSLK6ZUk9DOssTqS0NZry6syc9I6IQYR6H2BRcnzf9oxvCTBWPzjSEBPi2cqYpyKbF1Y322XtLj7fdNTu8IVkmUULxwH3R1GVsEZrdpOAOJpM0b1ZAsJZEI0K3hiv~ENiV79hUjoyRu5xLaDeDWA4Nhg4Q-J8Zu8UQ18hQEjl0dOZnq7o4Xq~2-8jbuzDxIQ__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA)

  > **Bugrate sinkt mit TDD um 62%-77%** , 15% -35% mehr Zeit für TDD notwendig.

- [Metastudie, die 6 unterschiedliche andere Studien ausgewertet hat](https://digitalcommons.calpoly.edu/cgi/viewcontent.cgi?article=1027&context=csse_fac)

  > Ergebnis: deutlich **Positiv, auch bezüglich Software-Architektur**

- [An Experimental Evaluation of the Effectiveness and Efficiency of the Test Driven Development](https://ieeexplore.ieee.org/abstract/document/4343756)

  > **deutlich bessere Gesamt-Produktivität und Codequalität**

- [noch eine Metastudie](https://www.researchgate.net/profile/Burak_Turhan/publication/258126622_How_Effective_is_Test_Driven_Development/links/54e794320cf27a6de10a8afe/How-Effective-is-Test-Driven-Development.pdf)

  > Gesamturteil deutlich positiv, aber Hinweis: "schwer zu meistern" , **Fazit: Empfehlung für TDD**

- [Empirische Studie zu Test-Driven Development](https://link.springer.com/book/10.1007%2F978-3-642-04288-1)
  > " _Test First_ ist **besser** darin, **lose gekoppelte** Softwarekomponenten hervorzubringen als _test last_." _Lose gekoppelt_ bewirkt zum Beispiel bessere Wartbarkeit, Verständlichkeit für die Entwickler, ist also was sehr gutes.

[mehr Details hier](../Literaturrecherche-TDD)

# Was ist TDD eigentich praktisch gesprochen?

.. und was meint Kent Beck mit "We will write tests before we code, minute by minute."?
Die lange Antwort liest du am besten selbst direkt im Buch nach.[^1]

## TDD sind das Gleiche wie Unittests, richtig ?
**Falsch!**

- Die Basis von TDD sind **NICHT** Unit-tests wie sie Wikipedia beschreibt[^5]. Insbesonders der Aspekt der Forderung nach **"Isolation"** eines Tests hat viel **Verwirrung** gestiftet: 
  - Zwar sollen verschiedenen Tests voneinander soweit **"isoliert"** sein, dass sie sich nicht gegenseitig beeinflussen, (z.B. darf es nicht von der Reihenfolge der Ausführung der Tests abhängig sein, ob ein Test erfolgreich läuft)
  - in TDD sollte man sich für einen Tests auch immer eine einzelnen möglichst atomaren Aspect, Requirement, Akzeptanzkriterium, oder wie auch immer du das nenenn willst beschränken
  - aber das heißt ausdrücklich NICHT, dass man nur eine Klasse oder eine Methode testen soll und alls Abhängigkeiten (dependencies) "weg-mocken" soll. 
  - vielmehr sollten **"Mocks"** sehr sparsam, mit Bedacht und und nur dort eingesetzt werden, wo es unbedingt nötig ist: 
    - im wesentlich müssen nur extern aufgerufene REST - Services gemockt werden 
    - evtl. wird manchmal auch die Datenbank gemockt, wenn ansonsten die Test zu langsam laufen würden, oder es zu schwierig erscheint, eine zum Testrunner lokale Datenbank zu instanzieren.
    - notfalls kann im Ausnahmefall auch mal ein zum Projekt gehörendes Modul gemock werden, wenn es eine sehr lange Laufzeit aufweist (z.B. lang laufende Berechnungen), denn das Ziel für automatische Tests ist schnelles Feedback für den Entwickler
- Hingegen ist es sogar erwünscht, dass ein einzelner TDD-Test z.B. für ein Spring - Backend den Rest-Controller zusammen mit "seinem" Service, und ggf. zusammen mit dessen DB-Repository testet (für letzeres verwende "Testcontainers" oder "embedded" DBs). 
- das "Interface" für einen Test ist immer die "öffentliche" und hoffentlich stabile API. **Stabil** heißt, dass sich die API nur selten ändern sollte. 
- teste **NIE** die Internas des Codes. Warum ? weil das zu enge Koppeln von Tests an die Internas des Codes zu fragilen/instabilen Test führt, die umfassendes Refaktoring verhindern und daher beim Refactoring auch geändert werden müssten.
- Tools wie "Junit", "Mockito", "jasmin" etc. können und sollen eingesetzt werden, solange man obige Regeln beachtet.
- Der eigentliche Witz ist aber vor allem: Wir schreiben den Test **BEVOR** wir den Code für die eigentlich nützliche Unit schreiben.
- Wenn man sich strickt an das Test-First Prinzip hält und wirklich immer nur das Implementiert, was der Test vordert muss das automatisch zu einer sogenannte **"Testabdeckung"** von **100%** führen. Auf die "Testabdeckung" gehen wir weiter unten noch ein.

(Abschnitt überarbeitet im April 2024)

## Was sich erst mit viel Praxis erschließt

Leider sieht der Product Ower, Scrum Master oder der noch nicht so erfahrene Entwickler an so einem einfachen Beispiel noch nicht, wie sich TestFirst auf die Softwarearchitektur auswirkt. Das offenbart sich nach meiner Erfahrung erst dann, wenn man wirklich komplexte Anforderungen programmiert und der Code einen gewissen Umfang an verschiedenen Klassen hat.

Das heißt für euch: wenn Ihr selbst die Erfahrung machen wollt, dann müsst ihr leider den langen Weg gehen. Es gibt keine Abkürzung Dazu passt auch prima das Zitat aus dem "Test-Driven Java Developmeht" - Buch unten.

> \"It\'s not an easy thing to master TDD. Even after learning all the
> theory and going through best practices and anti-patterns, the journey
> is only just beginning. **TDD requires time and a lot of practice**. It\'s a
> long trip that does not stop with this book. As a matter of fact, it
> never truly ends. There are always new ways to become more proficient
> and faster. However, even though the cost is high, the benefits are even
> higher. **People who have spent enough time with TDD claim that there is
> no other way to develop a software.** We are one of them and we\'re sure
> that you will be too.\"[^3]

Meine Überzeugung ist, das den sehr guten Softwareentwickler von dem Gewinner der Championsleague trennt, ist, unter anderem TDD zu beherschen. (..um auch mal einen Vergleich aus dem Fußball zu bemühen)

# Die häufigsten Fragen

## Warum findet man so wenige Programmierer die das tatsächlich tun ?

oder anders gefragt: **Warum ist das eigentlich sooo schwer?**
Ist es wirklich sooo schwer ? Eindeutig ja!

- Zitat aus aus [Large-Scale Scrum >>LeSS<<](https://less.works/de/less/technical-excellence/test-driven-development):

  > "Wir treffen **selten** Entwickler, die in der Lage ware, sich TDD/TestFirst selbst beizubringen. Die meisten Entwickler brauchen **tage- oder gar wochenlanges** Pair-Programming, bis sie es können."

  und weiter :

  > "Test-Driven Development ist vermutlich die **schwierigste** agile Praxis, aber TDD ist gleichzeitig die einer der **größten Gelegenheiten** die Qualität und das Design des Codes zu verbessern.

- [Metastudie: How Effective is Test-Driven Development?](https://www.researchgate.net/profile/Burak_Turhan/publication/258126622_How_Effective_is_Test_Driven_Development/links/54e794320cf27a6de10a8afe/How-Effective-is-Test-Driven-Development.pdf) :

  > "Fast alle \[Studien\] sind sich einig, dass **TDD schwierig zu lernen** ist.

- Aus [Test-Driven Java Development - Second Edition](https://www.packtpub.com/product/test-driven-java-development-second-edition/9781788836111)
  > "It\'s not an easy thing to master TDD. Even after learning all the theory and going through best practices and anti-patterns, the journey is only just beginning. **TDD requires time and a lot of practice**. It\'s a long trip that does not stop with this book.

## Wie kann ich als Softwareentwickler mich in kleinen Schritten inkrementell von Test Last zu Test First vorarbeiten ?

### Zunächst klären wir ein paar Vorraussetzungen.

Sind wir überhaupt in der Situation, TDD mit 'test first' gerade anwenden zu können ?

Nehmen wir an, wir wären ein SWEntwickler in einem Team
irgend jemand hat sich schon über das Gesamtkonzept den Kopf zerbrochen und eine Software-Architektur entworfen und diese uns soweit erklärt, dass wir ein grobes Verständniss dafür haben.
Wir sollen jetzt ein neues Feature implementieren, wofür wir aller Vorraussicht mindestens eine neue Klasse, Komponente, oder Service oder ähnliches benötigen.
wir müssen zwar auch bestehenden Code ändern, aber der neu zu schreibende Code überwiegt auf jeden Fall. Idealerweise gibt es schon irgendein Unittest-Framework im Projekt, auch wenn das bisher nur zum "Test Last" eingesetzt wurde.

### Im Gegensatz dazu: wann ist TDD nicht der richtige Ansatz?

Wo macht TDD weniger Sinn ?
[Nochmal der Meister Beck selbst ab 51:26](https://youtu.be/FlJN6_4yI2A?t=3084)

TDD/TestFirst macht unter folgenden Vorraussetzungen eher weniger Sinn.
Diese Punkte zu kennen , ist wichtig um Misserfolg bei der Anwendung von TestFirst zu vermeiden.

- ein großes Projekt ohne jegliche automatischen Tests

- nur minimale Kenntnis der eingesetzten Sprache/Framework/Testframework

- Architektur ist unklar.

- die Hauptarbeit ist rauszufinden, welche 2 Parameter geändert werden sollen, damit die neue Anforderung erfüllt wird, kaum oder gar keine neuer Code zu schreiben

- sehr große Skepsis bis Ablehnung im Kollegenkreis, keine Unterstützung durch PO/Scrummaster/Architekt

### HTML-Templates und TDD

Bei HTML-Templates (z.B. für SinglePageApplications) wie sie in Angular oder React vorkommen funktioniert der klassische TDD nicht. Aber es gibt ein speziell für diesen Fall angepasstes TDD: [Visual TDD](https://storybook.js.org/tutorials/visual-testing-handbook/react/en/vtdd/).

Grundidee basiert darauf, dass "Visual Testcases" mit einem Tool wie [storybook](https://storybook.js.org/) erstellt werden "visuell" vom Entwickler (oder jedenfalls einem Menschen) einmalig geprüft und für ok befunden werden und dann davon ein Snapshot (in form eines PNGs ) automatisch erstellt wird. Bei jedem folgenden Testdurchlauf werden dann die Snapshots mit denen im git eingechecken verglichen und bei Abweichungen muss wieder ein Mensch prüfen ob hier ein Fehler vorliegt, oder die Änderung ok ist.

## Ich hab noch nie TestFirst gemacht, wie komme ich dahin?

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

# Bonus Content:

## Testabdeckung messen ?

- Ja, aber nur wärend des schreibens der Tests, um Lücken in der Testabdeckung zu finden. ![testCoverage](/assets/images/testCoverage.png){:height="360px" width="360px"}

- NEIN, um Qualitätsaussagen über die gesamte Codebasis zu machen

  - weil es gibt Code der nicht sinnvoll zu testen ist, z.B. weil er keine Fallunterscheidungen oder Schleifen enthält. Hier nachträglich die Testabdeckung zu erhöhen macht die Codebasis in der Regel nicht besser.

- Beispiel : \[TBD\]

## noch besser: Mutation-Testing, hilft auch bei Test-Last!

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

# Weitere Interessante Links zum Thema:

- [Wenn Tests schwer zu schreiben sind, dass sagt das was aus über die Qualität unserer Softwarearchitektur: das stimmt was nicht!](https://www.youtube.com/watch?v=UWtEVKVPBQ0):

- [Tdd Antipatterns](https://web.archive.org/web/20100105084725/http://blog.james-carr.org/2006/11/03/tdd-anti-patterns/)

- [Developers don't use TDD](https://www.javacodegeeks.com/2018/02/developers-dont-use-tdd.html)

---

Fußnoten:

[^1]: [Kent Beck: Extreme Programming Explained. Embrace Change., Addison-Wesley, 2000, ISBN 0-201-61641-6. Kapitel 18](https://books.google.de/books?id=G8EL4H4vf7UC&lpg=PR9&ots=jbvErnnRBq&dq=%22We%20will%20write%20tests%20before%20we%20code%2C%20minute%20by%20minute.%22&hl=de&pg=PA115#v=onepage&q=%22We%20will%20write%20tests%20before%20we%20code,%20minute%20by%20minute.%22&f=false)
[^2]:
    SOLID steht für : Single Responsibility (SRP), Open/Close, Liskov's Substitution, Interface Segregation, and Dependency Inversion.
    The SOLID concepts are:
    The **Single-responsibility principle**: "There should never be more than one reason for a class to change."[5] In other words, every class should have only one responsibility.[6]
    The **Open–closed principle**: "Software entities ... should be open for extension, but closed for modification."[7]
    The **Liskov substitution principle**: "Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it".[8] See also design by contract.[8]
    The **Interface segregation principle**: "Many client-specific interfaces are better than one general-purpose interface."[9][4]
    The **Dependency inversion principle**: "Depend upon abstractions, [not] concretions."[10][4]
    The SOLID acronym was introduced later, around 2004, by Michael Feathers.[11]

[^3]: [Was ist ein Unit-Test?](https://www.it-agile.de/agiles-wissen/agile-entwicklung/unit-tests/)
[^4]: [Test-Driven development by Example von Kent Beck](https://www.amazon.de/dp/8131715957/ref=cm_sw_em_r_mt_dp_B70TB8B67MC0XC1VV2CV)
[^5]: [Unit testing](https://en.wikipedia.org/wiki/Unit_testing)
