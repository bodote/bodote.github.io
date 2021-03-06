---
title: "Test Driven Development mit Angular Folge 1-5"
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
oder verwende `ng new tdd-angular` und reduziere dann `src/app/app.component.html` auf ein Minimum , lösche alles und setzte  

```html
<div class="content"> 
  <span>{{ title }} app is running!</span>
</div>
``` 
ein.

## Aufgabe 1
* füge eine Componente namens "favorite-movies" hinzu ( z.B. mit `ng g c ...`). Die Componente `FavoriteMoviesComponent` soll eine Headline mit dem Titel "My Favorite Movies" anzeigen. 
* **STOP**: noch nicht `FavoriteMoviesComponent` oder das Template ändern, sondern
  * nur Componente  anlegen (ggf. mit **leeren** Methoden/Properties)
  * dann den Test schreiben , bzw den Test  in `favorite-movies.component.spec.ts` ergänzen!
  * dann Lösung implementieren; also erst jetzt das Template `favorite-movies.component.html` ändern bis der Test grün ist.
* Tip: arbeite mit `fixture.debugElement.query(...)` oder `fixture.debugElement.queryAll(...)`
### Lösung zu Aufgabe 1
{% include video id="p4kpUTBmYq0" provider="youtube" %} 
* [Link zum Video](https://youtu.be/p4kpUTBmYq0)
* [Lösung im Git Repo](https://github.com/bodote/tdd-angular/tree/v1.1)
* [Feedback und Kommentare](https://github.com/bodote/bodote.github.io/discussions)



## Aufgabe 2
* Wir planen, dass die `FavoriteMoviesComponent`  eine Liste der Movies als property vom typ `sting[]` bekommen soll. Diese Property soll später mal von außerhalb der  `FavoriteMoviesComponent` (z.B. mit einem `@Input()`-Decorator) gesetzt werden können. Teste, dass diese Liste deiner Liebligsfilme, wenn sie nicht `undefined` ist, auch im HTML unterhalb der Headline aus Aufgabe 1 angezeigt wird.
* **STOP**: noch nicht die Lösung in `FavoriteMoviesComponent` oder im  Template einbauen, denke nicht mal darüber nach! Sondern:
  * überlege welche Klasse(n), Methode(n), oder Properties (**OHNE** Initialisierung!), brauchst du für den Test?
  * dann den Test schreiben!
  * dann die Implementierung bis Test grün ist
* Tip: wenn  `describe` oder `it` umbenannt wird in  `fdescribe` oder `fit`  werden  **NUR** diese ausgeführt und vor allem sieht man auch die gerenderte Ausgabe des jeweiligen TestBeds in Browser!
### Lösung zu Aufgabe 2
{% include video id="pozhRdiXkI0" provider="youtube" %} 
* [Link zum Video](https://youtu.be/pozhRdiXkI0)
* [Lösung im Git Repo](https://github.com/bodote/tdd-angular/tree/v1.2) (Anmerkung zu Lösung: `@Input()` vor der `favoriteMovies` property der Klasse `FavoriteMoviesComponent` ist für den Unittest unnötig, geht auch ohne, stört aber auch nicht) 
* [Feedback und Kommentare](https://github.com/bodote/bodote.github.io/discussions)

## Aufgabe 3
* nehmen wir an die `favoriteMovies` sollen alternativ auch durch einen `Service` asynchron bereit gestellt werden. Erzeuge den (leeren) service mit `ng g s favorite-movies`. 
* Die Idee ist: wenn unsere Componente bei ihrer Initialisierung in ihrer Properity `favoriteMovies` **kein** String Array vorfindet, nur dann soll alterntiv der Service gerufen werden.
* Teste, ob der Service richtig von der `FavoriteMoviesComponent` verwendet wird, (d.h. du sollst **NICHT** den Service selbst testen, nur seine korrekte Verwendung!). Dazu den Service "mocken" und prüfe, ob er richtig aufgerufen und verwendet wird.
* Teste, ob unsere `FavoriteMoviesComponent` die aus dem Observable empfangen Daten sich auch "merkt"! 
* Tip: verwende `spyOn()`
* refactoriere ggf. den Code, sodass auch die Test aus den ersten 2 Aufgaben wieder laufen
### Lösung zu Aufgabe 3
{% include video id="s87D_oSc1-o" provider="youtube" %} 
* [Link zum Video](https://youtu.be/s87D_oSc1-o)
* [Lösung im Git Repo](https://github.com/bodote/tdd-angular/tree/v1.3)
* [Feedback und Kommentare](https://github.com/bodote/bodote.github.io/discussions)

## Aufgabe 4
Vermutlich hast du in Aufgabe 3 in der `ngOnInit()` methode auf das `Observable` , welches du von `FavoriteMovieService` bekommst direkt subscribed, richtig ?
Wenn ja , dann 
* ändere den Code, sodass du in `ngOnInit()` nur das `Observable` selbst holst und es als solches in `FavoriteMoviesComponent` als property speicherst (Verwende auch die übliche Schreibweise der Property mit dem "$" am Ende). 
* Laufen die Tests noch alle ?
* Eigentlich müsste jetzt zwar der der neue Test auf Aufgabe 3 noch grün sein, aber der Test aus Aufgabe 2 funktioniert nicht mehr, Jedenfalls , wenn du in der `ngOnInit()` methode direkt auf das `Observable` subscribed hattest und dir nur das Ergebniss `<string[]>` der Movies gemerkt hattes. 
* Du musst also jetzt noch den Test aus Aufgabe 2 Anpassen, und vor allem dein Template ändern, damit es direkt das `Observable<string[]>`  statt dem `<string[]>` verwendet. **TIP**: verwende eine sogenannte "async pipe" mit `*ngIf = "myobservable$ | async as myArray"`
### Lösung zu Aufgabe 4
{% include video id="bnHbEJGnkMk" provider="youtube" %} 
* [Link zum Video](https://youtu.be/bnHbEJGnkMk)
* [Lösung im Git Repo ](https://github.com/bodote/tdd-angular/tree/v1.4)
### Bonusaufgabe
* was passiert, wenn du im gerade erstellten Unittest hier:
```typescript
const favMovServSpy = spyOn(favoriteMoviesService, 'getFavoriteMovies')
        .and.returnValue(of(favoriteTestMovies))
```
eine Verzögerung mit `.pipe(delay(100))`in das Test-Observables einbaust ? :
```typescript
const favMovServSpy = spyOn(favoriteMoviesService, 'getFavoriteMovies')
        .and.returnValue(of(favoriteTestMovies).pipe(delay(100)))
```
Hinweis : Ergänze oben im *.spec.ts:  `import { delay } from 'rxjs/operators';`
### Lösung zu Bonus-Aufgabe 4
{% include video id="UiZbXSXkPR0" provider="youtube" %} 
* [Link zum Video](https://youtu.be/UiZbXSXkPR0)
* [Feedback und Kommentare](https://github.com/bodote/bodote.github.io/discussions)

## Aufgabe 5
Was ist aber, wenn das `Observable` aus unserem `FavoriteMovieService`, das uns die 'Favorite Movies' liefern soll, einen Fehler wirft ?
In diesem Fall soll in der Browser-View nach der Überschrift an Stelle der Liste der Filme eine Fehlermeldung angezeigt werden. Die Fehlermeldung soll im HTML mit der CSS-Klasse `error` versehen werden (z.B. weil unser Stylesheet einen Text mit dieser `error`-Klasse rot anzeigen wird ).
* Wie kannst du das im Test "simulieren" ? Hinweis : verwende wieder einen `spy`
* und wie kannst du im Test abtesten ob deine `FavoriteMoviesComponent` den Fehler korrekt verarbeitet und auch in der Browseransicht richtig anzeigt ?
* Bonusfrage: Der Messagetext der Observerfehlermeldung soll nicht direkt angezeigt 
* Hinweis: das `fixture.detectChanges()` darf jetzt NICHT mehr im `beforeEach()`, sondern erst in den eigentlichen Unit-Tests und dort im `//act`-Teil ausgeführt werden. 
### Lösung zu Aufgabe 5
{% include video id="hTxUyh1evcg" provider="youtube" %} 
* [Link zum Video](https://youtu.be/hTxUyh1evcg)
* [Einfache Lösung zu Aufgabe 5](https://github.com/bodote/tdd-angular/tree/v1.5.1) 
werden, sondern eine andere, für den User verständlichere Meldung.
* [Bessere Lösung zu Aufgabe 5](https://github.com/bodote/tdd-angular/tree/v1.5.2)
* [Feedback und Kommentare](https://github.com/bodote/bodote.github.io/discussions)

[Weiter gehts hier](../TDD-mit-Angular6-10)

## Feedback und Kommentare:
Bitte gib mir dein Feedback! Das hilft uns sehr das Tutorial und die Videos noch besser zu machen.

[Hier gehts zu Feedback und Kommentare](https://github.com/bodote/bodote.github.io/discussions) 