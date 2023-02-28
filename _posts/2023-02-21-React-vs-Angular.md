---
title: "React versus Angular"
date: 2023-02-12
published: false
visible: false
categories:
  - Blog
tags:
  - Angular
toc: false
classes: wide
---
This is a meta analysis, what I found, what other people think about the differences between React and Angular.

My personal conclusion is: Angular beats React, especially for the Enterprise environment.

## Video 1[^1]:

### Usage of Angular:
* Gmail
* Google
* Microsoft
* upwork (Freelancer portal)
* Sony
* Forbes

### Usage of React
* Facebook
* Instagram
* Netflix
* Dropbox
* Über

### Mission Statements of Google vs Facebook:
* Google: "do no evil"
* Facebook: "move fast &  break things"
* "solid" vs "disruptive" ?

## Google search :
"What are the main difference between the Angular framework and React library regarding business applications especially big ones?"
* lots of bad superficially written articles, seems they just repeat known prejudices, such as "easy to learn" without any evidence or more precise explanation given.


## ChatGPT :
"What are the main difference between the Angular framework and React library regarding business applications especially big ones?"
* basically same problem but at least a nice summary of those links given by Google:

| Feature                | React                                                    | Angular                                                  |
|-----------------------|---------------------------------------------------------|---------------------------------------------------------|
| Type                   | Library                                                  | Full-featured framework                                   |
| Architecture           | Component-based                                          | Model-View-Controller (MVC)                               |
| Rendering              | Virtual DOM                                              | Regular DOM                                              |
| Syntax                 | JSX                                                      | HTML, TypeScript                                         |
| Learning Curve         | Easy                                                    | Steep                                                    |
| Community Support      | Large and active                                         | Smaller but significant                                 |
| Performance            | Good                                                     | Good, especially for large-scale applications            |
| Built-in Features      | Minimalist, requires additional libraries/tools           | Large number of built-in features and abstractions       |
| State Management       | Requires additional libraries/tools                       | Built-in                                                 |
| Dependency Injection   | Not built-in                                             | Built-in                                                 |
| Two-way Data Binding   | Not built-in                                             | Built-in                                                 |
| Strong Typing          | Optional                                                 | Built-in with TypeScript                                 |
| Routing                | Requires additional libraries/tools                       | Built-in                                                 |
| Testing                | Requires additional libraries/tools                       | Built-in                                                 |


