---
title: "Test Driven Development mit Angular Folge 6-9"
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
Kommen wir zurück zu unserer `FavoriteMoviesComponent`. Wir wollen jetzt nicht einfach eine Liste der Movies ausgeben, sondern jeder Spielfilm soll mit einer eigenen "Presentation" oder "Dumb" -Component, genannte `FavoriteMovieComponent` (also ohne das "s" ) dargestellt werden. Was diese `FavoriteMovieComponent` macht und wie sie implementiert ist, das ist uns im Moment unwichtig.
Wir wollen aber testen, dass unsere bestehende `FavoriteMoviesComponent` jetzt jeden Film als `FavoriteMovieComponent` (mit dessen Selector `favorite-movie`) statt  eines Listenelements `<li>` verwendet  **und** dass diesem `FavoriteMovieComponent` der Name des Films auch korrekt übergeben wird.

Mit anderen Worten:
Lege eine neue Componente "favorite-movie" an (mit `ng g c`) und definiere dort `selector: 'favorite-movie'` und `@Input() favoriteMovie: string;`
Die sonstige Implementierung und ebenso das HTML-Template von `FavoriteMovieComponent` interessiert uns aber nicht weiter.

Weil wir in unseren Tests in `favorite-movies.component.spec.ts` aber weiterhin nur echte Unittests und keinen Integrationstest haben wollen, sollten wir die `FavoriteMovieComponent` mit Hilfe des npm - Packages `ng-mocks` mocken. Daher installierte dieses Package mit `npm install ng-mocks`

### Aufgabenstellung:
1. Ändere unsere Tests in `favorite-movies.component.spec.ts` so, dass satt dem `<li>`mit einem Movie, `<favorite-movie>` erwartet wird
2. Ändere den Test so , dass geprüft wird, ob auch der Parameter `FavoriteMovieComponent.favoriteMovie` von `FavoriteMoviesComponent` korrekt übergeben wird.

## Aufgabe 9
Unsere `FavoriteMovieComponent` soll jetzt auch einen Event emittieren, wenn ein Movie gelöscht werden soll. Erweitere `FavoriteMovieComponent` entsprechend um ein `@Output...`.
Außerdem soll unser `FavoriteMovieService` eine weitere Methode bekommen um einen Movie zulöschen. Die Implementierung des Events und der Servicemethode interessiert uns nicht. Sondern wir wollen in einem neuen Test prüfe, ob unsere `FavoriteMoviesComponent` (mit "s") auf den Event korrekt reagiert indem sie im Service die `deleteMovie`-Methode mit dem richtigen Parameter aufruft.


## Feedback und Kommentare:
Bitte gib mir dein Feedback! Das hilft uns sehr das Tutorial und die Videos noch besser zu machen.

[Hier gehts zu Feedback und Kommentare](https://github.com/bodote/bodote.github.io/discussions) 