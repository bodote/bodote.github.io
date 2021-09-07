---
title: "TDD Teil 1: Warum Test Driven Development?"
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

# Teil 1: Warum TDD und was hat TDD mit Scrum zu tun ?

Ganz Gallien ist von den Römern besetzt, nur ein kleines.... usw, die Asterix Fans unter euch kennen den Text.

Mit TDD ist es irgendwie so ähnlich, man könnten fast schreiben:
"Die ganze Softwarewelt ist von Agilität und Scrum besetzt! Wirklich ? Nur ein kleines scheinbar unbedeutendes Kapitel in Kent Becks Buch aus dem Jahr 2000, in dem er die Grundlagen zu Scrum gelegt hat, wiedersetzt sich nach wie vor der wirklich großen Verbreitung. Das Kapitel beschreibt Test Driven Development."

Warum ist das so ? Ist TDD wirklich eine so gute Idee? Warum wird es dann nicht überall eingesetzt? In welchem Umfeld steigert es die Produktivität der Softwareentwicklung, in welchem Umfeld vieleicht ist es sogar contraproduktiv ?

Wenn du dich das jetzt auch fragst, und den Beweis sehen willst, dass TDD mit Test First 50% weniger Bugs und einen bessere Softwarearchitektur zur Folge hat, dann lies weiter.

Also für mich begann das alles mit dem Buch "Extreme Programming" von Kent Beck im Jahr 2000.
In dem Buch war viel von den Konzepten die Rede, die später unter dem Namen "Scrum" bekannt wurden.
Aus heutiger Sicht zeigt das schon: Kent Beck ist nicht irgendein Fachbuchautor, er ist einer DER großen Vordenker der Softwareindustrie. Seine Bücher, Blogs und Youtube-Video sind immer sehr interessant und oft wegweisend.
Kent Beck hat die Art und Weise wie wir heute Software entwickeln wie kaum ein Anderer beeinfluss.
Er war maßgeblich am **"Agile Manifest"** beteiligt, das 2001 publiziert wurde und damit eine wahre Revolution in der Softwarebranche ausgelöst hat.
Also, er ist tatsächlich einer der "Erfinder\*" von Scrum, wenn du so willst. Und inzwischen arbeitet praktisch jeder in der Softwareindustrie weltweit nach der Methode, oder zumindest behaupet praktisch jeder, dass er nach Scrum arbeite würde. (Auch wenn es bei näherem Hinsehen manchmal fragwürdig erscheint.)

# Meine persönliche Erfahrung mit TDD

Jedenfalls, im Jahr 2000 hatte ich das Buch gelesen. Der Inhalt war genau , was der Titel versprach. Nämlich **Extrem**. Für die meisten damals war es es vor allem aber **extreme** Unsinn. Wer hatte denn sowas schon mal gehört: die Entwickler sollten **paarweise** am gleichen Problem gemeinsam arbeiten!
Mit kam das auch zumindest ungewöhnlich und überraschend vor. Aber ich hatte schon genügend Probleme in meinen damals 5 Jahren Berufserfahrung gesehen, dass ich für neue Lösungsansätze sehr offen war. Kent Becks Ideen fand ich jedenfalls sehr spannend.
Leider ist es mir damals in meinem beruflichen Umfeld noch nicht sofort gelungen Scrum einzuführen! Die Zeit oder die Umständen waren irgendwie noch nicht reif.

Aber da gab es ja noch Kapitel 18 in Kent Beck's Buch: Auf gerade mal 6 Seiten erklärt Kent Beck, dass man Software automatisch testen sollte und sogar die Tests **VOR** dem **eigentlichen** Teil der Software schreiben sollte:
"We will write tests before we code, minute by minute. We will preserve these tests forever, and run them all together frequently. We will also derive tests from the customer's perspective." [^1]
Wir vergegenwärtigen uns nochmal: Kent Beck ist nicht irgendwer, sondern einer der ganz großen Vordenker der agilen Bewegung und der Softwarebranche insgesamt.
So, und wenn einer DER großen Vordenker der letzten 20 Jahre in der Branche eine Konzept wie TDD vorschlägt, dann darf man das auf jeden Fall sehr ernst nehmen, und es lohnt sich sicher, sich damit näher aueinanderzusetzten, oder?

