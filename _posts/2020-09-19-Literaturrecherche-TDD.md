---
title: "Literaturrecherche zu TDD"
date: 2020-10-12
categories:
  - blog
tags:
  - TDD
  - Test Driven Development
toc: true
classes: wide
---
# Bücher:
Ich bin ja ein enthusiastischer Befürworter von Test Driven Design (TDD), insbesondere von dem "test first" Ansatz. Daher hat es mich einfach interessiert, was denn andere Autoren und auch (aber nicht nur) die wissenschaftliche Literatur zu dem Thema hergibt. Hier ist, was sich dazu gefunden habe:[^1] 

## Aus [Langlebige Softwarearchitekturen](https://langlebige-softwarearchitekturen.de) 

### Abschnitt 9.1.1: 

\"Für Klassen, die in **Zyklen** sind, existieren in den meisten Systemen
keine direkten Unit-Testklassen. Wollte man die Unit Tests programmieren, 
müsste man alle im Zyklus verflochtenen Klassen durch einen Mock
ersetzen oder Objekte von ihnen erzeugen. Das ist sehr viel Aufwand,
den die meisten Entwicklungsteams und Projektleiter scheuen.\"[^2]

## Aus [Test-Driven Java Development - Second Edition](https://www.packtpub.com/product/test-driven-java-development-second-edition/9781788836111) 

### Kapitel 1 , Abschnitt \"Why TDD?\": 

\"It\'s not an easy thing to master TDD. Even after learning all the
theory and going through best practices and anti-patterns, the journey
is only just beginning. **TDD requires time and a lot of practice**. It\'s a
long trip that does not stop with this book. As a matter of fact, it
never truly ends. There are always new ways to become more proficient
and faster. However, even though the cost is high, the benefits are even
higher. **People who have spent enough time with TDD claim that there is
no other way to develop a software.** We are one of them and we\'re sure
that you will be too.\"[^3]



# Wissenschaftliche oder zumindest systematische Studien zu TDD {#wissenschaftliche_studien_zu_tdd}


## [Assessing test-driven development at IBM](https://collaboration.csc.ncsu.edu/laurie/Papers/MAXIMILIEN_WILLIAMS.PDF): 

"... we reduced our **defect rate by about 50 percent** compared to a
similar system that was built using an ad-hoc unit testing approach. The
project completed on time with **minimal development productivity impact.**
Additionally, the suite of automated unit test cases created via TDD is
a reusable and extendable asset that will continue to improve quality
over the lifetime of the software system. The test suite **will be the basis for quality checks** 
and will serve as a quality contract between all members of the team."

## [Evaluating the Efficacy of Test-Driven Development: Industrial Case Studies (Microsoft)](https://d1wqtxts1xzle7.cloudfront.net/36509027/fp17288-bhat.pdf?1423032149=&response-content-disposition=inline%3B+filename%3DEvaluating_the_Efficacy_of_Test_Driven_D.pdf&Expires=1599907639&Signature=RuaKEjh7AbrkimLa5LGjb6zOpojv18srJrYQO7ONLNjWm586g6nxlDjGnYgubwIFYYp5fNkQulFn6YD3wpvud5bBhvwkO4nOOFMYyhATLdvHjHtW3vzm6ncsuqgwYTIKtrxbxAd7lQiEiue~D300FsgSLK6ZUk9DOssTqS0NZry6syc9I6IQYR6H2BRcnzf9oxvCTBWPzjSEBPi2cqYpyKbF1Y322XtLj7fdNTu8IVkmUULxwH3R1GVsEZrdpOAOJpM0b1ZAsJZEI0K3hiv~ENiV79hUjoyRu5xLaDeDWA4Nhg4Q-J8Zu8UQ18hQEjl0dOZnq7o4Xq~2-8jbuzDxIQ__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA) 

-   2,6-4,2 mal mehr Bugs , wenn KEIN TDD verwendet. oder anders
    gerechnet **Bugrate sinkt mit TDD um 62%-77%** .
-   15% -35% mehr Zeit für TDD notwendig.

" The results summarized ... indicate that while the development of
both the systems utilizing TDD took extra time upfront the **resulting quality was higher** 
than teams that adopted a non-TDD approach by an
order of at least two times. "

## Metastudie, die 6 unterschiedliche Studien ausgewertet hat: [Does Test-Driven Development Really Improve Software Design Quality?](https://digitalcommons.calpoly.edu/cgi/viewcontent.cgi?article=1027&context=csse_fac) 

