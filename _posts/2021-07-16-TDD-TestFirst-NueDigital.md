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
Im Vortrag gehen wir dieser Frage gemeinsam auf den Grund. Auf dem Weg zu einer Antwort klären wir außerdem, was mit Test-driven Development und Test First überhaupt gemeint ist, untersuchen anhand vieler Beispielprojekte den Status Quo und tragen mit einem Blick in Literatur sowie einschlägige Studien die vielen nachgewiesenen Vorteile dieser Entwicklungsmethoden zusammen. Wir wollen Vorurteile abbauen und die wichtigsten Fragen rund um Test-driven Development beantworten: Warum ist Test First scheinbar so schwierig? Welche Vorteile verschenken wir, wenn wir rein auf Test Last setzen?  Wird Softwarearchitektur durch Test First wirklich besser? Welchen Unterschied genau macht es, die Tests vor der Implementierung zu schreiben statt im Nachhinein? Warum hat Test First automatisch einen sehr positiven Einfluss auf meine Softwarearchitektur, Test Last aber eher weniger?  Wie kommen wir von Test Last zu Test First? Und welche Fragen hast du zu dem Thema?  
# Timestamp: 0
# Short Teaser2:
## Ganz Gallien ist ...
## Die ganze Softwarewelt ist
.. von Agiliität und Scrum besetzt, nur ein kleines scheinbar unbedeutendes Kapitel in Kent Becks Buch aus dem Jahr 2000,  in dem er die Grundlagen zu Scrum gelegt hat, das umzingelt ist von TestAutomatisierung, TestLast und DomainDrivenDesign wiedersetzt sich nach wie vor der wirklich großen Verbreitung. Das Kapitel beschreibt Test Driven Development.
Warum ist das so ? Ist TDD wirklich eine so gute Idee? Warum wird es dann nicht überall eingesetzt?  In welchem Umfeld steigert es die Produktivität der Softwareentwicklung, in welchem Umfeld vieleicht ist es sogar contraproduktiv ? 

Genau darüber werden wir heute sprechen!
# Mein Name..
ist Bodo. 1980 begann ich mit meinem ersten Computer Sinclair ZX80 Software zu entwicklen.
Zunächst in Basic und Assember, später dann C, jetzt schon lange Java und in letzter Zeit auch Javascript.
# Willkommen
...zu "Test-driven Development?! Na klar … aber richtig!"
## Disclaimer
Also um hier gleich eins klar zu stellen: 
ich bin **kein Berater/Speaker/Buchautor** der von Konferenz zu Konferenz reist und sein tiefes Wissen mit immer neuen Varianten und Facetten zum Besten gibt. 

* Sondern, Ich hab mich in meiner bisherigen Berufslaufbahn auch etliche Jahre mit Themen befasst, bei denen ich nicht direkt selbst Software schreiben durfte. 

* Ich war nämlich unter **auch mal Abteilungsleiter**, bis mich **Scrum**, Scrumteam, Scrummaster und Product-Owner von meinem Leiden erlöst haben, sodass ich jetzt wieder **entwickeln** darf. 

## Mein Ziel:
ist, dass jeder von euch nach dem Vortrag rausgeht und sich sagt: hey, über dieses TDD muss ich mehr lernen, und ich muss gleichzeitig rausfinden, wo TDD angebracht ist, und wo nicht.

* Grundidee (ganz kurz nur Test first)
* Reputation des Erfinders, Studien, andere Anwender , also Beweise dass TDD eine gute Idee ist.
* Versteckete überraschende Vorteile (Softwarearchitektur)
* Grundidee (bischen ausführlicher)
* Passender Context/Unpassender Context für die Anwendung.

TDD ist ein großes Thema über das schon viele Bücher geschrieben wurde. Wir wollen uns heute anschaun, was unterscheidet TDD von anderen Arten der Testautomatisierung, wo kann TDD helfen, welche Argumente sprechen dafür und wer setzt es ein ?


