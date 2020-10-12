---
title: "TDD? aber richtig!"
date: 2020-10-09
categories:
  - blog
tags:
  - TDD
  - Test Driven Development
toc: true
classes: wide
---
# >>TDD<< und  >>Test First<< 

Vorweg eine Frage: Sind wir uns einig, dass Unittests mit angemessener
Testabdeckung sehr wünschenswert sind ? (Es geht hier zunächst mal nur
um Unittests, nicht um Integrationstests oder um Akzeptanztests oder der
gleichen)
 
- Wenn ja: Gut, dann ist diese Hürde ja schon mal aus dem Weg geräumt.
- Wenn nein, dann .....[^1]

## Was **GENAU** sind >>Unittests<< ?? 

Mit Unittests meine ich hier immer "White Box" - Tests die immer automatisiert sind.
* Whiteboxtest: derjenige, der den Test schreibt oder plant,  kennt immer auch die Internas der Test-Klasse(n) (andernfalls wäre es ja ein "Black-Box-Test")

## Testabdeckung ist sehr wichtig, richtig ?  
Ich halte die Testabdeckung im Sinn von 'x %' der Codezeilen ehr für fast nebensächlich. Auf keinen Fall darf sie als Hauptkriterium für die Qualität der Tests missverstanden werden. Ich kann dir mühelos eine 100% Testabdeckung erzielen, ohne dass ich auch nur jemals einen Fehler damit finde. 

## Was ist >>Test Driven Development<< ?
Mit geht es hier um TDD im Sinne von z.B.  dem Buch "[Test Driven Java Development](https://www.packtpub.com/product/test-driven-java-development-second-edition/9781788836111)".[^2] 

Nämlich: **TEST FIRST**

# Warum ist >>Test First<<  entscheidend? 

* **Test first** zwingt vor dem Schreiben des eigentlich Code und der eigentlichen Unittests dazu,  sehr klar über die Anforderungen und das Softwaredesign (auf Klassen/Interface- Ebene) nachzudenken
* **Test first** trägt dann fast automatisch zu einer klareren Softwarearchitektur auf Klassen/Interface- Ebene bei. 
* **Test zuerst** zu schreiben geht nur , wenn ich genau die Anforderungen verstanden und wenn ich genau verstanden habe wie sich mein neuer Code in den bestehenden einfügen soll 
* **Test first** Code braucht weniger spätes  Refactoring (also Refactoring dessen Notwendigkeit erst später offensichtlich wird)
* **Test first** führt zu kleineren Klassen und Methoden, förder automatisch das [Single-Responsibility-Prinzip](https://de.wikipedia.org/wiki/Single-Responsibility-Prinzip)
* **Test first** spart am Ende Zeit und liefert höhere Code-Qualität

## Was ist falsch mit "test last" ?
* **Test first** - denken zu lernen ist schwer und kostet erstmal Zeit
* **Test first** lässt sich vor allem in altem Legacy-Code kaum nachträglich einführen und schon gar nicht kann man mit Legacy-Code neu lernen.
* **Test first** spielt in der Ausbildung oder Studium nach wie vor kaum eine Rolle

# Beweise , Beweise !

ok, beweisen im strengen Sinn lässt sich das vieleicht nicht ohne weiteres, aber es gibt doch eine größere Zahl an [Vergleichsstudien zum Thema TDD](../Literaturrecherche-TDD)! 

# Meine persönliche Erfahrung mit TDD:

-   es macht mir einfach viel mehr Spaß so zu programmieren
-   mit dem konsequenten "test first"-Ansatz von TDD ergibt sich ein
    geringerer Zeitaufwand gegenüber nachträglich gebauten Unittests:
    -   Weil ich dann während des Schreibens der eigentlichen
        Klasse/Methode ja keine **manuellen** Tests mehr mache.
    -   Denn: wenn ich noch keinen Unittest habe, wie teste ich eine
        Klasse/Methode die ich grad geschrieben oder verändert hat?
        durch bloßes hinschauen (ist fehleranfällig) oder durch
        manuelles Testen, das kostet jedes mal wieder Zeit!
    -   Weil ich gedanklich praktisch gleichzeitig eigentlichen Code und TestCode erfinde, ich bin also beim Schreiben des Tests schon gedanklich in der Thematik drin bin.
    -   Schreibe ich dagegen den Unittest erst später, dann muss ich
        mich ja ins Thema erst wieder neu eindenken. Schlimmstenfalls
        müsste ich sogar meine Klassen/Methoden-Design ändern, was ich
        natürlich im nach hinein eher nicht mehr mache.
-   Ich habe keinen Zeitdruck mehr beim "nachziehen" von Test: leider ist es nicht selten, dass nachträglich geschriebene Unittests von mindere Qualität ist, obwohl doch die Testabdeckung-Metrik hoch ist, oder schlimmer, dass die Tests ganz "vergessen" werden, weil:
    -   der Sprint schon vorbei ist
    -   der PO oder der Kunden mit neuen Featurewünschen drängt

-   Nochmal zur manchmal so heiligen **Testabdeckung**: Ehrlich gesagt ist mir die komplett egal wenn ich "test first" mache ! Denn: ich weiß ja von vornherein, dass ich alle Methoden in allen Klassen, die auch nur minimale Logic enthalten, mit Unittests zu 100% abgedeckt habe. Ob die gesamte Testabdeckung dann bei 80, 90 oder 95 % liegt (weil halt Glue-Code ohne Logik und Setter/Getter nicht abgedeckt sind), ist doch dann komplett irrelevant.
-   Falls ich in meinen Unittests doch mal einen Fall vergessen habe, der dann im Integrationstest oder noch später aufgedeckt wird, dann und nur dann ziehe ich zuerst den Unittests nach und dann **und erst da nach** fixe ich den eigentlichen Code.

## TDD/Unittest finde ich sehr schwer, wenn  ...  

-   wenn es schon nennenswert Codeteile gibt, die ohne Unittests sind
-   und wenn gerade diese Codeteile geändert werden müssen
-   wenn es nicht einfach möglich ist, neue Features mit komplett neuen Klassen/Modulen zur realisieren, sondern alte Klassen erweitert
werden müssen.

## Denn unter solchen widrigen Randbedingungen..
-   ..ist TDD extrem mühsam: ich muss mich in Codeteile von anderen Entwicklern reindenken, ohne Unittests und ohne Doku. Das ist das doppelt schwer
-   und solchen Randbedingungen ist TDD extrem zeitaufwändig ohne vor allem ohne unmittelbaren Gewinn für PO und Kunden.

Übrigens: das heißt dann logischerweise auch, dass es keinen Sinn macht TDD an einem Projekt mit kaum Unittests **neu lernen** zu wollen. Denn das geht ziemlich sicher schief.

Wer sich an so einem "dicken Brett" mit TDD versuchen will, der muss
schon sehr TDD-Sattelfest sein und die Randbedingungen (Zeit, Geld)
müssen außerdem sehr optimal sein.

## Wo ich TDD schwierig finde, es aber gerne besser machen möchte 

-   bei (Script) - Code, der direkt auf betriebssystemnahen Funktionen
    operiert
-   beim Testen von Networking oder bei DB- Code

Also , wenn es nur schwer gelingt, die externen Objekte (z.B.
betriebssystemnahen Funktionen) sinnvoll zu mocken.

[^1]: ...bin ich auch ratlos...
[^2]:  Die Grundidee ist auch abseits von Java in anderen Programmiersprachen die gleiche. 