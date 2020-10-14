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

Vorweg eine Frage: Sind wir uns eigentlich einig, dass Unittests mit angemessener
Testabdeckung sehr wünschenswert sind ? (Wobei es mir hier tatsächlich erstmal **nur**
um Unittests geht, nicht um Integrationstests oder um Akzeptanztests oder der
gleichen)
 
- Wenn ja: Gut, dann haben wir diese Hürde ja schon mal aus dem Weg geräumt.
- Wenn nein: Weil Ihr Unittests nicht für wichtig hälst oder das  das Messen der Testabdeckung ? [^1]

## Was **GENAU** sind >>Unittests<< ?? 

Mit Unittests meine ich hier immer "White Box" - Tests,  die außerdem immer automatisiert sind.
* Whiteboxtest heißt ja: derjenige, der den Test schreibt oder plant,  kennt immer auch die Internas der zu testenden Klasse(n) (andernfalls wäre es ja ein "Black-Box-Test")

## Testabdeckung ist sehr wichtig, richtig ?  
Na ja, ich halte die Testabdeckung im Sinn von 'x %' der Codezeilen ehr für fast nebensächlich. Weil, wenn Ihr sie als Hauptkriterium für die Qualität der Tests missverstehst, da bin ich wirklich anderer Meinung. Ich kann euch nämlich mühelos eine 100% Testabdeckung erzielen, ohne dass ich auch nur jemals einen Fehler damit finde. Wie? Indem ich einfach alle "assert..." Statements im Unittest vergesse. 

## Was ist >>Test Driven Development<< ?
Mit geht es hier um TDD im Sinne von z.B.  dem Buch "[Test Driven Java Development](https://www.packtpub.com/product/test-driven-java-development-second-edition/9781788836111)".[^2] Gibt natürlich viele andere Bücher Tutorials und ONline-Kurse zum Thema.

Also das wichtige und entscheidende ist für mich das  **TEST FIRST** Prinzip. Daher kommt ja auch das **DRIVEN** in TDD.

#  >>Test First<<  ist deswegen entscheidend, weil... 

* **Test first** zwingt vor dem Schreiben des eigentlich Code und der eigentlichen Unittests dazu, sich sehr klar über die Anforderungen und das Softwaredesign und zwar auf Klassen/Interface- Ebene Gedanken zu machen.
* **Test first** trägt dann fast automatisch zu einer klareren Softwarearchitektur auf Klassen/Interface- Ebene bei. 
* **Test zuerst** zu schreiben geht aber nur, wenn ich nicht nur die **fachlichen** Anforderungen genau verstanden sondern, wenn ich auch genau verstanden habe wie sich mein neuer Code in den bestehenden einfügen soll. Ich bin also gezwungen, mir vor der ersten Codezeile die ich schreibe, mehr Gedanken zu machen.
* **Test first**- Code braucht meiner Erfahrung nach weniger späteres  Refactoring (also Refactoring dessen Notwendigkeit erst in einem späteren Entwicklungszyklus oder in einem späteren Sprint offensichtlich wird)
* **Test first** führt zu kleineren Klassen und Methoden, fördert automatisch das [Single-Responsibility-Prinzip](https://de.wikipedia.org/wiki/Single-Responsibility-Prinzip), damit meine ich, kleinere Klassen und kleinere Methode die von weniger anderen Klassen abhängen. Ich hoffe euch ist klar, dass das was sehr gutes ist. 
* **Test first** spart am Ende halt doch Zeit und liefert höhere Code-Qualität.

## Das Gegenteil von **Test First** ist ja dann "test last"
Also die Frage ist ja, warum wird "test last" so häufig praktiziert? obwohl man mit "test last" kaum die gerade genannte Vorteile erzielt.
Ich denke das liegt daran, dass ...
* **Test first** - zu denken halt erstmal sehr schwer zu lernen ist und es kostet einiges an Zeit um das zu lernen.
* **Test first** lässt sich vor allem in altem Legacy-Code kaum nachträglich einführen und es macht schon gar keinen Sinn **Test First** im Umfeld von altem Legacy-Code neu lernen zu wollen, das geht aus meiner Erfahrung schief. Ja und...
* **Test first** spielt leider in der Ausbildung oder Studium nach wie vor kaum eine Rolle, gleiches gilt für die meisten Fachbücher und Tutorials
* also **Test First** kann/muss  man daher leider also erst immer "zusätzlich" lernen, nachdem man die jeweilige Programmiersprache oder Framework schon quasi "falsch" nämlich "test last" gelernt hat. Das macht es Neulingen leider zusätzlich unnötig schwer.

Ich behaupte, wenn man jede neue Programmiersprache oder jedes neue Framework von vornherein mit **Test First** lernen würden, würde es viel mehr praktiziert und wäre einfach viel selbstverständlicher.

Jetzt könnt Ihr sagen: "Der Bodo kann uns viel erzählen, wo sind die Beweise?"
# Beweise , Beweise !

ok, beweisen im strengen mathematische Sinn lässt sich das nicht ohne weiteres. ABER: es gibt doch eine größere Zahl an [Vergleichsstudien zum Thema TDD und andere interessante Zitate](../Literaturrecherche-TDD)! die ich für euch recherchiert habe. 

Wer jetzt schon überzeugt ist, der kann sich die restlichen 10-15 min sparen. 

Bevor Ihr geht, fragt Ihr euch wahrscheinlich , wie geht's jetzt weiter ?
Der kurze Termin sollte ja erstmal das Thema nur anteasern. 
Die Frage ist dann, wie groß ist bei euch das Interesse und die Bereitschaft Zeit in das Thema zu stecken? und vor allem wann wollt Ihr das dann machen? 

So. Und alle die von euch die noch nicht überzeugt sind, lade ich jetzt ein mit mir meine [Fundstellen zu TDD](../Literaturrecherche-TDD) durchzugegen. Wie gesagt so ca 10-15 minuten.



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

[^1]: Unittests sind gut und richtig, aber die Qualität von Unittest an der Testabdeckung zu messen halte ich für falsch.
[^2]: Die Grundidee ist auch abseits von Java in anderen Programmiersprachen die gleiche. 
