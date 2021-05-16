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
## Warum TDD
* Warum halte ich hier trotzdem einen Vortrag zum Thema TDD ? Weil mich das Thema schon **immer** interessiert hat, seit ich so ums Jahr 2000 das Buch "Extreme Programming" von Kent Beck gelesen habe. 
* Da war viel von den Konzepten die Rede, die später unter dem Namen "Scrum" bekannt wurden. Als ich 2003 meinem Kompangnion Joachim von dieser Vision für eine bessere Methode Software zu entwickeln überzeugen wollte, hat er nur gesagt: "Wer Visionen hat sollte zum Arzt gehn"  (nur um dann ein paar Jahre später einzusehen, dass Kent Becks Ideen doch extrem brauchbar sind)
* Also mit Scrum war erstmal nix! Aber da gab es ja noch Kapitel 18: Auf gerade mal 6 Seiten erklärte Kent Beck, dass man Software automatisch testen sollte und sogar die Tests **VOR** dem eigentlichen Teil der Software schreiben sollte.
* Zitat "We will write tests **before** we code, minute by minute. We will preserve these tests forever, and run them all together frequently. We will also derive tests from the customer's perspective."
* Das war damals echt revolutionär und für mich eine neue Idee, die ich dann gleich auch  umzusetzten versuchte. 
* Dabei hatte ich das Glück damals gerade einen neuen Job zu haben, in dem ich mir nicht nur selbst Java beibringen durfte. Sondern ich durfte auch fast 2 Jahre mehr oder weniger unbehelligt an einer neuen Text-Layout Engine programmieren, mit nur einer Hand voll Anforderungen, und weitgehend unbehelligt von unbequemen Fragen oder gar Termindruck. 
* Wer im Pubikum kennt noch *TeX* oder *Latex*? Ja, genau damit hatte ich ein paar Jahre zuvor meine Diplomarbeit geschrieben. Die Algorithmen von Latex waren in einem Buch erklärt. Das besorgte ich mich und programmierte das ganze in Java nach. Nicht 1 zu 1. Sonst hätten wir ja gleich Latex nehmen können. Das Quellformat sollte jetzt nämlich nicht die etwas kryptische Latex-Syntax sein, sondern das damals ganz moderne XML. 
* Aber genug der alten Geschichten..
## Warum TDD und Test First?
* Welches Problem will TDD und Test First eigentlich lösen ?
* In Softwareprojekten die von mehrern Entwicklern über mehrer Jahre entwickelt, weiterentwickeln und neuen Anforderungen angepasst werden, entstehen typischerweise eine Reihe von Problemen, die mit TDD/TestFirst deutlich verbessert werden können:
    * Softwarequalität, Stabilität, Zuverlässigkeit, Belastbarkeit werden früher oder später ein Thema sein
    * oft stellen die Beteiligten fest, dass je größer die Software wird und je älter, desto schwieriger und langwieriger wird es, Anpassungen und Änderungen vorzunehmen. 
    * Die Entwickler verbringen zu viel Zeit mit Bugsuche, statt neue Funktionen einzubauen.
    * Die Softwarearchitektur erodiert bis zu Unkenntlichkeit: Dadurch, dass neue Entwickler, die die ursprüngliche Architektur nicht gut genug kennen, Änderungen vornehmen, entwickelt sich die Software von dieser Architektur auch immer weiter weg, bis  dann kein architektonische Konzept erkennbar ist.
* Ok, jetzt denken vieleicht viele von euch: "ok, Softwarequalität, Stabilität, Zuverlässigkeit, da sehe ich  einen Zusammenhang zu automatischen Tests, aber was hat das mit Softwarearchitektur zu tun ?"
Stimmts?
* Also im Vertrauen, dass euch der Zusammenhang zwischen Testen und Qualität und damit auch automatischem Testen und Softwarequalität klar ist lasst mich direkt auf die Softwarearchitektur eingehen:
* Vorher ein Wort zu den verschiedenen Ebenen von Softwarearchitektur: 
    * wie beim Bauen von Gebäuden gibt es ja auch verschiedenen Ebenen: also
        * Wie sieht mein Stadtteil aus in dem die Gebäude stehen, wie sind die Straßen, Gehwege, Parks und Gebäude insgesamt organisiert?
        * Wie ist die Aufteilung in den Gebäuden? z.B. Büros, große oder kleine Wohnungen 
        * Wie sind die Wohnungen aufteilt, z.b. wie groß ist das Wohnzimmer im Vergleich zur Küche
        * bis hin: welchen Bodenbelag hab ich wo, Welche Lichtschalter an dern Wand , welche Türgriffe?
    * Wenn wir diese 4 Ebenen auf Softwarearchitektur übertragen und das auf TDD anwenden, dann hilft TDD eher bei den untern beiden Ebenen, also bei der Architektur der kleineren Details, weniger bei den obern beiden Ebenen, der Architektur im ganz Großen.
* So, die Behauptung die jetzt im Raume steht, ist also dass TDD/TestFirst bei der Softwarearchitektur der untern beiden Ebenen massiv hilft und auch hift über längere Zeiträume diese Architektur positiv beeinflusst.
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
    * Geht das überhaupt ?
    * Warum hackt da Kent Beck und andere immer noch so darauf rum ?
    * Warum findet man so wenige Programmierer die das tatsächlich tun ?
    * Wie kann ich als Softwareentwickler mich in kleinen Schritten incrementell von TestLast zu TestFirst vorarbeiten ?
* This is what we talk about today ! (wie meine Lieblings-Physikerin auf Youtube immer sagt)
# Timestamp:? Min
## Geht das überhaupt?
* Also, wenn man die paar Zeilen aus Kents Becks Buch einfach so versucht direkt umzusetzten, dann merkt man schnell, ganz so einfach ist das nicht.
* Zunächst klären wir ein paar Vorraussetzungen. Sind wir überhaupt in der Situation, TDD mit test first gerade anwenden zu können ?
    * Nehmen wir an wir sein ein SWEntwickler in einem Team
    * irgend jemand hat sich schon über das Gesamtkonzept den Kopf zerbrochen und eine Software-Architektur entworfen und diese uns soweit erklärt, dass wir ein grobes Verständniss dafür haben.
    * Wir sollen jetzt ein neues Feature implementieren, wofür wir aller Vorraussicht mindestens eine neue Klasse, Komponente, oder Service oder ähnliches benötigen. 
    * wir müssen zwar auch bestehenden Code ändern, aber der neu zu schreibende Code überwiegt auf jeden Fall.
    * idealerweise gibt es schon irgendein Unittest-Framework im Projekt, auch wenn das bisher nur zum "Test Last" eingesetzt wurde.
* Die Erfahrung zeigt, dass man sinnvollerweise so vorgeht:
    1. wir brauchen ein Konzept, das kann im einfachsten Fall im Kopf passieren, mit Papier und Bleistift, Oder, wer's gerne schwergewichtig mag (oder in einem großen Projekt Dokumentationspflichten hat), denn gern auch mit einer Software seiner Wahl.
    1. 
## Anmerkungen fürs nächste mal: Beispiele einbauen.