Genau das hab ich damals von 2001 bis 2003 selbst ausprobiert, selbst wenn es damals war alles andere als offensichtlich war, dass das eine wirklich gute Idee ist und Kent Beck damals mit seinem Buch einer unter vielen, der halt ein paar verrückt klingende Ideen hatte.
Irgendwie war ich auch gerade auf der Suche nach Ideeen, wie man besser als bisher Software entwickeln könnte. Denn ich hatte in meiner bisherigen Berufserfahrung natürlich auch eine Reihe von Problem in Softwareentwicklungsprojekten gesehen, für die ich Lösungen suchte.

Dabei hatte ich das Glück, dass ich damals gerade einen neuen Job hatte, in dem ich mir erstmal selbst selbst Java beibringen durfte. Java war damals ja auch noch einigermaßen neu.

Noch besser aber war: ich durfte auch fast 2 Jahre mehr oder weniger unbehelligt an einem Projekt programmieren, mit nur einer Hand voll Anforderungen, und weitgehend unbehelligt von unbequemen Fragen oder gar Termindruck. Mein Damaliger Chef verbrachte nämlich die meiste Zeit auf Jamaika mit seiner heißen jamaikanischen Freundin und war deshalb nur 2 mal im Jahr überhaupt anwesend.
Außerdem waren wir eine RisikoKapital finanziertes Startup, die Internetblase war damals noch voll am Aufblähen und Geld spielte Keine Rolle. Die Startups waren froh wenn sie überhaupt Softwareentwickler finden konnten.

