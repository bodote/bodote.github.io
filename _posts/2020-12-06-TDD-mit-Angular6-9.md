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

## Aufgabe 8
Kommen wir zurück zu unserer `FavoriteMoviesComponent`. Wir wollen jetzt nicht einfach eine Liste der Movies ausgeben, sondern jeder Movie soll mit einer eigenen (Dumb)-Compoment `FavoriteMovieComponent` (also ohne das "s" ) dargestellt werden. Was diese `FavoriteMovieComponent` macht und wie die implementiert ist, das ist uns im Moment unwichtig. 
Wir wollen aber Testen, dass unsere bestehende `FavoriteMoviesComponent` jetzt jeden Movie als `FavoriteMovieComponent` (mit dessen Selector `kbd-favorite-movie`) statt  eines Listenelements `<li>` verwendet  UND dass diesem `FavoriteMovieComponent` der Name des Movies auch korrekt übergeben wird. 

Mit anderen Worten:
Lege eine neue Componente "favorite-movie" an (mit `ng g c`) und definiere dort `selector: 'kpd-favorite-movie'` und `@Input() favoriteMovie: string;`
Die sonstige Implementierung und ebenso dessn html-template interessiert uns aber nicht weiter.

Weil wir in unserem `favorite-movies.component.spec.ts` aber weiterhin nur echte Unittests und keinen Integrationstest haben wollen, wollen wir die `FavoriteMovieComponent` mit Hilfe des npm - packages `ng-mocks` mocken. Daher installierte dieses Package.

### Aufgabenstellung: 
1. Ändere unsere Test `favorite-movies.component.spec.ts` so dass satt dem `<li>`mit einem Movie, `kbd-favorite-movie` erwartet wird
2. Ändere den Test so , dass auch der Parameter `FavoriteMovieComponent.favoriteMovie` von `FavoriteMoviesComponent` korrekt übergeben wird



## Aufgabe 9
TBD


## Feedback und Kommentare:
Bitte gib mir dein Feedback! Das hilft uns sehr das Tutorial und die Videos noch besser zu machen.

[Hier gehts zu Feedback und Kommentare](https://github.com/bodote/bodote.github.io/discussions) 