---
title: "TDD Where it did go wrong"
date: 2023-02-12
published: false
visible: true
categories:
  - Blog
tags:
  - TDD
toc: true
classes: wide
---

# When TDD might not be a good fit
## Requirements are not stable
* Frontend keeps changing, due to user feedback
* implementing a prototype, for which the requirements are not yet clear
* startup, testing new Ideas,
* not Enterprise software (not accounting etc. )
* Sozial Media in general ? because user base can grow fast , but also shrink fast if users just don't like it the way it is any more
* hypothesis: some programmers minds/characters fit better with TDD than others 


# TDD the wrong way
* testing implementation details, that may change, leads to broken tests, that needs to be fixed
* too many mocks, 
* not testing the public API of a module but instead keeping a 1:1 relationship between test class and implementation class
* TDD can lead to bad design, e.g.  too much layers of unnecessary abstraction just to be able to test intermediate results, which makes source code hard to read, instead of going for more cohesion, which might be much easier to understand.
* is it really a good idea, when the angular CLI automatically generates a test-file for each component ?
* going for too much abstraction: it is not realistic in any way that you just can swap out webservice for a in memory data base (or vice versa) so why make an repository abstraction in the first place?


# what is the actual purpose of TDD ?
* being able to confidently add new features (without breaking the old ones) TTD is one way, but not the only way to reach that 
* proof that the software does the right thing, where it is important, and errors are catastrophic in some way (accounting, controlling machines that could do harm to people, organizing companies: offers, orders, invoices )
* to get feedback for the developer, in terms of correctness, but also in term of good (oder bad) design.

# controversial and provocative arguments
* it is better to offload the responsibility for the software quality to some other guys (the "QS" - department)
* 