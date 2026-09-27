---
title: "der Code-Review Engpass"
date: 2026-09-16
published: false
visible: false
categories:
  - Blog
tags:
  - Agentic
toc: true
classes: wide
---

# Meine Hypothesen
* **Flut an generiertem Code**: KI-Agenten erzeugen riesige Pull Requests (oft  1.000+ Zeilen Code), was Entwickler beim manuellen Prüfen überfordert.
  * Entwickler schaffen ca 200-400 LOC pro Stunden, können das aber nicht länger als 1,5 durchhalten und brauchen Pause 
  * ein Pullrequest von 5000 Zeilen in 1 Tag erzeugt benötigt, dann mind. 2 Tage zum Reviewen
  * Streng genommen sogar das doppelte, weil der Entwickler der den Code erzeugen lies UND ein weitere Entwickler müssen den Code reviewen , wenn man weiterhin traditionell arbeiten will , also brauchen wir fürs review 4 Tage. 
  * der Alltag eines Entwickler würden dann zu 80% nur noch aus Code reviews bestehen. -> unrealistisch.
* also Codereview muss drastisch vereinfacht werden, z.B. durch
  * coding agents selbst (mit review- skills)
  * oder andere Ideen wie die von Viktor Rentea 