"... Our results indicate that **test-first programmers** are more likely
to write software in more and smaller units that are **less complex and more highly tested** ...."

## [An Experimental Evaluation of the Effectiveness and Efficiency of the Test Driven Development](https://ieeexplore.ieee.org/abstract/document/4343756) 

"Our results suggest that **TDD** helps in **reducing overall development effort** 
and **improving developer's productivity** whereas the code quality
seems to be affected by the actual testing efforts applied during a
development-style."

## Metastudie: [How Effective is Test-Driven Development?](https://www.researchgate.net/profile/Burak_Turhan/publication/258126622_How_Effective_is_Test_Driven_Development/links/54e794320cf27a6de10a8afe/How-Effective-is-Test-Driven-Development.pdf) 

**"Is it for everyone?"**

"One basic fact on which almost everyone agrees is that **TDD is difficult to learn**. 
It involves a steep learning curve that requires skill,
maturity, and time, particularly when developers are entrenched in the
code-then-test paradigm. Better tool support for test-case generation
and early exposure in the classroom to a test-then-code mentality may
encourage TDD adoption."

**"Could it be addictive?"**

"Personal communications with TDD developers suggest that it is an addictive practice. 
It **changes the way people think** and their approach
to coding in a way that is difficult to roll back. Therefore, leaving
TDD practices may be as difficult as adopting them."

**Fazit: Empfehlung für TDD**

## [Comparing the Defect Reduction Benefits of \... Test-Driven Development](http://ibiai.mg.gov.br/wp-content/uploads/2019/08/05750007-1.pdf) 

"TDD has several purported benefits---only one of which is software
defect reduction ... We found that **code inspection \[=review?\] is more effective than TDD** 
at reducing defects, but that **code inspection is also more expensive** 
to implement. We also found some evidence to indicate that TDD
may result in an implementation cost savings, ..."

## [Test-Driven Development](https://link.springer.com/book/10.1007%2F978-3-642-04288-1) 

Empirical studies by Madeyski (Madeyski, 2010a) showed that TDD is
**better** in producing **loosely coupled** software in comparison with
traditional test last software development practice.

# Sonstige Links:
## aus [Large-Scale Scrum >>LeSS<<](https://less.works/de/less/technical-excellence/test-driven-development):

"We **rarely** meet people who were able to adopt this by **self-education**. Most developers **need a coach** to pair-program with them for days or weeks."

und: 

"Test-driven development might be the **hardest agile practice** to adopt, but it is also **one of the biggest opportunities** for improving the quality of the design and code. "

und weiter:

"TDD can help improve the architecture of a system. How?

When we are coaching, a frequent request is help for dealing with our client’s “inflexible architecture.” This most often boils down to problems in **high coupling between components** —a common problem in legacy code written **without TDD** because the original developer did not try to test the component in isolation.

On the other hand, when a developer creates a new component (such as a class) **with TDD**, or refactors a legacy component to be unit-testable, they must break the dependencies of that component so that it is testable in isolation. That requires **designing (or refactoring) for dependency** injection and **increased use of mechanisms for flexibility**: interfaces, polymorphism, design patterns, dependency injection frameworks, function pointers, and more.

In this way, **TDD** encourages **lower coupling** and simple, flexible configuration—qualities of a **good architecture.**"

********************

Fußnoten: 

[^1]: Angeregt wurde ich dazu übrigens, als ich das Buch [Langlebige Softwarearchitekturen](https://langlebige-softwarearchitekturen.de) von Carola Lilienthal las. Sie hat nämlich an einige Stellen auf auf systematische Studien verwiesen, die Ihre jeweilige Aussagen im Buch belegen sollen. Übrigens schreibt sie auch sehr positiv über TDD in dem Buch, wie man hier gleich in der ersten Fundstelle sieht.

[^2]: Ich hoffe, wir sind uns einig, dass Zyklen, egal ob auf
    Modul/Package-Ebene oder auf Ebene von Klassen innerhalb eines
    Packages böse sind. Daher, heißt das 
    im Umkehrschluss: wenn ich mit TDD anfange, kann mir das
    nicht passieren. Im Gegenteil: TDD hindert mich direkt daran, solche
    Fehler zu machen und zwingt mich, vor schreiben von Classen und
    Methode mir Gedanken über die Microarchitektur (also die Architektur
    von Klassen, die zu einem Bounded Context gehören, die zu einem
    Package gehören oder sonst eng zusammengehören.)

[^3]:  den fett gedruckte Satz kann ich aus eigener Erfahrung bestätigen.