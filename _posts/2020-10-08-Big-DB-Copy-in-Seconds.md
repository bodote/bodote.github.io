---
title: "Sehr große Datenbanken sehr schnell kopieren"
date: 2020-10-08
categories:
  - blog
tags:
  - Testing
  - DevOps
toc: true
classes: wide
---

# Sehr große produktive Datenbanken als schreibbare Test-DBs den  Entwicklern in Sekunden zu Verfügung stellen
## Das Problem
Im Rahmen einer großen Webapps-Entwicklung braucht das SW-Entwicklerteam zum Debuggen die "echten" Daten der Datenbank. 
Wenn diese aber leider mehrere 100 Gigabyte oder mehrere Terabyte groß ist, führt das zu sehr langen Wartezeiten 
in der Größenordnung von Stunden oder Tagen, bis die DB vom Produktionssystem 
exportiert und im Test-System wieder importiert ist. 
Weiterhin müssen ggf. einzelne Teile der kopierten Datenbank anonymisiert werden um dem Datenschutz zu genügen.

## Die Lösung: ZFS und Docker
Die Grundidee ist:
* Ein ZFS-Dateisystem[^1] (z.B. "ZFS on Linux"[^2]) erstellt Snapshots des Dateisystem auf dem die Datenbankengine operiert. (Dauert unter einer Sekunde)
* Aus dem ZFS - Snapshot wird eine lese- und schreibbarer "Clone" des Dateisystem erzeugt (Dauerte unter einer Sekunde)
* dieser Clone wird einem Dockerconteiner mit der DB-Engine (z.B. ein MySql-Dockercontainer)
* Der Dockercontainer wird gestartet und seine IP - Adresse in einem Nameserver registiriert (z.B. mit "Bind")
* Die einzelnen Schritte werden dann per Script automatisiert und 
* mit Hilfe eines Jenkins-Job den Entwicklern zu verfügung gestellt. 
* Damit können die Entwickler das ganze mit wenigen Mouseklicks bedienen und jederzeit innerhalb von Sekunden oder wenige Minuten einen 
schreibbaren DB-test - Clone der Produktiven Daten erzeugen. 
* ggf. lässt sich ein Anonymisierungsscript sehr leicht via Script noch ergänzen.

[^1]: [ZFS Dateisystem](https://de.wikipedia.org/wiki/ZFS_(Dateisystem)#:~:text=ZFS%20ist%20ein%20von%20Sun,im%20Server%2D%20und%20Rechenzentrumsbereich%20enth%C3%A4lt.)
[^2]: [ZFS on Linux](https://openzfs.github.io/openzfs-docs/Project%20and%20Community/Admin%20Documentation.html)