## Popularity
* [React on github:](https://github.com/facebook/react): 203k stars, 1606 contributors
* [Angular on gibhub](https://github.com/angular/angular): 87k stars, 1675 contributors
* [Spring Framework on gibhub](https://github.com/angular/angular): 65.8k stars, 978 contributors
* [Google trends Deutschland](https://trends.google.com/trends/explore?cat=31&date=today%205-y&geo=DE&q=%2Fm%2F012l1vxv,%2Fg%2F11c6w0ddw9): letzten 12 monate: 79:54 für React 
* [Google trends Worlwide](https://trends.google.com/trends/explore?cat=31&date=all&q=%2Fm%2F012l1vxv,%2Fg%2F11c6w0ddw9): 90:36 für React

## Jobs
[Video](https://youtu.be/2MdFCCLXX9A)
* less applicants for  Angular jobs
* for Angular developers there might be more jobs on bigger, longer lasting projects

also questionable, because not much evidence given.



## Video 1[^2]
Its the best video I found for the topic:

"React or Angular - The Best Tech Stack for Your Development Team"
tries to give a "High Level difference for Managers":

* new Teams have fast success with React at first
  * later there are not as productive 
* without a basic training, a developer can not use Angular
* React vs. Angular[^3]: 

{% include figure image_path="/assets/images/ReactVsAngularLearningCurve.webp" alt="React vs. Angular learning curve" caption="Learning curve." %}

* most developer focuses on dataflow and business logic, then Angular is the better choice
* if the focus is more the view, developers build hierarchies of views but don't think about layering the architecture. 
* with React the business logic get too much mixed in with the views, which is not best practices, and is very difficult to test the business logic independent of the views
* it is certainly possible to keep views separate from the business logic in React as well, but it does not enforce it the same way Angular does. In React, its easier to do it the wrong way.
* Angular has lots of libraries that come with it, so there is a default, and those  guarantied to work with the base version.
  * forms
  * i18n
  * routing
  * lazy loading
  * rest services features
  * dependency injection (very good for automated testing)
* all those are the same in each Angular Project, but not in React
* In React the developer needs to choose those libraries by himself, and not every library works well with another, with arbitrary version numbers. They can be very different in different React projects
* its comparatively easy for an Angular Developer to work on a React project
* buts is hard for a React Developer to work on an Angular project

{% include figure image_path="/assets/images/HiringReactVsAngularDevelopers.png" alt="React vs. Angular hiring developers" caption="Hiring Developers." %}

{% include figure image_path="/assets/images/ReactVSAngularTechnology.png" alt="React vs. Angular Technologie " caption="Technology" %}

{% include figure image_path="/assets/images/AngularPlusReact.png" alt="Angular plus React " caption="interesting recommendation for testing" %}

{% include figure image_path="/assets/images/AngularVsReactExec.png" alt="Angular vs React " caption="Executive Criteria" %}

## Best Article I found:
[Why Angular is the right choice for enterprise level applications over React](https://medium.com/@kanth.vallampati/why-angular-is-the-right-choice-for-enterprise-level-applications-over-react-9063dc742902)

The author clearly has a bias towards Angular, but at least he gives some interesting and solid arguments for that.

### Short Summary
#### Evolution of React and Angular
* unfortunately Angular had many breaking changes until Version 5 , which helped React to grab the Market
* now React since React seems "bigger" to new developers , more developers jump on it's wagon 

#### 1st Misconception: React is easier to learn 
* Since React is just a library with less features, new developers are faster to get productive with React, but only as long as they don't need the additional features of Angular. But React is missing lots of features that Angular already has build in.
* Then React is even harder to learn with all the additional libraries needed than Angular.

{% include figure image_path="/assets/images/ReactVsAngularLearningCurve.webp" alt="React vs. Angular learning curve" caption="Learning curve." %}

#### 2nd Misconception: React is faster
* "React is faster than Angular because of **Virtual DOM** was a misunderstanding spread by React team themselves. "
* see links in the original article why this is not true
* Angulars **Incremental DOM** is better now

#### React Problems:
* lots of other dependencies needed for real world apps, but no guarantee that they work together correctly.
* Separation of concerns: 
  * JSX  is not good with conditionals and loops
  * problematic inline styles, no media queries
* not truly reactive
* no standard data layer
* "it has not solved styling components."

## Other random opinions I found:

### Library vs Framework
* Since React is "just" a library, it seems to have learning curve not as steep as Angular. 
* on the other Hand, Angular has a lot more features (see table above) than React. Yes, you can add those missing features with other libraries in React, but there seems to be a lot of possibilities you need to choose between, which is not easy either.
* Angular gives the deveoper a more rigid structure, which he needs to learn first, but makes it easier to navigate though the code base for large applications

### Performance
Whereas React seemed to be better in the old days of AngularJS before 2016, the Angular version 2 and newer is at least equal in speed and for some benchmarks even better than React. On some other task, React might still be faster

### Learning curve
Since React is just a library with less features, new developers are faster to get productive with React, as long as they don't need the additional features of Angular.
On the other hand Angular has very good documentation of it's rich feature set. 
Angular apps tend to be more consistent across projects.

### Reusing of Components
Some say, that reusing of components is easier in React then in Angular.

### Testability
Since React uses a dynamically typed language and no dependency injection, it seems to be easier to write automated test for Angular, and thanks to TypeScript some developer errors are already found by the compiler in Angular for which TypeScript is mandatory.

### Enterprise Environment
Seems that Angular is more often used for Enterprise - Type single-page Applications and in environments with multiple project and teams.


-----

[^1]: [Video, length 6:25: React vs. Angular in 2023](https://youtu.be/CynLOUL9vsU)
[^2]: VP of Engineering Services at Briebug, Thomas Burleson, Video ["React or Angular - The Best Tech Stack for Your Development Team", video length: 21:26 ](https://youtu.be/Z46mcHIfzoE)
[^3]: from [Why Angular is the right choice for enterprise level applications over React](https://medium.com/@kanth.vallampati/why-angular-is-the-right-choice-for-enterprise-level-applications-over-react-9063dc742902)
