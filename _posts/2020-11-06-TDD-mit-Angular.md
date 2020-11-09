---
title: "Test Driven Development mit Angular"
date: 2020-11-08 
categories:
  - blog
tags:
  - TDD
  - Test Driven Development
toc: true
classes: wide
---
# Angular TDD Workshop
Diese Angular-TDD-Workshop ist eine Variante von diesem [Workshop](https://itnext.io/test-driven-development-in-an-angular-world-92c0c42a54d0)
Wir verwende hier aber `jasmine` statt `Jest`
## Setup
```bash
git clone git@github.com:bodote/tdd-angular.git 
git checkout v1.0
```
## Aufgabe 1
* füge eine Compomenten namens "favorite-movies" hinzu die eine Headline mit dem Titel "My Favorite Movies" anzeigt. 
* das heißt für TDD:  schreibe zuerst den Test  in `favorite-movies.component.spec.ts` und ergänze dannach das Template `favorite-movies.component.html` bis der Test grün ist.
* [Lösung zu Aufgabe 1](https://github.com/bodote/tdd-angular/tree/v1.1)

## Aufgabe 2
* Angenommen die neue Componente hätte schon eine Liste der Movies bekommen (z.B. von der Parent-Component an die `FavoriteMoviesComponent`, in dem dessen property mit einem `@Input()` Decorator versehen wird, oder auch durch einen Service), teste, dass diese auch angezeigt werden.
* Tip: wenn  `describe` oder `it` umbenannt wird in  `fdescribe` oder `fit`  werden  **NUR** diese ausgeführt und vor allem sieht man auch die gerenderte Ausgabe des jeweiligen TestBeds in Browser!
* Anmerkung: `@Input()` vor der `favoriteMovies` property der Klasse `FavoriteMoviesComponent` ist für den Unittest unnötig, geht auch ohne
* [Lösung zu Aufgabe 2](https://github.com/bodote/tdd-angular/tree/v1.2)
## Aufgabe 3
* nehmen wir an die `favoriteMovies` sollen durch einen `Service` asynchron bereit gestellt werden. Teste ob der Service richtig verwendet wird. Dazu den Service "mocken" und prüfe ob er richtig aufgerufen wurde.
* refactore den gesamten Code, sodass auch die Test aus den ersten 2 Aufgaben wieder laufen
* Zusatzfrage: kann man die Componente FavoriteMoviesComponent so bauen , dass sie automatisch **entweder** mit `@Input()` Decorator **oder** mit dem `Service` funktioniert? Wenn ja wie ?
* [Lösung zu Aufgabe 3](https://github.com/bodote/tdd-angular/tree/v1.3)

## Aufgabe 4
Vermutlich hast du in Aufgabe 3 in der `ngOnInit()` methode auf das `Observable` , welches du von `FavoriteMovieService` bekommst direkt subscribed, richtig ?
Wenn ja , dann 
* ändere den Code, sodass du in `ngOnInit()` nur das `Observable` selbst holst und es als solches in `FavoriteMoviesComponent` als property speicherst (Verwende auch die übliche Schreibweise der Property mit dem "$" am Ende). 
* Laufen die Tests noch alle ?
* Eigentlich müsste jetzt zwar der der neue Test auf Aufgabe 3 noch grün sein, aber der Test aus Aufgabe 2 funktioniert nicht mehr, Jedenfalls , wenn du in der `ngOnInit()` methode direkt auf das `Observable` subscribed hattest und dir nur das Ergebniss `<string[]>` der Movies gemerkt hattes. 
* Du musst also jetzt noch den Test aus Aufgabe 2 Anpassen, und vor allem dein Template ändern, damit es direkt das `Observable<string[]>`  statt dem `<string[]>` verwendet. **TIP**: verwende eine sogenannte "async pipe" mit `*ngIf = "myobservable$ | async as myArray"`
* [Lösung zu Aufgabe 4](https://github.com/bodote/tdd-angular/tree/v1.4)
## Aufgabe 5
Was ist aber, wenn das `Observable`, von dem wir die 'Favorite Movies' bekommen einen Fehler wirft ?
* Wie kannst du das im Test "simulieren" 
* und wie kannst du im Test abtesten ob deine `FavoriteMoviesComponent` den Fehler korrekt verarbeitet und auch in der View richtig anzeigt ?
* [Lösung zu Aufgabe 5 Variante 1](https://github.com/bodote/tdd-angular/tree/v1.5.1)
* [Lösung zu Aufgabe 5 Variante 2](https://github.com/bodote/tdd-angular/tree/v1.5.2)
