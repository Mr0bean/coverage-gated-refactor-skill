# Tsconfig Strict

- URL: https://www.typescriptlang.org/tsconfig#strict
- Retrieved: 2026-02-14 12:32:50 UTC
- Partition: `typescript`
- Fetch status: `ok`

## Distilled Key Point

- Enable strict mode to catch regressions early.

## Extracted Source Snapshot

```text
TypeScript: TSConfig Reference - Docs on every TSConfig option
Skip to main content         TypeScript      Download
Docs
Handbook
Community
Playground
Tools

in En

Intro to the TSConfig Reference
A TSConfig file in a directory indicates that the directory is the root of a TypeScript or JavaScript project...

Compiler Options

Top Level
files  ,

extends  ,

include  ,

exclude   and

references

" compilerOptions "

Type Checking
allowUnreachableCode  ,

allowUnusedLabels  ,

alwaysStrict  ,

exactOptionalPropertyTypes  ,

noFallthroughCasesInSwitch  ,

noImplicitAny  ,

noImplicitOverride  ,

noImplicitReturns  ,

noImplicitThis  ,

noPropertyAccessFromIndexSignature  ,

noUncheckedIndexedAccess  ,

noUnusedLocals  ,

noUnusedParameters  ,

strict  ,

strictBindCallApply  ,

strictBuiltinIteratorReturn  ,

strictFunctionTypes  ,

strictNullChecks  ,

strictPropertyInitialization   and

useUnknownInCatchVariables

Modules
allowArbitraryExtensions  ,

allowImportingTsExtensions  ,

allowUmdGlobalAccess  ,

baseUrl  ,

customConditions  ,

module  ,

moduleResolution  ,

moduleSuffixes  ,

noResolve  ,

noUncheckedSideEffectImports  ,

paths  ,

resolveJsonModule  ,

resolvePackageJsonExports  ,

resolvePackageJsonImports  ,

rewriteRelativeImportExtensions  ,

rootDir  ,

rootDirs  ,

typeRoots   and

types

Emit
declaration  ,

declarationDir  ,

declarationMap  ,

downlevelIteration  ,

emitBOM  ,

emitDeclarationOnly  ,

importHelpers  ,

inlineSourceMap  ,

inlineSources  ,

mapRoot  ,

newLine  ,

noEmit  ,

noEmitHelpers  ,

noEmitOnError  ,

outDir  ,

outFile  ,

preserveConstEnums  ,

removeComments  ,

sourceMap  ,

sourceRoot   and

stripInternal

JavaScript Support
allowJs  ,

checkJs   and

maxNodeModuleJsDepth

Editor Support
disableSizeLimit   and

plugins

Interop Constraints
allowSyntheticDefaultImports  ,

erasableSyntaxOnly  ,

esModuleInterop  ,

forceConsistentCasingInFileNames  ,

isolatedDeclarations  ,

isolatedModules  ,

preserveSymlinks   and

verbatimModuleSyntax

Backwards Compatibility
charset  ,

importsNotUsedAsValues  ,

keyofStringsOnly  ,

noImplicitUseStrict  ,

noStrictGenericChecks  ,

out  ,

preserveValueImports  ,

suppressExcessPropertyErrors   and

suppressImplicitAnyIndexErrors

Language and Environment
emitDecoratorMetadata  ,

experimentalDecorators  ,

jsx  ,

jsxFactory  ,

jsxFragmentFactory  ,

jsxImportSource  ,

lib  ,

libReplacement  ,

moduleDetection  ,

noLib  ,

reactNamespace  ,

target   and

useDefineForClassFields

Compiler Diagnostics
diagnostics  ,

explainFiles  ,

extendedDiagnostics  ,

generateCpuProfile  ,

generateTrace  ,

listEmittedFiles  ,

listFiles  ,

noCheck   and

traceResolution

Projects
composite  ,

disableReferencedProjectLoad  ,

disableSolutionSearching  ,

disableSourceOfProjectReferenceRedirect  ,

incremental   and

tsBuildInfoFile

Output Formatting
noErrorTruncation  ,

preserveWatchOutput   and

pretty

Completeness
skipDefaultLibCheck   and

skipLibCheck

Command Line

Watch Options
assumeChangesOnlyAffectDirectDependencies

" watchOptions "

watchOptions
watchFile  ,

watchDirectory  ,

fallbackPolling  ,

synchronousWatchDirectory  ,

excludeDirectories   and

excludeFiles

" typeAcquisition "

typeAcquisition
enable  ,

include  ,

exclude   and

disableFilenameBasedTypeAcquisition

Root Fields

Starting up are the root options in the TSConfig - these options relate to how your TypeScript or JavaScript project is set up.

#  Files -  files

Specifies an allowlist of files to include in the program. An error occurs if any of the files can’t be found.

{
"  compilerOptions  "  : {},
"  files  "  : [
"core.ts"  ,
"sys.ts"  ,
"types.ts"  ,
"scanner.ts"  ,
"parser.ts"  ,
"utilities.ts"  ,
"binder.ts"  ,
"checker.ts"  ,
"tsc.ts"
]
}

This is useful when you only have a small number of files and don’t need to use a glob to reference many files.
If you need that then use   include
.

Default:   false

Related:      include

exclude

Released:   1.5

#  Extends -  extends

The value of  extends
is a string which contains a path to another configuration file to inherit from.
The path may use Node.js style resolution.

The configuration from the base file are loaded first, then overridden by those in the inheriting config file. All relative paths found in the configuration file will be resolved relative to the configuration file they originated in.

It’s worth noting that   files
,   include
, and   exclude
from the inheriting config file  overwrite  those from the
base config file, and that circularity between configuration files is not allowed.

Currently, the only top-level property that is excluded from inheritance is   references
.

Example

configs/base.json
:

{
"  compilerOptions  "  : {
"  noImplicitAny  "  :   true  ,
"  strictNullChecks  "  :   true
}
}

tsconfig.json
:

{
"  extends  "  :   "./configs/base"  ,
"  files  "  : [  "main.ts"  ,   "supplemental.ts"  ]
}

tsconfig.nostrictnull.json
:

{
"  extends  "  :   "./tsconfig"  ,
"  compilerOptions  "  : {
"  strictNullChecks  "  :   false
}
}

Properties with relative paths found in the configuration file, which aren’t excluded from inheritance, will be resolved relative to the configuration file they originated in.

Default:   false

Released:   2.1

#  Include -  include

Specifies an array of filenames or patterns to include in the program.
These filenames are resolved relative to the directory containing the  tsconfig.json
file.

json
{
"include"  : [  "src/**/*"  ,   "tests/**/*"  ]
}

Which would include:

.
├── scripts                ⨯
│   ├── lint.ts            ⨯
│   ├── update_deps.ts     ⨯
│   └── utils.ts           ⨯
├── src                    ✓
│   ├── client             ✓
│   │    ├── index.ts      ✓
│   │    └── utils.ts      ✓
│   ├── server             ✓
│   │    └── index.ts      ✓
├── tests                  ✓
│   ├── app.test.ts        ✓
│   ├── utils.ts           ✓
│   └── tests.d.ts         ✓
├── package.json
├── tsconfig.json
└── yarn.lock

include
and  exclude
support wildcard characters to make glob patterns:

*
matches zero or more characters (excluding directory separators)

?
matches any one character (excluding directory separators)

**/
matches any directory nested to any level

If the last path segment in a pattern does not contain a file extension or wildcard character, then it is treated as a directory, and files with supported extensions inside that directory are included (e.g.  .ts
,  .tsx
, and  .d.ts
by default, with  .js
and  .jsx
if   allowJs
is set to true).

Default:   []
if   files
is specified;  **/*
otherwise.

Related:      files

exclude

Released:   2.0

#  Exclude -  exclude

Specifies an array of filenames or patterns that should be skipped when resolving   include
.

Important :  exclude
only  changes which files are included as a result of the   include
setting.
A file specified by  exclude
can still become part of your codebase due to an  import
statement in your code, a  types
inclusion, a  /// <reference
directive, or being specified in the   files
list.

It is not a mechanism that  prevents  a file from being included in the codebase - it simply changes what the   include
setting finds.

Default:  node_modules bower_components jspm_packages   outDir

Related:      include

files

Released:   2.0

#  References -  references

Project references are a way to structure your TypeScript programs into smaller pieces.
Using Project References can greatly improve build and editor interaction times, enforce logical separation between components, and organize your code in new and improved ways.

You can read more about how references works in the  Project References  section of the handbook

Default:   false

Released:   3.0

Compiler Options

These options make up the bulk of TypeScript’s configuration and it covers how the language should work.

Type Checking

Modules

Emit

JavaScript Support

Editor Support

Interop Constraints

Backwards Compatibility

Language and Environment

Compiler Diagnostics

Projects

Output Formatting

Completeness

Command Line

Watch Options

# Type Checking

#  Allow Unreachable Code -  allowUnreachableCode

When:

undefined
(default) provide suggestions as warnings to editors

true
unreachable code is ignored

false
raises compiler errors about unreachable code

These warnings are only about code which is provably unreachable due to the use of JavaScript syntax, for example:

ts
function     fn  (  n  :   number  ) {
if   (  n   >   5  ) {
return     true  ;
}   else   {
return     false  ;
}
return     true  ;
}

With  "allowUnreachableCode": false
:

ts
function      fn   (   n   :   number  ) {
if   (   n    >   5  ) {
return     true  ;
}   else   {
return     false  ;
}
return     true  ;
Unreachable code detected.  7027   Unreachable code detected.   }

Try

This does not affect errors on the basis of code which  appears  to be unreachable due to type analysis.

Released:   1.8

#  Allow Unused Labels -  allowUnusedLabels

When:

undefined
(default) provide suggestions as warnings to editors

true
unused labels are ignored

false
raises compiler errors about unused labels

Labels are very rare in JavaScript and typically indicate an attempt to write an object literal:

ts
function      verifyAge   (   age   :   number  ) {
// Forgot 'return' statement
if   (   age    >   18  ) {
verified :   true  ;
Unused label.  7028   Unused label.     }
}

Try

Released:   1.8

#  Always Strict -  alwaysStrict

Ensures that your files are parsed in the ECMAScript strict mode, and emit “use strict” for each source file.

ECMAScript strict  mode was introduced in ES5 and provides behavior tweaks to the runtime of the JavaScript engine to improve performance, and makes a set of errors throw instead of silently ignoring them.

Recommended

Default:   true
if   strict
;  false
otherwise.

Related:      strict

Released:   2.1

#  Exact Optional Property Types -  exactOptionalPropertyTypes

With exactOptionalPropertyTypes enabled, TypeScript applies stricter rules around how it handles properties on  type
or  interfaces
which have a  ?
prefix.

For example, this interface declares that there is a property which can be one of two strings: ‘dark’ or ‘light’ or it should not be in the object.

ts
interface     UserDefaults   {
// The absence of a value represents 'system'
colorThemeOverride  ?:   "dark"   |   "light"  ;
}

Without this flag enabled, there are three values which you can set  colorThemeOverride
to be: “dark”, “light” and  undefined
.

Setting the value to  undefined
will allow most JavaScript runtime checks for the existence to fail, which is effectively falsy. However, this isn’t quite accurate;  colorThemeOverride: undefined
is not the same as  colorThemeOverride
not being defined. For example,  "colorThemeOverride" in settings
would have different behavior with  undefined
as the key compared to not being defined.

exactOptionalPropertyTypes
makes TypeScript truly enforce the definition provided as an optional property:

ts
const      settings    =    getUserSettings   ();
settings   .   colorThemeOverride    =   "dark"  ;
settings   .   colorThemeOverride    =   "light"  ;

// But not:
settings   .   colorThemeOverride    =    undefined   ;
Type 'undefined' is not assignable to type '"dark" | "light"' with 'exactOptionalPropertyTypes: true'. Consider adding 'undefined' to the type of the target.  2412   Type 'undefined' is not assignable to type '"dark" | "light"' with 'exactOptionalPropertyTypes: true'. Consider adding 'undefined' to the type of the target.
Try

Recommended

Released:   4.4

#  No Fallthrough Cases In Switch -  noFallthroughCasesInSwitch

Report errors for fallthrough cases in switch statements.
Ensures that any non-empty case inside a switch statement includes either  break
,  return
, or  throw
.
This means you won’t accidentally ship a case fallthrough bug.

ts
const      a   :   number   =   6  ;

switch   (   a   ) {
case     0  :
Fallthrough case in switch.  7029   Fallthrough case in switch.          console   .   log   (  "even"  );
case     1  :
console   .   log   (  "odd"  );
break  ;
}

Try

Released:   1.8

#  No Implicit Any -  noImplicitAny

In some cases where no type annotations are present, TypeScript will fall back to a type of  any
for a variable when it cannot infer the type.

This can cause some errors to be missed, for example:

ts
function      fn   (   s   ) {
// No error?
console   .   log   (   s   .   subtr   (  3  ));
}
fn   (  42  );

Try

Turning on  noImplicitAny
however TypeScript will issue an error whenever it would have inferred  any
:

ts
function      fn   (    s    ) {
Parameter 's' implicitly has an 'any' type.  7006   Parameter 's' implicitly has an 'any' type.        console   .   log   (   s   .   subtr   (  3  ));
}

Try

Recommended

Default:   true
if   strict
;  false
otherwise.

Related:      strict

Released:   1.0

#  No Implicit Override -  noImplicitOverride

When working with classes which use inheritance, it’s possible for a sub-class to get “out of sync” with the functions it overloads when they are renamed in the base class.

For example, imagine you are modeling a music album syncing system:

ts
class      Album    {
download   () {
// Default behavior
}
}

class      SharedAlbum      extends      Album    {
download   () {
// Override to get info from many sources
}
}

Try

Then when you add support for machine-learning generated playlists, you refactor the  Album
class to have a ‘setup’ function instead:

ts
class      Album    {
setup   () {
// Default behavior
}
}

class      MLAlbum      extends      Album    {
setup   () {
// Override to get info from algorithm
}
}

class      SharedAlbum      extends      Album    {
download   () {
// Override to get info from many sources
}
}

Try

In this case, TypeScript has provided no warning that  download
on  SharedAlbum
expected  to override a function in the base class.

Using  noImplicitOverride
you can ensure that the sub-classes never go out of sync, by ensuring that functions which override include the keyword  override
.

The following example has  noImplicitOverride
enabled, and you can see the error received when  override
is missing:

ts
class      Album    {
setup   () {}
}

class      MLAlbum      extends      Album    {
override      setup   () {}
}

class      SharedAlbum      extends      Album    {
setup    () {}
This member must have an 'override' modifier because it overrides a member in the base class 'Album'.  4114   This member must have an 'override' modifier because it overrides a member in the base class 'Album'.   }

Try

Released:   4.3

#  No Implicit Returns -  noImplicitReturns

When enabled, TypeScript will check all code paths in a function to ensure they return a value.

ts
function      lookupHeadphonesManufacturer   (   color   :   "blue"   |   "black"  ):    string    {
Function lacks ending return statement and return type does not include 'undefined'.  2366   Function lacks ending return statement and return type does not include 'undefined'.       if   (   color    ===   "blue"  ) {
return     "beats"  ;
}   else   {
(  "bose"  );
}
}

Try

Released:   1.8

#  No Implicit This -  noImplicitThis

Raise error on ‘this’ expressions with an implied ‘any’ type.

For example, the class below returns a function which tries to access  this.width
and  this.height
– but the context
for  this
inside the function inside  getAreaFunction
is not the instance of the Rectangle.

ts
class      Rectangle    {
width   :   number  ;
height   :   number  ;

constructor  (   width   :   number  ,    height   :   number  ) {
this  .   width    =    width   ;
this  .   height    =    height   ;
}

number' >getAreaFunction   () {
return     function   () {
return      this   .   width    *    this   .   height   ;
'this' implicitly has type 'any' because it does not have a type annotation.
'this' implicitly has type 'any' because it does not have a type annotation.  2683 2683   'this' implicitly has type 'any' because it does not have a type annotation.
'this' implicitly has type 'any' because it does not have a type annotation.       };
}
}

Try

Recommended

Default:   true
if   strict
;  false
otherwise.

Related:      strict

Released:   2.0

#  No Property Access From Index Signature -  noPropertyAccessFromIndexSignature

This setting ensures consistency between accessing a field via the “dot” ( obj.key
) syntax, and “indexed” ( obj["key"]
) and the way which the property is declared in the type.

Without this flag, TypeScript will allow you to use the dot syntax to access fields which are not defined:

ts
interface      GameSettings    {
// Known up-front properties
speed   :   "fast"   |   "medium"   |   "slow"  ;
quality   :   "high"   |   "low"  ;

// Assume anything unknown to the interface
// is a string.
[   key   :   string  ]:   string  ;
}

const      settings    =    getSettings   ();
settings   .   speed   ;

(property) GameSettings.speed: "fast" | "medium" | "slow"
settings   .   quality   ;

(property) GameSettings.quality: "high" | "low"

// Unknown key accessors are allowed on
// this object, and are `string`
settings   .   username   ;

(index) GameSettings[string]: string

Try

Turning the flag on will raise an error because the unknown field uses dot syntax instead of indexed syntax.

ts
const      settings    =    getSettings   ();
settings   .   speed   ;
settings   .   quality   ;

// This would need to be settings["username"];
settings   .    username    ;
Property 'username' comes from an index signature, so it must be accessed with ['username'].  4111   Property 'username' comes from an index signature, so it must be accessed with ['username'].
(index) GameSettings[string]: string

Try

The goal of this flag is to signal intent in your calling syntax about how certain you are this property exists.

Released:   4.2

#  No Unchecked Indexed Access -  noUncheckedIndexedAccess

TypeScript has a way to describe objects which have unknown keys but known values on an object, via index signatures.

ts
interface      EnvironmentVars    {
NAME   :   string  ;
OS   :   string  ;

// Unknown properties are covered by this index signature.
[   propName   :   string  ]:   string  ;
}

declare     const      env   :    EnvironmentVars   ;

// Declared as existing
const      sysName    =    env   .   NAME   ;
const      os    =    env   .   OS   ;

const os: string

// Not declared, but because of the index
// signature, then it is considered a string
const      nodeEnv    =    env   .   NODE_ENV   ;

const nodeEnv: string

Try

Turning on  noUncheckedIndexedAccess
will add  undefined
to any un-declared field in the type.

ts
declare     const      env   :    EnvironmentVars   ;

// Declared as existing
const      sysName    =    env   .   NAME   ;
const      os    =    env   .   OS   ;

const os: string

// Not declared, but because of the index
// signature, then it is considered a string
const      nodeEnv    =    env   .   NODE_ENV   ;

const nodeEnv: string | undefined

Try

Released:   4.1

#  No Unused Locals -  noUnusedLocals

Report errors on unused local variables.

ts
const       {
type: string;
modelID: number;
}' >createKeyboard    = (   modelID   :   number  )   =>   {
const       defaultModelID     =   23  ;
'defaultModelID' is declared but its value is never read.  6133   'defaultModelID' is declared but its value is never read.       return   {    type :     "keyboard"  ,    modelID    };
};

Try

Released:   2.0

#  No Unused Parameters -  noUnusedParameters

Report errors on unused parameters in functions.

ts
const       {
type: string;
modelID: number;
}' >createDefaultKeyboard    = (    modelID    :   number  )   =>   {
'modelID' is declared but its value is never read.  6133   'modelID' is declared but its value is never read.       const      defaultModelID    =   23  ;
return   {    type :     "keyboard"  ,    modelID :      defaultModelID    };
};

Try

Parameters declaration with names starting with an underscore ( _
) are exempt from the unused parameter checking. e.g.:

ts
const       {
type: string;
}' >createDefaultKeyboard    = (   _modelID   :   number  )   =>   {
return   {    type :     "keyboard"   };
};

Try

Released:   2.0

#  Strict -  strict

The  strict
flag enables a wide range of type checking behavior that results in stronger guarantees of program correctness.
Turning this on is equivalent to enabling all of the  strict mode family  options, which are outlined below.
You can then turn off individual strict mode family checks as needed.

Future versions of TypeScript may introduce additional stricter checking under this flag, so upgrades of TypeScript might result in new type errors in your program.
When appropriate and possible, a corresponding flag will be added to disable that behavior.

Recommended

Related:      alwaysStrict

strictNullChecks

strictBindCallApply

strictBuiltinIteratorReturn

strictFunctionTypes

strictPropertyInitialization

noImplicitAny

noImplicitThis

useUnknownInCatchVariables

Released:   2.3

#  Strict Bind Call Apply -  strictBindCallApply

When set, TypeScript will check that the built-in methods of functions  call
,  bind
, and  apply
are invoked with correct argument for the underlying function:

ts
// With strictBindCallApply on
function      fn   (   x   :   string  ) {
return      parseInt   (   x   );
}

const      n1    =    fn   .   (this: (this: undefined, args_0: string) => number, thisArg: undefined, args_0: string): number' >call   (   undefined   ,   "10"  );

const      n2    =    fn   .   (this: (this: undefined, x: string) => number, thisArg: undefined, x: string): number' >call   (   undefined   ,    false   );
Argument of type 'boolean' is not assignable to parameter of type 'string'.  2345   Argument of type 'boolean' is not assignable to parameter of type 'string'.
Try

Otherwise, these functions accept a

[Truncated snapshot to keep repository size manageable.]
```