## Warum beschäftigt mich TDD?
### (Kent Beck, "Extreme Programming")

 * Das Thema beschäftigt mich, seit ich so ums Jahr **2000** das Buch "Extreme Programming" von Kent Beck gelesen habe. 

 * In dem Buch war viel von den **Konzepten** die Rede, die später unter dem Namen "**Scrum**" bekannt wurden. 

 * Dazu muss man wissen: Kent Beck ist nicht **irgendein** Fachbuchautor, er ist einer DER Fachbuchautoren, Speaker auf allen einschlägigen Konferenze. 
    * Vor allem aber ist er **anerkannt** als einer DER Vordenker der Softwareindustrie.
    * Er hat die Art und Weise wie wir heute Software entwickeln wie kaum ein Anderer beeinfluss.
    * Er war maßgeblich am  **"Agile Manifest"** beteiligt, das **2001** publiziert wurde und damit eine wahre **Revolution** in der Softwarebranche ausgelöst hat.
    * Also, er ist tatsächlich einer der "**Erfinder**" von Scrum, wenn du so willst. Und inzwischen arbeitet praktisch **jeder** in der Softwareindustrie weltweit nach der Methode, oder zumindest **behaupet** praktisch jeder, dass er nach Scrum arbeite würde.
###### bis hierher auswendig ?

 * Also 2000 hatte ich das Buch gelesen. Aber der Inhalt war genau , was der Titel versprach. Nämlich **Extrem**. Für die meisten damals war es es vor allem aber **extreme** Unsinn. Wer hatte denn sowas schon mal gehört: die Entwickler sollten **paarweise** am gleichen Problem gemeinsam arbeiten!
 Mit kam das auch zumindest ungewöhnlich und überraschen vor.  

 * Aber in 2003: Als ich damals meinem **Kompangnion Joachim** von dieser Vision für eine bessere Methode der Softwareentwicklung  überzeugen wollte, hat er nur gesagt: "Wer **Visionen** hat sollte zum Arzt gehn"  (nur um dann ein paar Jahre später einzusehen, dass Kent Becks Ideen doch **extrem** brauchbar sind)

 * Also mit Scrum war erstmal **nix**, Anfang der 2000er Jahre! Aber da gab es ja noch Kapitel 18: Auf gerade mal **6 Seiten** erklärte Kent Beck, dass man Software automatisch testen sollte und sogar die Tests **VOR** dem **eigentlichen** Teil der Software schreiben sollte.

 * Zitat "We will write tests **before** we code, minute by minute. We will preserve these tests forever, and run them all together frequently. We will also derive tests from the customer's perspective."

    * Dazu wiederhole ich nochmal: Kent Beck ist **nicht irgendwer**, sondern einer **der** ganz großen **Vordenker** der **agilen Bewegung** und der Softwarebranche insgesamt. 
    * So, und wenn einer DER großen Vordenker der letzten 20 Jahre in der Branche eine Konzept wie TDD vorschlägt, dann darf man das auf jeden Fall **sehr ernst nehmen**, und es lohnt sich sicher, sich damit näher aueinanderzusetzten, oder?


 * **Zurück** zu mir ins Jahr **2000**. **Damals** war das allerdings alles andere als offensichtlich und Kent Beck war mit seinem Buch **einer unter vielen**, der halt ein paar **verrückt klingende Ideen** hatte.

 * Trotzdem das damals echt revolutionär und **für mich völlig neu** war, wollte ich das  gleich ausprobieren. Irgendwie war ich auch auf der Suche nach Ideeen, wie man besser als **bisher** Software entwickeln könnte.

 * Dabei hatte ich das Glück, dass ich damals gerade einen **neuen Job** hatte, in dem ich mir erstmal selbst selbst Java beibringen durfte. Java war damals ja auch noch einigermaßen neu. Noch besser aber war: ich durfte auch fast 2 Jahre mehr oder weniger **unbehelligt** an einer neuen Typesetting System (**Web2Print**) programmieren, mit nur einer Hand voll Anforderungen, und weitgehend unbehelligt von unbequemen Fragen oder gar Termindruck. 

 * Wer im Pubikum kennt noch *TeX* oder *Latex*? Ja, genau! Damit hat man damals Diplomarbeiten, Wissenschaftliche Paper, usw. geschrieben. **Word** war zu der Zeit für sowas ziemlich **unbrauchbar**, und ist es zum Teil heute noch.

 * Jedenfalls: Ein paar Jahre früher hatte ich damit  meine Diplomarbeit geschrieben. Die **Algorithmen von Latex** waren in einem Buch erklärt. Das besorgte ich mir und programmierte das ganze in Java nach. Nicht 1 zu 1. Sonst hätten wir ja gleich Latex nehmen können. Das Quellformat sollte jetzt nämlich nicht die etwas kryptische Latex-Syntax sein, sondern das damals **ganz moderne XML**. 

 * Aber genug der alten Geschichten.. **der Punkt ist**, dass ich damit **TestDrivenDevelopment** mit Hilfe der 6 Seite aus Kent Becks Buch recht **erfolgreich** gelernt und praktisch **angewendet** habe.

