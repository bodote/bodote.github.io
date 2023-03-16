---
title: "TDD Where it did go wrong"
date: 2023-02-12
published: true
visible: true
categories:
  - Blog
tags:
  - TDD
toc: true
classes: wide
---
In order to not fall into the confirmation bias fallacy, I volunteered to play the role of a TDD opponent in a Open Space event at our company.

I still think, that TDD is a great tool (if not the greatest) in the software developers tool box, but nevertheless 
what I found was actually quite interesting:


# TDD the wrong way
## ... because of coupling  tests to implementation 
..instead of testing the specification and confirming the behavior:
* some less experienced developers think like: "I can't figure out, how to write tests first, so at least I write it after" , which is NOT a good idea, because it leads to a strong coupling between tests and **implementation** (instead of tests and **specification**)
* testing **implementation** details is generally wrong, because that may or even **should** change, leads to broken tests, that needs to be fixed
* too many **mocks**, seems to be a good indicator of doing it the wrong way
* not testing the **public API** of a module but instead keeping a 1:1 relationship between test class and implementation class
* TDD can lead to **poor design**, e.g.  too much layers of unnecessary abstraction just to be able to test intermediate results, which makes source code hard to read, instead of going for more cohesion, which might be much easier to understand.
* is it really a good idea, when the **angular CLI** automatically generates a test-file **for each component** ?
* going for **too much abstraction**: it is not realistic in any way that you just can swap out webservice for a in memory data base (or vice versa) so why make an repository abstraction in the first place?
* **public methods** or accessors of production classes **only** used in test code
* TDD is the right idea, but most teams get it wrong. the problem is wrong wording wrong mindset because it's not about "tests" it's about "specifications". It's not about testing the code but confirming the behaviour of the system. **BDD** (Behavior Driven Development) was invented to  to teach TDD better.
  * unlike most people think , BDD is **not** about the tools, and its core is **not** about test written in a more natural language (i.e. what **Gherkin** (the language) or **Cucumber** does )

## ...because of chasing the code coverage
* **code coverage** alone is a very bad metric for test quality

## ...because falling in those common TDD traps:
it's too easy to make mistakes when trying TDD:
* the **Liar** : helps code coverage, but does not have any useful assertions. (mostly seen when "cheating" TDD by writing test last, but can be automatically uncovered with "mutation" testing tools.)
* **excessive setup** : sign of poor modularity and poor separation of concerns: test and code highly coupled: test breaks when implementation changes (e.g. to add new features).
* the **Giant** : writing multiple assertions, difficult to understand
* the **Mockery** many mocks, but not actual code, that is tested.
* the **Inspector** violates encapsulation because of e.g. poor use of dependency injection 
  * never compromise encapsulation
  * but at the same time, design for testability, which is NOT she same as compromise encapsulation!
* you **think**, you have mastered TDD, because you can write tests first now without any significant problems,  but in fact half the way is still in front of you yet.


## ... because it's taught the wrong way
* although it seems right to first learn to write tests first on simple examples, and even that seems already hard to learn. But it is a **totally different level** to write tests first for komplex real world business software!
* Many give up on TDD because they don't really experience the benefits of TDD because they don't realize that these are **only to be found at the next level**, of which level they are not even aware of!


# When TDD might not be a good fit
## Requirements are not stable
* Frontend keeps changing, due to user feedback
* its not yet clear how the frontend should look like, developer still figuring out , while he writes the html - code for it
* implementing a prototype, for which the requirements are not yet clear
* startup, testing new Ideas,
* not Enterprise software (not accounting etc. )
* Sozial Media in general ? because user base can grow fast , but also shrink fast if users just don't like it the way it is any more
* hypothesis: some programmers minds/characters fit better with TDD than others 



# What is the actual purpose of TDD ?
* to get feedback for the developer, in terms of correctness, but also in term of good (oder bad) design.
  * how good is that feedback, in what percentage of cases is a green test really telling that there are in fact not bugs ?
* being able to confidently add new features (without breaking the old ones) TTD is one way, but not the only way to reach that 
* proof that the software does the right thing, where it is important, and errors are catastrophic in some way (accounting, controlling machines that could do harm to people, organizing companies: offers, orders, invoices )
* the main point of **soft**ware , is that it should be easy to change, if that is not the case, its not **soft**ware, its **hard**ware 


# Controversial and provocative arguments against TDD
* Isn't it better to offload the responsibility for the software quality to some other guys (the **"QS"-department**) so that I as a developer don't need to bother with that unpleasant task?
* TDD is so successfull, that it give the developer **OVERconfidence**, so that they think, they don't need QA, and ship bad software.
* more , faster and better tests come at a **cost**, but the TDD-proponents seem not to think about that
* TDD leads to **fragile code base**: small changes leads to broken tests and the code base is hard to change and hard to maintain: **true**, if you make the **mistakes listed above**!

# Perspective of a customer or a manager
When you are planning a project and you have only developers that are not experienced in test driven development then you are in big trouble:
* If you choose the test driven development path, then you need a lot of money and a lot of time to bring the developers up to speed in test driven development.
* If you don't do test driven development, then you're also in big trouble because then you'll end up with a really bad code in the long run. 
* So overall, No matter what, you'll always lose.

---

Sources : [TDD, Where Did It All Go Wrong (Ian Cooper)](https://youtu.be/EZ05e7EMOLM), [Is TDD Dead?](https://martinfowler.com/articles/is-tdd-dead/) [Test Driven Development vs Behavior Driven Development](https://youtu.be/Bq_oz7nCNUA) [When Test Driven Development Goes Wrong](https://youtu.be/UWtEVKVPBQ0), [stackoverflow:disadvantages-of-test-driven-development](https://stackoverflow.com/questions/64333/disadvantages-of-test-driven-development)