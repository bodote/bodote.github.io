---
title: "Bodos unwissenschaftliche Argumente für TDD"
date: 2020-09-18T15:34:30-04:00
categories:
  - blog
tags:
  - TDD
  - Test Driven Design
---

Vorweg eine Frage: Sind wir uns einig, dass Unittest mit angemessener
Testabdeckung sehr wünschenswert sind ? (es geht hier zunächst mal nur
um Unittest, nicht um Integrationstest oder um Akzeptanztests und der
gleichen)
- Wenn nicht, dann gehe zurück auf LOS ...gehe direkt dort hin, ziehe
keine 4.000,- Euro ein\....oder so ähnlich. 
- Wenn ja: Gut, dann ist diese
Hürde ja schon mal aus dem Weg geräumt.

### Meine Motivation, TDD wo immer erlaubt und möglich einzusetzen, ist folgende: {#meine_motivation_tdd_wo_immer_erlaubt_und_möglich_einzusetzen_ist_folgende}

-   es macht mir einfach viel mehr Spaß so zu programmieren
-   ich bin sicher: mit TDD geschriebene Software bekommt ~~fast~~ schon
    automatisch eine bessere Architektur/Design, zumindest auf unterster
    Ebene (also für alle Klassen innerhalb eines Packages oder eines
    Modules )
-   mit dem konsequenten \"test first\"-Ansatz von TDD ergibt sich ein
    geringere Zeitaufwand gegenüber nachträglich gebauten Unittests:
    -   Weil ich dann während des Schreibens der eigentlich
        Klasse/Methode ja keine **manuellen** Test mehr mache.
    -   Denn: wenn ich noch keinen Unittest habe, wie teste ich eine
        Klasse/Methode die ich grad geschrieben oder verändert hat?
        durch bloses hinschauen (ist fehleranfällig) oder durch
        manuelles Testen, das kostet jedes mal wieder Zeit!
    -   Weil ich gedanklich praktisch gleichzeitig eigentlichen Code und
        TestCode erfinde, ich bin also beim schreiben des Tests schon
        gedanklich in der Thematik drin bin.
    -   Schreibe ich dagegen den Unittest erst später, dann muss ich
        mich ja ins Thema erst wieder neu eindenken. Schlimmstenfalls
        müsste ich sogar meine Klassen/Methoden-Design ändern, was ich
        natürlich im nach hinein nicht mehr mache.
-   Ich habe keinen Zeitdruck mehr beim \"nachziehen\" von Test: wir
    sind uns doch einig, dass wie wenigsten Menschen/Teams wirklich die
    Disziplin immer aufbringen die Tests \"nachzuziehen\" obwohl der
    -   Sprint schon vorbei ist
    -   der PO oder der Kunden mit neuen Feature wünschen drängt
-   Und die **Testabdeckung**: Ehrlich gesagt ist mir die komplett egal!
    Denn: ich weiß ja von vornherein, dass ich alle Methoden in allen
    Klassen, die auch nur minimale Logic enthalten, mit Unittests zu
    100% abgedeckt habe. Ob die gesamte Testabdeckung dann bei 80, 90
    oder 95 % liegt (weil halt Glue-Code ohne Logik und Setter/Getter
    nicht abgedeckt sind), ist dann komplett irrelevant.
-   hab ich in meinen Unittests doch mal einen Fall vergessen, der dann
    im Integrationstest oder noch später aufgedeckt wird, dann und nur
    dann ziehe ich zuerst den Unittest nach und dann **und erst dann**
    fixe ich den eigentlichen Code.

### Fast keine Motivation für TDD bringe ich auf \... {#fast_keine_motivation_für_tdd_bringe_ich_auf_...}

-   wenn es schon nennenswert Codeteile gibt, die ohne Unittests sind
-   wenn diese Codeteile geändert werden müssen
-   wenn es keine Option ist, neue Features mit komplett neuen
    Klassen/Modulen zur realisieren, sondern alte Klassen erweitert
    werden müssen.

\... ganz ehrlich: dann hab ich auch keine Lust auf TDD, denn das ist
dann nur noch frustrierender.

Denn dann ist TDD:

-   extrem mühsam: ich muss mich in Codeteile von anderen Entwickler
    reindenken, ohne Unittest und ohne Doku ist das doppelt schwer
-   extrem zeitaufwändig ohne unmittelbaren Gewinn für PO und Kunden
-   macht einfach keinen Spaß

Übrigens: das heißt dann logischerweise auch, dass es keinen Sinn macht
TDD an einem Projekt mit wenig Unittests neu lernen zu wollen, das geht
ziemlich sicher schief.

Wer sich an so einem \"dicken Brett\" mit TDD versuchen will, der muss
schon sehr TDD-Sattelfest sein und die Randbedingungen (Zeit, Geld)
müssen außerdem noch stimmen.

### Wo ich TDD schwierig finde, es aber gerne besser machen möchte {#wo_ich_tdd_schwierig_finde_es_aber_gerne_besser_machen_möchte}

-   bei (Script) - Code der direkt auf betriebssystemnahen Funktionen
    operiert
-   beim testen von Networking oder bei DB- Code

Also, wenn es nicht einfach gelingt, die externen Dinge (z.B.
betriebssystemnahen Funktionen) sinnvoll zu mocken.

### Die Wette {#die_wette}

Ich möchte mit euch eine Wette abschließen:

Ich wette, dass es keinem von euch gelingt im großen weiten Internet
eine Empfehlung eines SWentwickler, der sich ernsthaft und tief mit TDD
auseinandergesetzt hat, zu finden, die bei neuen (größeren,
nichttrivialen) Projekten ausdrücklich von TDD abrät.

Gegenprobe: es ist rel. leicht Aussagen zu finden, die von dieser oder
jeder SW-Technologie, Architekturstil, Programmiersprache etc.
ausdrücklich und auch begründet abraten. Außer bei TDD (angewendet bei
neuen Projekten) eben.