## Warum TDD und Test First?
https://youtu.be/FlJN6_4yI2A?t=1595 26:35

 * **Welches Problem** will TDD und "Test First" eigentlich lösen ?
But: https://youtu.be/FlJN6_4yI2A?t=3084 51:26


### Stabilität, Qualität

 * In Softwareprojekten die von mehrern Entwicklern über mehrer Jahre entwickelt, weiterentwickeln und neuen Anforderungen angepasst werden, entstehen typischerweise eine Reihe von Qualitäts Problemen. Und wie die meisten aus der Branche inzwischen auch gelernt haben:  Mit automatischen Tests lässt sich die Qualität deutlich verbessern:
    * Softwarequalität, Stabilität, Zuverlässigkeit, Belastbarkeit sind früher oder später ein Thema in praktisch jedem Projekt :
        * Die Entwickler verbringen zu viel Zeit mit Bugsuche, statt neue Funktionen einzubauen.
        * oft stellen die Beteiligten fest, dass je größer die Software wird und je älter, desto schwieriger und langwieriger wird es, Anpassungen und Änderungen vorzunehmen.

Ich hoffe, bis jetzt hab ich euch nix neues erzählt...
### Softwarearchitektur 

 * in größeren Softwareprojekten entsteht typischerweise noch ein weiteres Problem: 
    * Die Softwarearchitektur erodiert bis zu Unkenntlichkeit: Dadurch, dass neue Entwickler, die die ursprüngliche Architektur nicht gut genug kennen, Änderungen vornehmen, entwickelt sich die Software von dieser Architektur auch immer weiter weg, bis  dann kein architektonische Konzept erkennbar ist.

 * Ok, jetzt denken vieleicht viele von euch: "ok, Softwarequalität, Stabilität, Zuverlässigkeit, da sehe ich  einen Zusammenhang zu automatischen Tests, aber was hat das mit Softwarearchitektur zu tun ?"
Stimmts?

 * Also im Vertrauen, dass euch der Zusammenhang zwischen Testen und Qualität und damit auch automatischem Testen und Softwarequalität klar ist, lasst mich direkt auf die Softwarearchitektur eingehen:
