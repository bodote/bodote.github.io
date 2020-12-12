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


## Feedback und Kommentare:
Bitte gib mir dein Feedback! Das hilft uns sehr das Tutorial und die Videos noch besser zu machen.

[Hier gehts zu Feedback und Kommentare](https://github.com/bodote/bodote.github.io/discussions) 