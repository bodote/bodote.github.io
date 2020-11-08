---
title: "Sehr große Datenbanken sehr schnell kopieren"
date: 2020-10-08
categories:
  - blog
tags:
  - Testing
toc: true
classes: wide
---

# Sehr große produktive Datenbanken als schreibbarte Test-DB den  Entwickler in Sekunden zu Verfügung stellen
## Das Problem
Im Rahmen von Webapps braucht das SW-Entwicklerteam  zum Debuggen die "echten" Daten der Datenbank. 
Wenn diese aber leider mehrere 100 Gigabyte oder mehrer Terabyte groß ist, führt das zu sehr langen Wartezeiten 
in der Größenordnung von Stunden oder Tagen, bis die DB vom Prodsystem 
exportiert und im Test-System wieder importiert ist. 
Weiterhin müssen ggf. einzelne Teile der kopierten Datenbank anonymisiert werden um dem Datenschutz zu genügen.

## Die Lösung: ZFS und Docker
Kurz skiziert funktioniert das so:
* ZFS erstellt Snapshots des Dateisystem auf dem die Datenbankengine operiert. (Dauert unter einer Sekunde)
* Aus dem ZFS - Snapshot wird eine lese- und schreibbarer "Clone" des Dateisystem erzeugt (Dauerte unter einer Sekunde)
* dieser Clone wird einem Dockerconteiner mit der DB-Engine (z.B. ein MySql-Dockercontainer)
* Der Dockercontainer wird gestartet und seine IP - Adresse in einem Nameserver registiriert (z.B. mit "Bind")
* Die einzelnen Schritte werden dann per Script automatisiert und 
* mit hilfe eines Jenkins-Job den Entwicklern zu verfügung gestellt. 
* Damit können die Entwickler das ganze mit wenigen Mouseklicks bedienen und jederzeit innerhalb von Sekunden oder wenige Minuten einen 
schreibbarten DB-test - Clone der Produktiven Daten erzeugen. 
* ggf. lässt sich ein Anonymisierungsscript sehr leicht via Script noch ergänzen.