Meine Aufgabe war ein Typesetting Engine für ein [Web2Print](https://de.wikipedia.org/wiki/Remote_Publishing)-System zu entwicklen. Web2Print ist im Grunde ist die Idee aus den Eingaben in ein Webformular auf einem Webserver ein Druckreifes PDF zu produzieren. Z.B. fürs Marketing. Das Webformular kann im Prinzip Sekretärin vom Chef ausfüllen und mit dem System ein 100% perfektes CI-konforme Werbeanzeige für die Tageszeitung produzieren. Man spart quasi den Graphiker ein.

Meine Lösungsidee war damals, den in Büchern gut beschriebenen Typesetting- Algorythmus von _TeX_ bzw. _Latex_ zu nehmen und als Beschreibungssprache das damals relativ neu definierte _XSLT/Formatting Objekts_ Format zu verwenden.

Und da ich wie gesagt keine weiteren Vorgaben hatte , und auch keinen wirklichen Zeitdruck, nahm ich mir vor das ganze mit dem TestDriven Development von Kent Becks Buch Ansatz zu entwickeln. Und weil ich das Projekt auch ganz allein entwicklen durfte, musste ich mich mit niemandem absprechen. Mein Chef war ja sowieso in Jamaika , also weit weg.

Fazit nach den 2 Jahren: für mich hat das damals prima funktioniert. Seit dem bin ich ein großer Fan von TestDrivenDevelopemt.

# Der Meister spricht

Jeder Entwickler der zum ersten Mal von der Idee hört den Test-Code VOR dem eigentlich Code zu schreiben, lacht doch darüber und denkt: "blöde Idee", oder ?

Genau das hat der Erfinder selbst auch zuerst gedacht. Hört selbst, was Meister Beck dazu zu sagen hat: [Video ab 26:35 bis 27:01](https://youtu.be/FlJN6_4yI2A?t=1595): "Turns out, there're lots of good reasons to write the test before you write the code"

# Welche Probleme genau will TDD und "Test First" eigentlich lösen ?

## Das Offensichtliche: Stabilität, Qualität

In Softwareprojekten die von mehrern Entwicklern über mehrere Jahre entwickelt, weiterentwickeln und neuen Anforderungen angepasst werden, entstehen typischerweise eine Reihe von Qualitäts Problemen. Und wie die meisten aus der Branche inzwischen auch gelernt haben: Mit automatischen Tests lässt sich die Qualität nicht nur deutlich verbessern, da sind wir uns sicher einig. Sondern ausreichende Testabgeckung vorrausgesetzt, kann man damit dann auch ein bestimmtes Qualitätsniveau auf Dauer halten.

Ich hoffe, bis jetzt hab ich nichts Neues erzählt...

Das Besondere an TDD und Test first ist aber dass die Bugraten nochmal um 50% oder mehr gesenkt werden kann im Vergleich zu Test-Last

Du glaubt das nicht ? Ich dann das beweisen , wie wir weiter unten noch sehen werden.

Softwarequalität, Stabilität, Zuverlässigkeit, Belastbarkeit sind früher oder später ein Thema in praktisch jedem Projekt, aber es gibt noch weitere Probleme die in Softwareprojekten typischerweise mit der Zeit auftauchen :

Also im Vertrauen, dass euch der Zusammenhang zwischen Testen und Qualität und damit auch automatischem Testen und Softwarequalität klar ist, lasst mich direkt auf die Softwarearchitektur eingehen:

## Das Überraschende: die Softwarearchitektur

in größeren Softwareprojekten entsteht typischerweise noch ein weiteres Problem:

Die Entwickler brauchen immer länger um Funktionen einzubauen: Oft stellen die Beteiligten fest, dass je größer die Software wird und je älter, desto schwieriger und langwieriger wird es, Anpassungen und Änderungen vorzunehmen.

Viele nehmen das als Gott-gegeben hin, aber das muss nicht so sein. Warum ist das aber oft so ?

Die ursprüngliche Architektur war noch klar strukturiert, Architekt und/oder die ERsten Entwickler hatten ein gutes Konzept und das auch so umgesetzt. Aber dann setzt Fluktuation der Entwickler ein oder die Entwickler werden mit der Zeit auch nachlässiger.
Es gibt neue Anforderungen die eigentlich eine Anpassung der Architektur erfordern würden, statt dessen wird versucht mit zunächst minimalem Aufwand hier und dort ein paar Kleinigkeiten dazuzustückeln.

Eine saubere Architektur tritt in den Hintergrund, alle wollen möglichst schnell neue Features einbauen. Das gelingt auch zunächste. Gleichzeitige erordiert aber die Architektur immer mehr.
Neue Entwickler kommen dazu , erkennen die geplante Architektur kaum noch und machen das ganze noch viel schlimmer.
Die Softwarearchitektur erodiert bis zu Unkenntlichkeit: Dadurch, dass neue Entwickler, die die ursprüngliche Architektur nicht gut genug kennen, Änderungen vornehmen, entwickelt sich die Software von dieser Architektur auch immer weiter weg, bis dann kein architektonische Konzept erkennbar ist.

## Aber Warum ist die Architektur überhaupt so wichtig ?

Ich als Entwickler möchte nicht, dass Änderungen an Komponente A keine Überraschende Wirkung in Komponenten B nach sich zieht.

Denn das wäre ja so, als ob ich Elektriker wäre, der hier in der Wand einen neuen Lichtschalter einbaut, und der auch zunächst funktioniert. Aber plötzlich entsteht in der Wand gegenüber ein Kurzschluss und die ganze Wand brennt ab. Jetzt bin ich natürlich tagelang damit beschäftigt die Überraschung erstmal zu verstehen und dann das Problem notdürftig zu flicken.

Zum Glück ist die elektrische Verkabelung von Gebäuden nicht annähernd so komplex wie Software sein kann.

Jedenfalls: TDD verspricht das Architekturproblem auf Ebene 3 und 4 zu lösen. Aber was sind die Ebenen 3 und 4 überhaupt ? Das klären wir im nächsten Teil der Blogserie.

# Fußnoten:

[^1]: [Kent Beck: Extreme Programming Explained. Embrace Change., Addison-Wesley, 2000, ISBN 0-201-61641-6. Kapitel 18](https://books.google.de/books?id=G8EL4H4vf7UC&lpg=PR9&ots=jbvErnnRBq&dq=%22We%20will%20write%20tests%20before%20we%20code%2C%20minute%20by%20minute.%22&hl=de&pg=PA115#v=onepage&q=%22We%20will%20write%20tests%20before%20we%20code,%20minute%20by%20minute.%22&f=false)
