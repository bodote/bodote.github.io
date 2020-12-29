---
title: "Test Driven Development mit Angular Folge 6-10"
date: 2020-12-08 
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

[Hier geht's zu den ersten 5 Folgen](../TDD-mit-Angular)

## Aufgabe 6
Legen wir unsere `FavoriteMovieComponent` zur Seite und widmen uns jetzt dem `FavoriteMovieService`. Services sind in Angular in der Regel mit dem `HttpClientModule` und dessen `HttpClient` implementiert. 

### Hilfreiche Hinweise:
* Passend zu `HttpClientModule` gibt es ein `HttpClientTestingModule` welches man in `jasmine` Tests zusammen mit dem `TestBed` verwenden kann. 
*  Das kann man dadurch erreichen, dass man dem Service, der zu testen ist,   statt dem "nomalen" `HttpClient` den speziellen `HttpTestingController` unterschiebt, sprich: `inject`-ed . 
* Dazu muss du im `*.spec.ts` die `TestBed`-Configuration mit einem zusätzlichen `imports:` ergänzen: 
```typescript
import {HttpClientTestingModule } from '@angular/common/http/testing';
//...
TestBed.configureTestingModule({
      imports: [HttpClientTestingModule]
    });
//...
``` 
* Damit kannst du Antworten der Remote-Rest-Serivces mocken und zusätzlich prüfen, ähnlich einem `spy`, ob und wie der `HttpClient` von deinem Service benutzt wurde. Lass dir vom `TestBed` einen `HttpTestingController` geben, verwende davon `expectOne()` und dessen Return-Objekt `TestRequest`
### Aufgabestellung:
* Teste, ob unser `FavoriteMoviesService` , die Favorite Movies per Observable zurückgibt und 
* ob er dazu die richtige URL mit der richtigen HTTP-Methode (hier: `GET`) aufruft und 
* Teste ob Fehler in der 'HTTP RESPONSE'  von `FavoriteMoviesService` zurückgegeben werden und ob diese gleichzeitig auf die Console geloggt werden.
* wenn diese Tests "grün" sind , dann teste wieder **alle bisherigen Tests**. Falls einige jetzt wieder "rot" sind , fixe diese. 
### Lösung Aufgabe 6 
{% include video id="f_aXwbDks0c" provider="youtube" %} 
* [Link zum Video](https://youtu.be/f_aXwbDks0c)
* [Lösung zu Aufgabe 6](https://github.com/bodote/tdd-angular/tree/v1.6) 
* [Feedback und Kommentare](https://github.com/bodote/bodote.github.io/discussions)


## Aufgabe 7
Unser geplantes Backend ist leider etwas unzuverlässig, daher wollen wir genau 'n' Wiederholversuche für jeden ServiceRequest machen. Erst wenn der 'n'-te Versuch auch fehlschlägt, dann erst soll der Fehler nach oben weitergereicht und geloggt werden.
* Welche Testfälle benötigen wir ? Beginne mit 2 Wiederholungsversuchen (also 'n'=2) und verallgemeinere dann.
* Tip : du musst jetzt mehrmals  `TestRequest.flush()` verwenden.
* die Anzahl der Wiederholungen soll im environment configurierbar sein.
### Lösung Aufgabe 7 
{% include video id="hZQQQTCmO_w" provider="youtube" %} 
* [Link zum Video](https://youtu.be/hZQQQTCmO_w)
* [Lösung zu Aufgabe 7](https://github.com/bodote/tdd-angular/tree/v1.7) 
* [Feedback und Kommentare](https://github.com/bodote/bodote.github.io/discussions)


## Bonusfrage zu Aufgabe 7
Was wenn der Externe HTTP-Service selbst keine Fehlermeldung sendet, sondern erst gar nicht erreicht werden kann (z.B. überhauptkeine Netzwerkverbindung besteht)?
* Tip : statt `TestRequest.flush()` kann man hier `TestRequest.error()` verwenden um eine solchen Fehlermodus zu simulieren. Siehe auch [ErrorEvent](https://developer.mozilla.org/en-US/docs/Web/API/ErrorEvent)
### Lösung Bonunsfrage 7
* [Lösung zu Bonus-Aufgabe 7](https://github.com/bodote/tdd-angular/tree/v1.7.1) 
* [Feedback und Kommentare](https://github.com/bodote/bodote.github.io/discussions)


## Aufgabe 8
Kommen wir zurück zu unserer `FavoriteMoviesComponent`. Wir wollen jetzt nicht einfach eine Liste der Filme ausgeben, sondern jeder Spielfilm soll mit einer eigenen "Presentation" -Component dargestellt werden. Diese Componente nennen wir  `FavoriteMovieComponent` (also ohne das "s" ). Was diese `FavoriteMovieComponent` macht und wie sie implementiert ist, das ist uns im Moment unwichtig.
Wir wollen aber testen, dass unsere bestehende `FavoriteMoviesComponent` jetzt für jeden Film die untergeordnete  `FavoriteMovieComponent` verwendet. Diese soll den `selector` `favorite-movie` nutzen und der soll statt  des bisherigen Listenelements `<li>` eingesetzt werden. Außerdem wollen wir testen, dass wir dieser `FavoriteMovieComponent` den Name des Films auch korrekt übergeben.

Mit anderen Worten:
Lege eine neue Componente "favorite-movie" an (mit `ng g c`) und definiere dort `selector: 'favorite-movie'` und `@Input() movieName: string;`
Die sonstige Implementierung und ebenso das HTML-Template von `FavoriteMovieComponent` interessiert uns aber nicht weiter.

Weil wir in unseren Tests in `favorite-movies.component.spec.ts` aber weiterhin nur echte Unittests und keinen Integrationstest haben wollen, sollten wir die `FavoriteMovieComponent` mit Hilfe des npm - Packages `ng-mocks` durch eine MockComponent ersetzten. Daher installiere zunächst dieses Package mit `npm install ng-mocks` in unserem Demo-Projekt.

### Aufgabenstellung:
1. Ändere unsere bisherigen Tests in `favorite-movies.component.spec.ts` so, dass satt dem `<li>`mit einem Spielfilmname, das `<favorite-movie>`-Element erwartet wird.
2. Ändere den Test so , dass geprüft wird, ob auch der Parameter `FavoriteMovieComponent.movieName` von `FavoriteMoviesComponent` korrekt übergeben wird.
3. Ändere die Implementierung oder das Html-Template der `FavoriteMoviesComponent` bis alle Tests wieder grün sind.
4. Verständnissfrage: Was hilft uns das ng-mocks-Package mit der MockComponent() überhaupt, wo wir doch in unserem Unittest trotzdem von `FavoriteMovieComponent` abhängig sind ? (Antwort in der Docu zu ng-mocks)
### Lösung Aufgabe 8 
{% include video id="a8Go3wm5-Zg" provider="youtube" %} 
* [Link zum Video](https://youtu.be/a8Go3wm5-Zg)
* [Lösung zu Aufgabe 8](https://github.com/bodote/tdd-angular/tree/v1.8) 
* [Feedback und Kommentare](https://github.com/bodote/bodote.github.io/discussions)


## Aufgabe 9
Unsere `FavoriteMovieComponent` soll jetzt einen `Event` emittieren, wenn ein Film gelöscht werden soll. Erweitere die `FavoriteMovieComponent` also um eine `EventEmitter` Property (`@Output...`).
Außerdem soll unser `FavoriteMovieService` eine weitere Methode bekommen, um einen Film löschen zu können. Die Implementierung des Events und der Servicemethode interessiert uns nicht. Vielmehr wollen wir in einem neuen Test prüfen, ob unsere `FavoriteMoviesComponent` (mit "s") auf den `Event` korrekt reagiert. Nämlich indem sie im Service die `deleteMovie`-Methode mit dem richtigen Parameter aufruft.
### Lösung Aufgabe 9 
{% include video id="MFFNtlhl1ek" provider="youtube" %} 
* [Link zum Video](https://youtu.be/MFFNtlhl1ek)
* [Lösung zu Aufgabe 9](https://github.com/bodote/tdd-angular/tree/v1.9) 
* [Feedback und Kommentare](https://github.com/bodote/bodote.github.io/discussions)

## Aufgabe 10
In dieser letzten Aufgabe der Serie wollen wir alles, was wir bis jetzt gelernt haben, nochmal anwenden.
Wir nehmen an, wir wollten noch eine weitere Sub-Komponente entwicklen. Mit dieser Sub-Komponente, die jetzt direkt unterhalb der Überschrift "My Favorite Movies" von unserer "FavoriteMoviesComponent" erscheinen soll, soll der User nach Filmen suchen können, und dann einen der gefunden Filme zu seinen "FavoriteMovies" hinzufügen können. Diese Sub-Komponente soll `SearchMoviesComponent` heißen.
Wobei wir hier **NICHT** die `SearchMoviesComponent` testen oder gar entwickeln wollen! 
Vielemehr überlegen wir uns nur, welche Schnittstellen sie haben müsste, damit wir sie in unsere "smarte" FavoriteMoviesComponent integrieren können. 
Dann erweitern wir unsere Tests für `FavoriteMoviesComponent`, um zu prüfen, ob `FavoriteMoviesComponent` die Subkomponente `SearchMoviesComponent` richtig integriert und verwendet.
### Lösung Aufgabe 10 
{% include video id="nZ6g3AbTd9M" provider="youtube" %} 
* [Link zum Video](https://youtu.be/nZ6g3AbTd9M)
* [Lösung zu Aufgabe 10](https://github.com/bodote/tdd-angular/tree/v1.10) 
* [Feedback und Kommentare](https://github.com/bodote/bodote.github.io/discussions)


## Feedback und Kommentare:
Bitte gib mir dein Feedback! Das hilft uns sehr das Tutorial und die Videos noch besser zu machen.

[Hier gehts zu Feedback und Kommentare](https://github.com/bodote/bodote.github.io/discussions) 