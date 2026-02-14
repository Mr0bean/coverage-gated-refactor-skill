# Ts Handbook Intro

- URL: https://www.typescriptlang.org/docs/handbook/intro.html
- Retrieved: 2026-02-14 12:32:49 UTC
- Partition: `typescript`
- Fetch status: `ok`

## Distilled Key Point

- Use TypeScript type system as primary guardrail for refactor safety.

## Extracted Source Snapshot

```text
TypeScript: Handbook - The TypeScript Handbook
Skip to main content         TypeScript      Download
Docs
Handbook
Community
Playground
Tools

in En

Was this page helpful?

Get Started                TS for the New Programmer
TypeScript for JS Programmers
TS for Java/C# Programmers
TS for Functional Programmers
TypeScript Tooling in 5 minutes

Handbook                The TypeScript Handbook
The Basics
Everyday Types
Narrowing
More on Functions
Object Types
Type Manipulation                Creating Types from Types
Generics
Keyof Type Operator
Typeof Type Operator
Indexed Access Types
Conditional Types
Mapped Types
Template Literal Types

Classes
Modules

Reference                Utility Types
Cheat Sheets
Decorators
Declaration Merging
Enums
Iterators and Generators
JSX
Mixins
Namespaces
Namespaces and Modules
Symbols
Triple-Slash Directives
Type Compatibility
Type Inference
Variable Declaration

Modules Reference                Introduction
Theory
Guides                Choosing Compiler Options

Reference
Appendices                ESM/CJS Interoperability

Tutorials                ASP.NET Core
Gulp
DOM Manipulation
Migrating from JavaScript
Using Babel with TypeScript

What's New                TypeScript 5.9
TypeScript 5.8
TypeScript 5.7
TypeScript 5.6
TypeScript 5.5
TypeScript 5.4
TypeScript 5.3
TypeScript 5.2
TypeScript 5.1
TypeScript 5.0
TypeScript 4.9
TypeScript 4.8
TypeScript 4.7
TypeScript 4.6
TypeScript 4.5
TypeScript 4.4
TypeScript 4.3
TypeScript 4.2
TypeScript 4.1
TypeScript 4.0
TypeScript 3.9
TypeScript 3.8
TypeScript 3.7
TypeScript 3.6
TypeScript 3.5
TypeScript 3.4
TypeScript 3.3
TypeScript 3.2
TypeScript 3.1
TypeScript 3.0
TypeScript 2.9
TypeScript 2.8
TypeScript 2.7
TypeScript 2.6
TypeScript 2.5
TypeScript 2.4
TypeScript 2.3
TypeScript 2.2
TypeScript 2.1
TypeScript 2.0
TypeScript 1.8
TypeScript 1.7
TypeScript 1.6
TypeScript 1.5
TypeScript 1.4
TypeScript 1.3
TypeScript 1.1

Declaration Files                Introduction
Declaration Reference
Library Structures
.d.ts Templates                Modules .d.ts
Module: Plugin
Module: Class
Module: Function
Global .d.ts
Global: Modifying Module

Do's and Don'ts
Deep Dive
Publishing
Consumption

JavaScript                JS Projects Utilizing TypeScript
Type Checking JavaScript Files
JSDoc Reference
Creating .d.ts Files from .js files

Project Configuration                What is a tsconfig.json
Compiler Options in MSBuild
TSConfig Reference
tsc CLI Options
Project References
Integrating with Build Tools
Configuring Watch
Nightly Builds

The TypeScript Handbook
About this Handbook

Over 20 years after its introduction to the programming community, JavaScript is now one of the most widespread cross-platform languages ever created. Starting as a small scripting language for adding trivial interactivity to webpages, JavaScript has grown to be a language of choice for both frontend and backend applications of every size. While the size, scope, and complexity of programs written in JavaScript has grown exponentially, the ability of the JavaScript language to express the relationships between different units of code has not. Combined with JavaScript’s rather peculiar runtime semantics, this mismatch between language and program complexity has made JavaScript development a difficult task to manage at scale.

The most common kinds of errors that programmers write can be described as type errors: a certain kind of value was used where a different kind of value was expected. This could be due to simple typos, a failure to understand the API surface of a library, incorrect assumptions about runtime behavior, or other errors. The goal of TypeScript is to be a static typechecker for JavaScript programs - in other words, a tool that runs before your code runs (static) and ensures that the types of the program are correct (typechecked).

If you are coming to TypeScript without a JavaScript background, with the intention of TypeScript being your first language, we recommend you first start reading the documentation on either the  Microsoft Learn JavaScript tutorial  or read  JavaScript at the Mozilla Web Docs .
If you have experience in other languages, you should be able to pick up JavaScript syntax quite quickly by reading the handbook.

How is this Handbook Structured

The handbook is split into two sections:

The Handbook

The TypeScript Handbook is intended to be a comprehensive document that explains TypeScript to everyday programmers. You can read the handbook by going from top to bottom in the left-hand navigation.

You should expect each chapter or page to provide you with a strong understanding of the given concepts. The TypeScript Handbook is not a complete language specification, but it is intended to be a comprehensive guide to all of the language’s features and behaviors.

A reader who completes the walkthrough should be able to:

Read and understand commonly-used TypeScript syntax and patterns

Explain the effects of important compiler options

Correctly predict type system behavior in most cases

In the interests of clarity and brevity, the main content of the Handbook will not explore every edge case or minutiae of the features being covered. You can find more details on particular concepts in the reference articles.

Reference Files

The reference section below the handbook in the navigation is built to provide a richer understanding of how a particular part of TypeScript works. You can read it top-to-bottom, but each section aims to provide a deeper explanation of a single concept - meaning there is no aim for continuity.

Non-Goals

The Handbook is also intended to be a concise document that can be comfortably read in a few hours. Certain topics won’t be covered in order to keep things short.

Specifically, the Handbook does not fully introduce core JavaScript basics like functions, classes, and closures. Where appropriate, we’ll include links to background reading that you can use to read up on those concepts.

The Handbook also isn’t intended to be a replacement for a language specification. In some cases, edge cases or formal descriptions of behavior will be skipped in favor of high-level, easier-to-understand explanations. Instead, there are separate reference pages that more precisely and formally describe many aspects of TypeScript’s behavior. The reference pages are not intended for readers unfamiliar with TypeScript, so they may use advanced terminology or reference topics you haven’t read about yet.

Finally, the Handbook won’t cover how TypeScript interacts with other tools, except where necessary. Topics like how to configure TypeScript with webpack, rollup, parcel, react, babel, closure, lerna, rush, bazel, preact, vue, angular, svelte, jquery, yarn, or npm are out of scope - you can find these resources elsewhere on the web.

Get Started

Before getting started with  The Basics , we recommend reading one of the following introductory pages. These introductions are intended to highlight key similarities and differences between TypeScript and your favored programming language, and clear up common misconceptions specific to those languages.

TypeScript for the New Programmer

TypeScript for JavaScript Programmers

TypeScript for Java/C# Programmers

TypeScript for Functional Programmers

Otherwise, jump to  The Basics .

On this page
About this Handbook
How is this Handbook Structured    Non-Goals

Get Started

Is this page helpful?
Yes        No

Next
The Basics
Step one in learning TypeScript: The basic types.

The TypeScript docs are an open source project. Help us improve these pages  by sending a Pull Request  ❤

Contributors to this page:   OT
MW
M
N
谭
5 +

Last updated: Feb 14, 2026

Customize
Site Colours :
System  Always Light  Always Dark
Code Font :
Cascadia  Cascadia (ligatures)  Consolas  Dank Mono  Fira Code  JetBrains Mono  OpenDyslexic  SF Mono  Source Code Pro

Popular Documentation Pages
Everyday Types  All of the common types in TypeScript

Creating Types from Types  Techniques to make more elegant types

More on Functions  How to provide types to functions in JavaScript

More on Objects  How to provide a type shape to JavaScript objects

Narrowing  How TypeScript infers types based on runtime behavior

Variable Declarations  How to create and type JavaScript variables

TypeScript in 5 minutes  An overview of building a TypeScript web app

TSConfig Options  All the configuration options for a project

Classes  How to provide types to JavaScript ES6 classes

Made with ♥ in Redmond, Boston, SF & Dublin
© 2012- 2026  Microsoft  Privacy  Terms of Use

Using TypeScript
Get Started
Download
Community
Playground
TSConfig Ref
Code Samples
Why TypeScript
Design

Community
Get Help
Blog
GitHub Repo
Community Chat
@TypeScript
Mastodon
Stack Overflow
Web Repo

MSG
```