### Ebenen der Softwarearchitektur im Vergleich

 * Vorher ein Wort zu den verschiedenen Ebenen von Softwarearchitektur: 
    * wie beim Bauen von Gebäuden gibt es ja auch verschiedenen Ebenen: also
        * Wie sieht mein Stadtteil aus in dem die Gebäude stehen, wie sind die Straßen, Gehwege, Parks und Gebäude insgesamt organisiert?
        * Wie schaut die Fassade aus, und wie ist die Aufteilung in den Gebäuden? z.B. Büros, große oder kleine Wohnungen 
        * Wie sind die Wohnungen aufteilt, z.b. wie groß ist das Wohnzimmer im Vergleich zur Küche
        * bis hin: welchen Bodenbelag hab ich wo, Welche Lichtschalter an dern Wand , welche Türgriffe?
    * Wenn wir diese 4 Ebenen auf Softwarearchitektur übertragen und das auf TDD anwenden, dann hilft TDD eher bei den untern beiden Ebenen, also bei der Architektur der kleineren Details, weniger bei den obern beiden Ebenen, der Architektur im ganz Großen.
### TDD und Softwarearchitektur Behauptung

 * So, die Behauptung die jetzt im Raume steht, ist also, dass TDD/TestFirst bei der Softwarearchitektur der untern beiden Ebenen massiv hilft und auch hift über längere Zeiträume diese Architektur positiv beeinflusst.

 * Im Gegensatz dazu, helfen nachträglich hinzugefügte automatische Tests zwar für die Softwarequalität im Sinne von Stabilität und Fehlerarmut. Nachträglich hinzugefügte automatische Tests helfen aber gar nicht für die Softwarearchitektur, für keine der 4 Ebenen
### Probleme ohne TDD 

 * Bei Software die von mehrköpfigen Teams gebaut werden,  ist es wichtig, dass nicht nur der ursprüngliche Autor einer Methode oder Klasse leicht versteht, und auch nach Wochen und Monate noch versteht. 

 * Denn Software die wirklich benutzt wird, muss ja ständig neuen Anforderungen angepasst werden und weiterentwickelt werden, da erzähle ich ja niemandem was neues.

 * Wenn ich aber Softwareteile anpassen und erweitern muss, muss ich erstmal verstehen was da bisher steht. Und zwar möglichst schnell.

 * Genau hier kommt die Softwarearchitektur der unteren beiden Detailebenen ins Spiel. 
    * ist die Softwarearchitektur für einen Entwickler schnell verständlich oder nicht ?
    * ist die Softwarearchitektur flexibel und leicht änderbar ? 

 * das ist auf den untern beiden Detailebenen, also der Ebene der Klassen und Methoden und des Zusammenspiels von diesen auf Modulebene extrem wichtig. 

