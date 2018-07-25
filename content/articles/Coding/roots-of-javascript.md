Title: The Lost Roots of JavaScript
Date: 2018-07-16
Tags: Programming, JavaScript

JavaScript has always been an interesting language. Its unique position as the
programming language of the web has something to do with its popularity, but I
think its creators also deserve credit for language design decisions made in
designing the language.

In practicality, JavaScript is at the forefront of multi-paradigm programming.
For many developers I bet JavaScript was the first language they used
functional programming in. In the classical, recognizable sense this is
true with features like `Array.prototype.map`, `Array.prototype.reduce`, and
the like, but it's commonly used at the basic level of a function being passed
around as a first-class object. Without really being clued in to what
functional programming is, people will learn some of the event processing
facilities useful for web development. the window "load" event and button
"click" event are common examples of events beginners learn about early on.

JavaScript is also a lot of people's introduction to reflective programming,
which is really so accessible in JavaScript that a lot of people don't really
think of it too much when doing it, at least at first.

Perhaps the most interesting feature of JavaScript is the prototype-based
object model JavaScript uses. It's the only popular modern language to go this
route, but it works for it. Especially considering how ubiquitous class-based
object-oriented became on server-side langauges during JavaScript's lifetime
this is impressive. Prototype-based object-oriented puts a lot more emphasis
on objects than class-based, which to me makes it perhaps the model that
deserves the name object-oriented more. The ability to create one-off objects
with the option to add any and all desired properties at any time has been
used extensively on the web by many JavaScript libraries.

There are downsides to JavaScript's object model being different to the main
competing concept. Most notably that users coming from class-based languages
often have trouble figuring out how JavaScript objects and constructors work.
JavaScript classes are I guess a response to this, and also provide a way to
make things such as HTMLElement extensible, as they aren't really JS objects.
Additionally, probably because of the bracket notation for accessing
properties, people will create an object where semantically they are
really trying to use an associative container such as JavaScript's Map,
and I've had trouble explaining to even some relatively senior developers
that the JavaScript object doesn't necessarily have the same performance
expenctations as a proper Map.

Given the above it might be fair to say there are a lot of developers
who work with JavaScript but don't fully understand JavaScript. Developers
from all backgrounds too, as colleges with computer science programs seem
to invariably begin with class-based object-oriented languages and don't
really go into how JavaScript is different in say, a programming languages
course. If even these people that we consider trained, professional
developers don't get it, are we at risk for losing the sense of what
defines JavaScript?
