Title: Node's contribution to JavaScript
Date: 2018-07-24
Tags: Programming, JavaScript

Thinking about JavaScript a couple of years ago, it was difficult to
determine what was part of JS as a language and what was part of the
API it exposed in the browser. JavaScript, in contrast to a lot of
other languages, was used in one environment and built specifically
for that environment, the web. That can be seen in the way JavaScript
has been taught too. Consider a theoretical book for learning JS,
where the index looks kind of like this:

    1. Hello, World
    2. Variables and Functions
    3. The Document and the Window
       ...
    6. jQuery
       ...
    9. Prototype-based Programming

An unfortunate side-effect of which is that for a lot of people it's
difficult to define JavaScript outside of the browser context, and
to say what is part of JavaScript versus what is part of APIs
implemeted by the browser. JavaScript definitely has a specification,
but historically there hasn't been too much value in considering 
what was the language and the standard library and what was the
browser. Some stuff clearly disappears; the Window API, the Document
API, and HTML elements, all gone. But maybe some of that was good,
and JavaScript could carve out a niche in scripting for other tree-
like document formats. That could be a practical use of a language
that is already used for similar tasks, but it wouldn't help us
evaluate JavaScript as a general purpose language. For that we
would need something that allowed JavaScript to tackle a dissimilar
problem domain. That's what NodeJS does when it puts JavaScript on
the other side of the client-server relationship.

Server-side JavaScript has allowed us to ask what the core parts of
JavaScript are and what was needed for it to function as a
general-purpose language. It has allowed JavaScript to find other
niches and allowed programmers to use JavaScript in ways not common
in the browser. The uses that JavaScript sees are commonly
web-adjacent. Somewhat unsurpisingly stateless transactional
communication has turned out to be one of JavaScript's strengths,
not just something that was done alongside DOM manipulation in the
browser. The JS object model is good for flyweight API endpoints
and RPC. First-class functions makes the use of various existing
frameworks as easy as passing a function definition into one of the
framework's functions. Event-driven programming is even still
present, and the runtime being event-loop based is a deliberate and
important decision for Node's runtime. The default mode being
event-loop based is a strong statement that one of the good things
about JavaScript is that it facilitates event-driven programming.

NodeJS is also notable for its `require` functionality, which is
completely unlike the traditional method of using different
JavaScript files in the browser. A convenient way for your code
to reference and rely on external libraries and objects is the
difference between a language that can only support glue scripts
and a language that you can write applications in. In the
browser, the basic way you have of doing this is effectively
just concatenating all the scripts you need something from
together. Node's `require` and packaging ecosystem in general
are a big step up from the bare minimum web developers have
generally had. We're seeing developments in the browser in this
area too, such as [RequireJS](https://requirejs.org/) and
ES6 modules with the import statement.

Everything developed for Node isn't necessarily going to be
appropriate to put back into client-side JavaScript. The APIs
for local filesystem access are inappropriate for the web, as
are foreign function interfaces. That's okay though because how
it's expanded what JavaScript programmer's and everyone else
sees in JavaScript is perhaps it's biggest contribution to the
language.
