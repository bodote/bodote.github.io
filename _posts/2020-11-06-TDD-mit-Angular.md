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
Wir verwenden hier aber `jasmine` statt `Jest`
## Setup
```bash
git clone https://github.com/bodote/tdd-angular.git
git checkout v1.0
```
oder verwende `ng new tdd-angular` und reduziere dann `src/app/app.component.html` auf ein Minimum , z.B. Lösche alles und setzte  `<div>{{ title }} app is running!</div>` ein.

## Aufgabe 1
* füge eine Componente namens "favorite-movies" hinzu ( z.B. mit `ng g c ...`). Die Componente `FavoriteMoviesComponent` soll später eine Headline mit dem Titel "My Favorite Movies" anzeigen. 
* **STOP**: noch nicht `FavoriteMoviesComponent` oder das Template ändern, sondern zuerst den Test schreiben!
* das heißt für TDD:  schreibe **zuerst** den Test  in `favorite-movies.component.spec.ts` und ergänze **danach** das Template `favorite-movies.component.html` bis der Test grün ist.
* Tip: arbeite mit `fixture.debugElement.query(...)` oder `fixture.debugElement.queryAll(...)`
* [Lösung zu Aufgabe 1](https://github.com/bodote/tdd-angular/tree/v1.1)

## Aufgabe 2
* Wir planen, dass die `FavoriteMoviesComponent`  eine Liste der Movies als property vom typ `sting[]` bekommen soll. Diese Property soll später mal von außerhalb der  `FavoriteMoviesComponent` (z.B. mit einem `@Input()`-Decorator) gesetzt werden können. Teste, dass diese Liste deiner Liebligsfilme, wenn sie nicht `undefined` ist, auch im HTML unterhalb der Headline aus Aufgabe 1 angezeigt wird.
* **STOP**: noch nicht `FavoriteMoviesComponent` oder das Template ändern, sondern zuerst den Test schreiben!
* Tip: wenn  `describe` oder `it` umbenannt wird in  `fdescribe` oder `fit`  werden  **NUR** diese ausgeführt und vor allem sieht man auch die gerenderte Ausgabe des jeweiligen TestBeds in Browser!
* [Lösung zu Aufgabe 2](https://github.com/bodote/tdd-angular/tree/v1.2) (Anmerkung zu Lösung: `@Input()` vor der `favoriteMovies` property der Klasse `FavoriteMoviesComponent` ist für den Unittest unnötig, geht auch ohne, stört aber auch nicht) 

## Aufgabe 3
* nehmen wir an die `favoriteMovies` sollen durch einen `Service` asynchron bereit gestellt werden. Erzeuge den (leeren) service mit `ng g s favorite-movies`. Teste ob der Service richtig von der `FavoriteMoviesComponent` verwendet wird, (d.h. du sollst **NICHT** den Service selbst testen, nur seine korrekte Verwendung!). Dazu den Service "mocken" und prüfe, ob er richtig aufgerufen wurde. 
* Tip: verwende `spyOn()`
* refactoriere den gesamten Code, sodass auch die Test aus den ersten 2 Aufgaben wieder laufen
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

## Aufgabe 6
Wir testen hier den `FavoriteMovieService`. Services sind in Angular in der Regel mit dem `HttpClientModule` und dessen `HttpClient` implementiert. Passend zu `HttpClientModule` gibt es ein `HttpClientTestingModule` welche man in `jasmine` Tests zusammen mit dem `Testbed` verwenden kann, in dem deinem Service statt dem `HttpClient` ein spezieller Test-`HttpClient` untergeschoven wird. Damit kann man Antworten der Remote-Rest-Serivces mocken und zusätzlich prüfen ob und wie der `HttpClient` von deinem Service benutzt wurde.
* Teste ob unser `FavoriteMoviesService` die richtigen URL mit der richtigen HTTP-Methode (z.B. hier `GET`) aufruft und die dem via `HttpClientTestingModule` untergeschobene `HTTP-RESPONSE` richtig verarbeitet. 
* Teste konkret ob Fehler in der `HTTP-RESPONSE` richtig von `FavoriteMoviesService` verarbeitet werden.
* wenn dieser Test "grün" ist , dann teste wieder **alle bisherigen Tests**. Falls einige jetzt wieder "rot" sind , fixe diese. 
* Tip: evtl. musst du `TestBed.configureTestingModule..` ergänzen.

## Aufgabe 7
Genau betrachtet, war die Aufgabe 6 "geschenkt" weil wir eigentlich nur getestet haben ob das Angular Observable Fehler korrekt meldet, was natürlich der Fall ist. Wir haben aber an unserem `FavoriteMovieService` eigentlich gar nicht ändern müssen, um den Test "rot" zu bekommen, richtig ?
Unser geplantes Backend ist leider etwas unzuverlässig, daher wollen wir genau 3 Wiederholversuche für jeden ServiceRequest machen. Erst wenn der 3. Versuch auch fehlschlägt, dann soll der Fehler nach oben weitergereicht werden.
* Was bedeutet das für unseren Test ? 
* nachdem der Test aus Aufgabe 6 ja streng genommen unser Code bisher gar nicht getestst hat (sondern nur das Angular-Interne Observable-Fehlerhandling), wollen wir diese Test jetzt auf 3 Versuche erweitern. 
* Tip : du musst jetzt 3 mal  `req.flush()` verwenden.

## Aufgabe 8
Was wenn der Externe HTTP-Service selbst keine Fehlermeldung sendet, sondern erst gar nicht erreicht werden kann (z.B. überhauptkeine Netzwerkverbindung besteht)?
* Tip : statt `req.flush()` kann man hier `req.error(errorEvent)` verwenden um eine solchen Fehlermodus zu simulieren.

## Aufgabe 9
Was , wenn die ersten 2 Versuche fehlschlagen, der dritte aber erfolgreich ist? Schreiben für diesen Fall einen Test
* refactoriere die Test um unnötige Codeduplizierungen zu beseitigen.


