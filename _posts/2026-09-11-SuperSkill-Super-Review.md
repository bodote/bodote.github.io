---
title: "Der Super Skill: /super-review"
date: 2026-09-11
published: false
visible: false
categories:
  - Blog
tags:
  - Agentic
toc: true
classes: wide
---
# /super-review [branch] [plan oder issue]

Alles Startet mit einem einfach Prompt z.B. "machen eine Code review der letzten Änderungen"

Ok, aber was, wenn in dem Branch schon mehrer Commits gemacht wurden und du alles in dem Featurebranch reviewen willst: 

> mache eine Code review der ~~letzten Änderungen~~ aller Änderungen in diesem Branch

oder wenn du sogenannten "Stacked Branches" hast : 

> mache eine Code review der ~~letzten Änderungen~~ aller Unterschiede zu  `my_base_branch

Ach so und dann möchte ich vermeiden dass irgendwas geändert wird, ich will ja nur wissen was geändert werden **sollte** : 

> mache eine Code review der  aller Unterschiede zu  `my_base_branch`, aber ändere nichts

Und wäre es nicht praktisch, wenn das ergebniss gleich in einer Markdown datei steht? Fragt sich : soll dieser Report dann mit eingecheckt werden, jedenfalls solange die Findings noch nicht behoben sind ? Wie auch immer du mit deinem Team entscheidest, diese Anweisung muss auch in den Prompt: 

> mache eine Code review der  aller Unterschiede zu  `my_base_branch`, aber ändere nichts und schreibe die Ergebnisse als Markdown nach tmp/review.md

oder besser

>mache eine Code review der  aller Unterschiede zu  `my_base_branch`, aber ändere nichts und schreibe die Ergebnisse als Markdown nach `tmp/review[branch-name].md` 

falls es einen Plan gibt: 

>mache eine Code review der  aller Unterschiede zu  `my_base_branch`, aber ändere nichts und schreibe die Ergebnisse als Markdown nach `tmp/review[branch-name].md` und prüfen ob die Änderungen den `PlanXY.md` befolgen

oder 

>mache eine Code review der  aller Unterschiede zu  `my_base_branch`, aber ändere nichts und schreibe die Ergebnisse als Markdown nach `tmp/review[branch-name].md` und prüfen ob die Änderungen das Ziel und die Akzeptanzkriterien in gitlab issue #123 erfüllen

wie kommt der Coding agent an gitlab issue #123 : schreib einen Skill der dem Coding agent das beibringt z.B. mit der `gitlab` oder `github` CLI , oder per REST API: beides geht du must dem Agent nur sagen welche Variante und natürlich für authentifizierung per API - Key sorgen (am besten du nimmst für den codeing agent einen eigenen API - key , sodass deine Person und dein API- Key in Kommentaren im `gitlab` oder `github` unterscheidbar bleibt.) 

Ach ja und dann haben wir noch vergessen: 

> mache eine Code review.... und du sollst dabei auch die Code Coverage messen und prüfen ob diese über 98% liegt

wo wir schon dabei sind: 

>mache eine Code review.... und prüfen die Guidelines für die Architektur 

(wobei : ist eine deterministische Prüfung mit `Archunit/Spring-Boot-Modulith` oder `Sheriff` für Angular besser?)

und viele weitere Punkte: 
* Sonar-Findings
* TDD eingehalten?
* Tiefe Tests (statt flache)
* code duplication vermeiden
* datenbank migration berücksichtigt?
etc. pp. 

Vermutlich gibt auch einige deutliche Unterschiede der Kriterien zwischen FE und BE in einer Code Review 

Das alles führt zu : 

## 2 Skills für die Reviews 
`/systematic-backend-review` und `/systematic-frontend-review`

## kann ich meinem LLM bei Code Reviews blind vertrauen ?
vermutlich nicht. zunächst. 
* Schau dir den Code selbst noch an: findet der Coding Agent mehr als du , oder weniger, oder anderen Punkte?
* "übersieht" er immer wieder die gleiche Art von Fehlern -> Skills ergänzen
* können unterschiedliche LLMs unterschiedlich gut Fehler finden ? -> probiere es aus: gleiche Codereview mit selben Skills und selben Codeänderung, aber 2 oder 3 verschiedenen LLMs  
* vergleiche die Findings der LLMs und natürlich mit deinen eigenen Findings
* finden 3 LLMs mehr als du ? übersehen Sie immer noch PUnkte obwohl du in den Skills schon extra drauf hinweist?
   * ja: dann machst du weiter manuelle Code reviews und verbesserst die Skills oder testest andere LLMs
   * nein: dann verschwende nicht deine teuere Zeit und lasse die Codings Agents für dich arbeiten

Ok, sagts du , aber ist doch viel Arbeit die code review 2 oder 3 mal zu starten  und dann die ganzen Findings zu sichten und überlappunten und Widersprüche zu finden

# Die Super-review
mach dir einfach einen neuen Skill der 
* mehrere Agenten mit mehrern LLMs für code review und BE und FE getrennt startet
* der die Ergebnisse für dich sichtet und Duplication und Widersprüche herausarbeiten
und packe das alles eine deinen neuen `/super-review` Skill

## und dann ?
2 Möglichkeiten: 
1. es ist dein Code und du möchtest die gefunden Punkte gleich beseitigen lassen
2. es ist nicht dein Code und du möchtest deinen Kollegen die gefunden Punkte geben

## Beheben der Findings
das lassen wir vom coding agent machen.

> behebe das Finding "F2" 

aber woher wissen wir dass das Problem wirklich gut behoben ist?

> prüfe ob die letzten Änderungen den Fehler XY im `review-findings-merged.md` wirklich behoben sind

reicht da ein LLM ? wir hatten ja schon bemerkt dass verschiedene LLMs verschieden gut darin sind nachträglich Fehler aufzuspüren, also hier auch wieder 2 oder 3 Agents mit verschiedenen Modellen ?