# Timestamp 13 Min
## Wie hilft TDD/TestFirst bei der Softwarearchitektur?
**Test first..**: 

 * .. zwingt **vor** dem Schreiben des eigentlich Code und der eigentlichen Unittests dazu, sich **sehr** **klar**,  **sehr** **klar**, über die **Anforderungen** und das Softwaredesign und zwar auf Klassen/Interface- Ebene Gedanken zu machen.

 * .. trägt dann fast automatisch zu einer **klareren Softwarearchitektur** auf Klassen/Interface- Ebene bei. 

 * .. zu schreiben geht aber **nur**, wenn ich nicht nur die **fachlichen** Anforderungen genau verstanden sondern, wenn ich auch **genau** verstanden habe wie sich mein neuer Code in den bestehenden einfügen soll. Ich bin also **gezwungen**, mir vor der **ersten** Codezeile die ich schreibe, mit ein **durchdachtes  Konzept** zu machen.

 * - solcher Code braucht meiner Erfahrung nach **weniger späteres  Refactoring** (also Refactoring dessen Notwendigkeit erst in einem späteren Entwicklungszyklus offensichtlich wird)

 * .. führt zu **kleineren** Klassen und Methoden, fördert automatisch das **[Single-Responsibility-Prinzip](https://de.wikipedia.org/wiki/Single-Responsibility-Prinzip)**, damit meine ich, kleinere Klassen und kleinere Methode, die von weniger anderen Klassen abhängen. Damit wir die Software leichter verständlich und auch leichter und damit billiger anpassbar.

Ich hoffe euch ist klar, dass das was sehr gutes ist. 


 * .. spart am Ende halt doch Zeit und liefert **höhere Code-Qualität**.

[mehr findest du hier](../_posts/2020-10-09-TDD-aber-richtig.md#test-first-ist-deswegen-entscheidend-weil)

## Beweise, Beweise
So jetzt könnt ihr sagen: Der Teichmann kann uns ja viel erzählen, stimmt das denn überhaupt und funktioniert das in der Praxis ? 

Die Frage ist, lassen sich meine Behauptungen belegen, welche Erfahrungen haben andern mit TDD/TestFirst gemacht?
Da findet man doch eine Menge Indizien, die dafür sprechen.

 * Bücher über TDD selbst, werden immer wieder neu herausgebracht. Kent Becks Buch ist also beweitem nicht das einzige zu dem Thema.

 * Bücher über Softwarearchitektur z.B. 

 * eine Reihe von wissenschaftlichen Studien, z.T. sogar richtige Vergleichsstudien

 * eine Reihe von systematischen Erfahrungsberichten aus verschiedenen großen Unternehmen.

 * sogar einige Metastudien zu dem Thema konnte ich finden.

 * Zitat: "Das Spring Team unterstützt und beführwortet TestDrivenDevelopment. ["The Spring team advocates test-driven development,TDD ."](https://docs.spring.io/spring-framework/docs/current/reference/html/testing.html)

 * Zitat: "Wir praktizieren selbst TestDrivenDeveopment. Da heißt, bevor wir die Arbeit an einem neuen Feature beginnen, schreiben wir zuerst einen Test, der das gewünschte Verhalten genau beschreibt." ["At VMware Pivotal Labs, we practice test-driven development (TDD). That means before we begin work on a new feature, we first write a test that describes the behavior we want to add to our software.](https://tanzu.vmware.com/content/blog/go-faster-write-tests-first)

### Ergebnisse:

 * [IBM: Assessing test-driven development](https://collaboration.csc.ncsu.edu/laurie/Papers/MAXIMILIEN_WILLIAMS.PDF) : **50% weniger Bugs** als bei "test last", minimaler geringere Produktivität

 * [Microsoft: Evaluating the Efficacy of Test-Driven Development: Industrial Case Studies](https://d1wqtxts1xzle7.cloudfront.net/36509027/fp17288-bhat.pdf?1423032149=&response-content-disposition=inline%3B+filename%3DEvaluating_the_Efficacy_of_Test_Driven_D.pdf&Expires=1599907639&Signature=RuaKEjh7AbrkimLa5LGjb6zOpojv18srJrYQO7ONLNjWm586g6nxlDjGnYgubwIFYYp5fNkQulFn6YD3wpvud5bBhvwkO4nOOFMYyhATLdvHjHtW3vzm6ncsuqgwYTIKtrxbxAd7lQiEiue~D300FsgSLK6ZUk9DOssTqS0NZry6syc9I6IQYR6H2BRcnzf9oxvCTBWPzjSEBPi2cqYpyKbF1Y322XtLj7fdNTu8IVkmUULxwH3R1GVsEZrdpOAOJpM0b1ZAsJZEI0K3hiv~ENiV79hUjoyRu5xLaDeDWA4Nhg4Q-J8Zu8UQ18hQEjl0dOZnq7o4Xq~2-8jbuzDxIQ__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA) :  **Bugrate sinkt mit TDD um 62%-77%** , 15% -35% mehr Zeit für TDD notwendig.

 * [Metastudie, die 6 unterschiedliche andere Studien ausgewertet hat](https://digitalcommons.calpoly.edu/cgi/viewcontent.cgi?article=1027&context=csse_fac): Ergebnis: deutlich **Positiv, auch bezüglich Software-Architektur**

 * [An Experimental Evaluation of the Effectiveness and Efficiency of the Test Driven Development](https://ieeexplore.ieee.org/abstract/document/4343756) : **deutlich bessere Gesamt-Produktivität und Codequalität**

 * [noch eine Metastudie](https://www.researchgate.net/profile/Burak_Turhan/publication/258126622_How_Effective_is_Test_Driven_Development/links/54e794320cf27a6de10a8afe/How-Effective-is-Test-Driven-Development.pdf) : Gesamturteil deutlich positiv, aber Hinweis: schwer zu meistern , **Fazit: Empfehlung für TDD**

 * [Empirische Studie zu Test-Driven Development](https://link.springer.com/book/10.1007%2F978-3-642-04288-1) : "test first" ist **besser** darin, **lose gekoppelte** Softwarekomponenten hervorzubringen als "test last". "lose gekoppelt" bewirkt zum Beispiel bessere Wartbarkeit, verständlichkeit für die Entwickler, ist also was sehr gutes.

[mehr Details hier](../_posts/2020-09-19-Literaturrecherche-TDD.md)


## Was ist TDD genau?
 .. und was meint Kent Beck mit  "We will write tests before we code, minute by minute."?

 * Die Basis von TDD sind Unit-tests. Mit "**Unit**" ist die kleinste sinnvolle Einheit, die testbar ist gemeint. Möglichst nur eine Methode oder Klasse oder eine Gruppe von wenigen eng zusammengehörige Methoden oder Funktionen, die eine nützliche Berechnung oder Entscheidung machen.

 * Schopsystem: Rabattberechnung.

 * Also im besten Fall ein paar Zeilen Code, sagen wir zwischen 10 und 100 Zeilen   

 * der Begriff *Unittest* meint dann einen Stück Software, welches die Korrektheit dieser einen **Unit** testet. Und nur dieser. D.h. der Test sollte nach Möglichkeit keine **anderen** Teile aus dem Softwareprojekt testen. 

 * Der Unittest soll **NICHT** andere Teile des Codes  testen, auch nicht, wenn die zu testende **Unit** eigentlich noch andere Units benötigt, um zu funktionieren. 

 * Der **Unit-Test-Code** sollte dabei **alle** möglichen Pfade in der der nützlichen **Unit** abtesten. Dabei insbesonders alle **Grenzbedinungen** in der **Unit** auf Korrektheit überprüfen. 

 * Das Ergebnis ist dann eine sogenannte Testabdeckung von 100%. Auf die "Testabdeckung" gehen wir später noch ein.

 * Der eigentliche Witz ist aber vor allem: Wir schreiben den Test **BEVOR** wir den Code für die eigentlich nützliche Unit schreiben. 
## Die wichtigen Fragen.
    * Wie geht das überhaupt ?
    * Warum findet man so wenige Programmierer die das tatsächlich tun ?
    * Warum ist das so schwer ? 
    * Wie kann ich als Softwareentwickler mich in kleinen Schritten incrementell von TestLast zu TestFirst vorarbeiten ?

# Timestamp:27 Min
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
### Wie gehen wir bei Test First vor? :

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

## Warum ist das eigentlich sooo schwer?
Ist es wirklich sooo schwer ? Eindeutig ja! 

 * Zitat aus aus [Large-Scale Scrum >>LeSS<<](https://less.works/de/less/technical-excellence/test-driven-development):
    * "Wir treffen **selten** Entwickler, die in der Lage ware, sich TDD/TestFirst selbst beizubringen. Die meisten Entwickler brauchen **tage- oder gar wochenlanges** Pair-Programming, bis sie es können." und weiter :
    * "Test-Driven Development ist vermutlich die **schwierigste** agile Praxis, aber TDD ist gleichzeitig die einer der **größten Gelegenheiten** die Qualität und das Design des Codes zu verbessern.

 * [Metastudie: How Effective is Test-Driven Development?](https://www.researchgate.net/profile/Burak_Turhan/publication/258126622_How_Effective_is_Test_Driven_Development/links/54e794320cf27a6de10a8afe/How-Effective-is-Test-Driven-Development.pdf) : 
    * "Fast alle \[Studien\] sind sich einig, dass **TDD schwierig zu lernen** ist.

 * Aus [Test-Driven Java Development - Second Edition](https://www.packtpub.com/product/test-driven-java-development-second-edition/9781788836111) 
    * "It\'s not an easy thing to master TDD. Even after learning all the theory and going through best practices and anti-patterns, the journey is only just beginning. **TDD requires time and a lot of practice**. It\'s a long trip that does not stop with this book.

## Ich hab noch nie TestFirst gemacht, wie komme ich dahin?
Nach der Vorwarnung gilt trotzdem: mit hinreichender Motivation kann man es sich durchaus beibringen. Wichtig ist nur entweder große Neugierde, oder die feste Überzeugung, dass es sich auszahlen wird. 
Daher hier eine Schritt für Schritt Anleitung: 
1. mache ein paar "Trockenübungen" also Übungsaufgaben abseits von realem Produktionscode, aber mit den gleich Sprachen/Tools wie deine Produktionsumgebung 
    * Suche die eine kleine Übungsaufgabe, die du in höchtens 1 stunde  lösen kannst. [Ideen hier](https://www.freecodecamp.org/news/the-10-most-popular-coding-challenge-websites-of-2016-fb8a5672d22f/)
    * notfalls, wenn du noch gar keine Plan für Test-First hast, fang mit Test-Last an und lerne wie man überhaupt Unittests schreibt.
    * wenn du fertig bis, lösche alles und fang mit der selben Aufgabe ganz von vorn an, diesmal aber test-first
    * mache diese Übung ein paar mal, immer wieder, bis  du für die Lösung mehr googlen musst und bis es es dir sehr flüssig von der Hand geht,
    * du wirst feststellen: in jeder Iteration wirst du nicht nur schneller, sondern dein Code bekommt mit jeder Iteration auch eine bessere Struktur, wird kompakter, gleichzeitg leichter für andere verständlich.
1. in der Produktionumgebung: fange an gute Test-Last Tests zu schreiben. Prüfe deren Testabdeckung, verwende Mutation-Testing. Baue Know How auf, wie du überhaupt Unittests in deinem Projekt schreiben kannst. 
1. Organisiere oder nehme Teil an Coding Dojos für Test-First
1. beginne auch in Produktionumgebung mit TestFirst.


# Timestamp 40 min 
## ganz einfaches Codebeispiel : 

# Bonus Content:
## Testabdeckung messen ?

 * Ja, aber nur wärend des schreibens der Tests, um Lücken in der Testabdeckung zu finden. ![testCoverage](/assets/images/testCoverage.png){:height="360px" width="360px"}

 * NEIN, um Qualitätsaussagen über die gesamte Codebasis zu machen 
    * weil es gibt Code der nicht sinnvoll zu testen ist, z.B. weil er keine Fallunterscheidungen oder Schleifen enthält. Hier nachträglich die Testabdeckung zu erhöhen macht die Codebasis  in der Regel nicht besser.


 * Beispiel : ???

### noch besser: Mutation-Testing, hilft auch bei Test-Last!

 * [Mutation-Testing](https://en.wikipedia.org/wiki/Mutation_testing)

 * hilft vor allem blinde Flecken zu finden, sehr gut auch für "test-last"

 * Konkret: 
    * [javascript (including angular)](https://stryker-mutator.io/docs/stryker-js/) getting-started
    * [java](https://pitest.org)

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



## Anmerkungen fürs nächste mal: Beispiele einbauen. Einfluss auf SoftwareArchitektur nachweisen

https://www.youtube.com/watch?v=UWtEVKVPBQ0 : 
Wenn Tests schwer zu schreiben sind, dass sagt das was aus über die Qualität unserer Softwarearchitektur: das stimmt was nicht!
https://web.archive.org/web/20100105084725/http://blog.james-carr.org/2006/11/03/tdd-anti-patterns/

https://www.javacodegeeks.com/2018/02/developers-dont-use-tdd.html









