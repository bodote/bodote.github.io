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
## Aufgabe 2
* Angenommen die neue Componente hätte schon eine Liste der Movies bekommen (z.B. von der Parent-Component an die `FavoriteMoviesComponent`, in dem dessen property mit einem `@Input()` Decorator versehen wird, oder auch durch einen Service), teste, dass diese auch angezeigt werden.
* Tip: wenn  `describe` oder `it` umbenannt wird in  `fdescribe` oder `fit`  werden  **NUR** diese ausgeführt und vor allem sieht man auch die gerenderte Ausgabe des jeweiligen TestBeds in Browser!
* Anmerkung: `@Input()` vor der `favoriteMovies` property der Klasse `FavoriteMoviesComponent` ist für den Unittest unnötig, geht auch ohne
## Aufgabe 3
* nehmen wir an die `favoriteMovies` sollen durch einen `Service` asynchron bereit gestellt werden. Teste ob der Service richtig verwendet wird. Dazu den Service "mocken" und prüfe ob er richtig aufgerufen wurde.
* refactore den gesamten Code, sodass auch die Test aus den ersten 2 Aufgaben wieder laufen
* Zusatzfrage: kann man die Componente FavoriteMoviesComponent so bauen , dass sie automatisch **entweder** mit `@Input()` Decorator **oder** mit dem `Service` funktioniert? Wenn ja wie ?



## Lösungen
sind [hier](https://github.com/bodote/tdd-angular) zu finden und zwar je Aufgabe ein git-Tag:
* Aufgabe 1 <=> v1.0, 
* Aufgabe 2 <=> v1.2, z.B.: [Lösung zu Aufgabe 2](https://github.com/bodote/tdd-angular/tree/v1.2)
* Aufgabe 3 <=> v1.3, 
* etc.