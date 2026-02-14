# Fastapi Bigger Applications

- URL: https://fastapi.tiangolo.com/tutorial/bigger-applications/
- Retrieved: 2026-02-14 12:32:12 UTC
- Partition: `backend`
- Fetch status: `ok`

## Distilled Key Point

- Split APIs into routers and maintain modular structure.

## Extracted Source Snapshot

```text
Bigger Applications - Multiple Files - FastAPI

Skip to content

Join the  FastAPI Cloud  waiting list 🚀

Follow  @fastapi  on  X (Twitter)  to stay updated

Follow  FastAPI  on  LinkedIn  to stay updated

Subscribe to the  FastAPI and friends  newsletter 🎉

sponsor

sponsor

sponsor

sponsor

sponsor

sponsor

sponsor

sponsor

sponsor

sponsor

sponsor

FastAPI

Bigger Applications - Multiple Files

en - English

de - Deutsch

es - español

fr - français

ja - 日本語

ko - 한국어

pt - português

ru - русский язык

tr - Türkçe

uk - українська мова

zh - 简体中文

zh-hant - 繁體中文

Initializing search

fastapi/fastapi

FastAPI

Features

Learn

Reference

FastAPI People

Resources

About

Release Notes

FastAPI

fastapi/fastapi

FastAPI

Features

Learn

Learn

Python Types Intro

Concurrency and async / await

Environment Variables

Virtual Environments

Tutorial - User Guide

Tutorial - User Guide

First Steps

Path Parameters

Query Parameters

Request Body

Query Parameters and String Validations

Path Parameters and Numeric Validations

Query Parameter Models

Body - Multiple Parameters

Body - Fields

Body - Nested Models

Declare Request Example Data

Extra Data Types

Cookie Parameters

Header Parameters

Cookie Parameter Models

Header Parameter Models

Response Model - Return Type

Extra Models

Response Status Code

Form Data

Form Models

Request Files

Request Forms and Files

Handling Errors

Path Operation Configuration

JSON Compatible Encoder

Body - Updates

Dependencies

Dependencies

Classes as Dependencies

Sub-dependencies

Dependencies in path operation decorators

Global Dependencies

Dependencies with yield

Security

Security

Security - First Steps

Get Current User

Simple OAuth2 with Password and Bearer

OAuth2 with Password (and hashing), Bearer with JWT tokens

Middleware

CORS (Cross-Origin Resource Sharing)

SQL (Relational) Databases

Bigger Applications - Multiple Files

Bigger Applications - Multiple Files

Table of contents

An example file structure

APIRouter

Import  APIRouter

Path operations  with  APIRouter

Dependencies

Another module with  APIRouter

Import the dependencies

How relative imports work

Add some custom  tags
,  responses
, and  dependencies

The main  FastAPI

Import  FastAPI

Import the  APIRouter

How the importing works

Avoid name collisions

Include the  APIRouter
s for  users
and  items

Include an  APIRouter
with a custom  prefix
,  tags
,  responses
, and  dependencies

Include a  path operation

Check the automatic API docs

Include the same router multiple times with different  prefix

Include an  APIRouter
in another

Background Tasks

Metadata and Docs URLs

Static Files

Testing

Debugging

Advanced User Guide

Advanced User Guide

Path Operation Advanced Configuration

Additional Status Codes

Return a Response Directly

Custom Response - HTML, Stream, File, others

Additional Responses in OpenAPI

Response Cookies

Response Headers

Response - Change Status Code

Advanced Dependencies

Advanced Security

Advanced Security

OAuth2 scopes

HTTP Basic Auth

Using the Request Directly

Using Dataclasses

Advanced Middleware

Sub Applications - Mounts

Behind a Proxy

Templates

WebSockets

Lifespan Events

Testing WebSockets

Testing Events: lifespan and startup - shutdown

Testing Dependencies with Overrides

Async Tests

Settings and Environment Variables

OpenAPI Callbacks

OpenAPI Webhooks

Including WSGI - Flask, Django, others

Generating SDKs

Advanced Python Types

FastAPI CLI

Deployment

Deployment

About FastAPI versions

FastAPI Cloud

About HTTPS

Run a Server Manually

Deployments Concepts

Deploy FastAPI on Cloud Providers

Server Workers - Uvicorn with Workers

FastAPI in Containers - Docker

How To - Recipes

How To - Recipes

General - How To - Recipes

Migrate from Pydantic v1 to Pydantic v2

GraphQL

Custom Request and APIRoute class

Conditional OpenAPI

Extending OpenAPI

Separate OpenAPI Schemas for Input and Output or Not

Custom Docs UI Static Assets (Self-Hosting)

Configure Swagger UI

Testing a Database

Use Old 403 Authentication Error Status Codes

Reference

Reference

FastAPI
class

Request Parameters

Status Codes

UploadFile
class

Exceptions -  HTTPException
and  WebSocketException

Dependencies -  Depends()
and  Security()

APIRouter
class

Background Tasks -  BackgroundTasks

Request
class

WebSockets

HTTPConnection
class

Response
class

Custom Response Classes - File, HTML, Redirect, Streaming, etc.

Middleware

OpenAPI

OpenAPI

OpenAPI  docs

OpenAPI  models

Security Tools

Encoders -  jsonable_encoder

Static Files -  StaticFiles

Templating -  Jinja2Templates

Test Client -  TestClient

FastAPI People

Resources

Resources

Help FastAPI - Get Help

Development - Contributing

Full Stack FastAPI Template

External Links

FastAPI and friends newsletter

Repository Management Tasks

About

About

Alternatives, Inspiration and Comparisons

History, Design and Future

Benchmarks

Repository Management

Release Notes

Table of contents

An example file structure

APIRouter

Import  APIRouter

Path operations  with  APIRouter

Dependencies

Another module with  APIRouter

Import the dependencies

How relative imports work

Add some custom  tags
,  responses
, and  dependencies

The main  FastAPI

Import  FastAPI

Import the  APIRouter

How the importing works

Avoid name collisions

Include the  APIRouter
s for  users
and  items

Include an  APIRouter
with a custom  prefix
,  tags
,  responses
, and  dependencies

Include a  path operation

Check the automatic API docs

Include the same router multiple times with different  prefix

Include an  APIRouter
in another

FastAPI

Learn

Tutorial - User Guide

Bigger Applications - Multiple Files ¶

If you are building an application or a web API, it's rarely the case that you can put everything in a single file.

FastAPI  provides a convenience tool to structure your application while keeping all the flexibility.

Info

If you come from Flask, this would be the equivalent of Flask's Blueprints.

An example file structure ¶

Let's say you have a file structure like this:

.
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   └── routers
│   │   ├── __init__.py
│   │   ├── items.py
│   │   └── users.py
│   └── internal
│       ├── __init__.py
│       └── admin.py

Tip

There are several  __init__.py
files: one in each directory or subdirectory.

This is what allows importing code from one file into another.

For example, in  app/main.py
you could have a line like:

from app.routers import items

The  app
directory contains everything. And it has an empty file  app/__init__.py
, so it is a "Python package" (a collection of "Python modules"):  app
.

It contains an  app/main.py
file. As it is inside a Python package (a directory with a file  __init__.py
), it is a "module" of that package:  app.main
.

There's also an  app/dependencies.py
file, just like  app/main.py
, it is a "module":  app.dependencies
.

There's a subdirectory  app/routers/
with another file  __init__.py
, so it's a "Python subpackage":  app.routers
.

The file  app/routers/items.py
is inside a package,  app/routers/
, so, it's a submodule:  app.routers.items
.

The same with  app/routers/users.py
, it's another submodule:  app.routers.users
.

There's also a subdirectory  app/internal/
with another file  __init__.py
, so it's another "Python subpackage":  app.internal
.

And the file  app/internal/admin.py
is another submodule:  app.internal.admin
.

The same file structure with comments:

.
├──   app                     # "app" is a Python package
│     ├──   __init__.py         # this file makes "app" a "Python package"
│     ├──   main.py             # "main" module, e.g. import app.main
│     ├──   dependencies.py     # "dependencies" module, e.g. import app.dependencies
│     └──   routers             # "routers" is a "Python subpackage"
│     │     ├──   __init__.py     # makes "routers" a "Python subpackage"
│     │     ├──   items.py        # "items" submodule, e.g. import app.routers.items
│     │     └──   users.py        # "users" submodule, e.g. import app.routers.users
│     └──   internal            # "internal" is a "Python subpackage"
│         ├──   __init__.py     # makes "internal" a "Python subpackage"
│         └──   admin.py        # "admin" submodule, e.g. import app.internal.admin

APIRouter
¶

Let's say the file dedicated to handling just users is the submodule at  /app/routers/users.py
.

You want to have the  path operations  related to your users separated from the rest of the code, to keep it organized.

But it's still part of the same  FastAPI  application/web API (it's part of the same "Python Package").

You can create the  path operations  for that module using  APIRouter
.

Import  APIRouter
¶

You import it and create an "instance" the same way you would with the class  FastAPI
:

Python 3.8+

app/routers/users.py        from     fastapi     import   APIRouter

router   =   APIRouter  ()

@router  .  get  (  "/users/"  ,   tags  =  [  "users"  ])
async   def     read_users  ():
return   [{  "username"  :   "Rick"  },   {  "username"  :   "Morty"  }]

@router  .  get  (  "/users/me"  ,   tags  =  [  "users"  ])
async   def     read_user_me  ():
return   {  "username"  :   "fakecurrentuser"  }

@router  .  get  (  "/users/  {username}  "  ,   tags  =  [  "users"  ])
async   def     read_user  (  username  :   str  ):
return   {  "username"  :   username  }

Path operations  with  APIRouter
¶

And then you use it to declare your  path operations .

Use it the same way you would use the  FastAPI
class:

Python 3.8+

app/routers/users.py       from     fastapi     import   APIRouter

router   =   APIRouter  ()

@router  .  get  (  "/users/"  ,   tags  =  [  "users"  ])
async   def     read_users  ():
return   [{  "username"  :   "Rick"  },   {  "username"  :   "Morty"  }]

@router  .  get  (  "/users/me"  ,   tags  =  [  "users"  ])
async   def     read_user_me  ():
return   {  "username"  :   "fakecurrentuser"  }

@router  .  get  (  "/users/  {username}  "  ,   tags  =  [  "users"  ])
async   def     read_user  (  username  :   str  ):
return   {  "username"  :   username  }

You can think of  APIRouter
as a "mini  FastAPI
" class.

All the same options are supported.

All the same  parameters
,  responses
,  dependencies
,  tags
, etc.

Tip

In this example, the variable is called  router
, but you can name it however you want.

We are going to include this  APIRouter
in the main  FastAPI
app, but first, let's check the dependencies and another  APIRouter
.

Dependencies ¶

We see that we are going to need some dependencies used in several places of the application.

So we put them in their own  dependencies
module ( app/dependencies.py
).

We will now use a simple dependency to read a custom  X-Token
header:

Python 3.10+

app/dependencies.py       from     typing     import   Annotated

from     fastapi     import   Header  ,   HTTPException

async   def     get_token_header  (  x_token  :   Annotated  [  str  ,   Header  ()]):
if   x_token   !=   "fake-super-secret-token"  :
raise   HTTPException  (  status_code  =  400  ,   detail  =  "X-Token header invalid"  )

async   def     get_query_token  (  token  :   str  ):
if   token   !=   "jessica"  :
raise   HTTPException  (  status_code  =  400  ,   detail  =  "No Jessica token provided"  )

🤓 Other versions and variants
Python 3.9+  Python 3.9+ - non-Annotated

app/dependencies.py       from     typing     import   Annotated

from     fastapi     import   Header  ,   HTTPException

async   def     get_token_header  (  x_token  :   Annotated  [  str  ,   Header  ()]):
if   x_token   !=   "fake-super-secret-token"  :
raise   HTTPException  (  status_code  =  400  ,   detail  =  "X-Token header invalid"  )

async   def     get_query_token  (  token  :   str  ):
if   token   !=   "jessica"  :
raise   HTTPException  (  status_code  =  400  ,   detail  =  "No Jessica token provided"  )

Tip

Prefer to use the  Annotated
version if possible.

app/dependencies.py       from     fastapi     import   Header  ,   HTTPException

async   def     get_token_header  (  x_token  :   str   =   Header  ()):
if   x_token   !=   "fake-super-secret-token"  :
raise   HTTPException  (  status_code  =  400  ,   detail  =  "X-Token header invalid"  )

async   def     get_query_token  (  token  :   str  ):
if   token   !=   "jessica"  :
raise   HTTPException  (  status_code  =  400  ,   detail  =  "No Jessica token provided"  )

Tip

We are using an invented header to simplify this example.

But in real cases you will get better results using the integrated  Security utilities .

Another module with  APIRouter
¶

Let's say you also have the endpoints dedicated to handling "items" from your application in the module at  app/routers/items.py
.

You have  path operations  for:

/items/

/items/{item_id}

It's all the same structure as with  app/routers/users.py
.

But we want to be smarter and simplify the code a bit.

We know all the  path operations  in this module have the same:

Path  prefix
:  /items
.

tags
: (just one tag:  items
).

Extra  responses
.

dependencies
: they all need that  X-Token
dependency we created.

So, instead of adding all that to each  path operation , we can add it to the  APIRouter
.

Python 3.8+

app/routers/items.py       from     fastapi     import   APIRouter  ,   Depends  ,   HTTPException

from     ..dependencies     import   get_token_header

router   =   APIRouter  (
prefix  =  "/items"  ,
tags  =  [  "items"  ],
dependencies  =  [  Depends  (  get_token_header  )],
responses  =  {  404  :   {  "description"  :   "Not found"  }},
)

fake_items_db   =   {  "plumbus"  :   {  "name"  :   "Plumbus"  },   "gun"  :   {  "name"  :   "Portal Gun"  }}

@router  .  get  (  "/"  )
async   def     read_items  ():
return   fake_items_db

@router  .  get  (  "/  {item_id}  "  )
async   def     read_item  (  item_id  :   str  ):
if   item_id   not   in   fake_items_db  :
raise   HTTPException  (  status_code  =  404  ,   detail  =  "Item not found"  )
return   {  "name"  :   fake_items_db  [  item_id  ][  "name"  ],   "item_id"  :   item_id  }

@router  .  put  (
"/  {item_id}  "  ,
tags  =  [  "custom"  ],
responses  =  {  403  :   {  "description"  :   "Operation forbidden"  }},
)
async   def     update_item  (  item_id  :   str  ):
if   item_id   !=   "plumbus"  :
raise   HTTPException  (
status_code  =  403  ,   detail  =  "You can only update the item: plumbus"
)
return   {  "item_id"  :   item_id  ,   "name"  :   "The great Plumbus"  }

As the path of each  path operation  has to start with  /
, like in:

@router  .  get  (  "/  {item_id}  "  )
async   def     read_item  (  item_id  :   str  ):
...

...the prefix must not include a final  /
.

So, the prefix in this case is  /items
.

We can also add a list of  tags
and extra  responses
that will be applied to all the  path operations  included in this router.

And we can add a list of  dependencies
that will be added to all the  path operations  in the router and will be executed/solved for each request made to them.

Tip

Note that, much like  dependencies in  path operation decorators  , no value will be passed to your  path operation function .

The end result is that the item paths are now:

/items/

/items/{item_id}

...as we intended.

They will be marked with a list of tags that contain a single string  "items"
.
These "tags" are especially useful for the automatic interactive documentation systems (using OpenAPI).

All of them will include the predefined  responses
.

All these  path operations  will have the list of  dependencies
evaluated/executed before them.
If you also declare dependencies in a specific  path operation ,  they will be executed too .

The router dependencies are executed first, then the   dependencies
in the decorator , and then the normal parameter dependencies.

You can also add   Security
dependencies with  scopes
.

Tip

Having  dependencies
in the  APIRouter
can be used, for example, to require authentication for a whole group of  path operations . Even if the dependencies are not added individually to each one of them.

Check

The  prefix
,  tags
,  responses
, and  dependencies
parameters are (as in many other cases) just a feature from  FastAPI  to help you avoid code duplication.

Import the dependencies ¶

This code lives in the module  app.routers.items
, the file  app/routers/items.py
.

And we need to get the dependency function from the module  app.dependencies
, the file  app/dependencies.py
.

So we use a relative import with  ..
for the dependencies:

Python 3.8+

app/routers/items.py       from     fastapi     import   APIRouter  ,   Depends  ,   HTTPException

from     ..dependencies     import   get_token_header

router   =   APIRouter  (
prefix  =  "/items"  ,
tags  =  [  "items"  ],
dependencies  =  [  Depends  (  get_token_header  )],
responses  =  {  404  :   {  "description"  :   "Not found"  }},
)

fake_items_db   =   {  "plumbus"  :   {  "name"  :   "Plumbus"  },   "gun"  :   {  "name"  :   "Portal Gun"  }}

@router  .  get  (  "/"  )
async   def     read_items  ():
return   fake_items_db

@router  .  get  (  "/  {item_id}  "  )
async   def     read_item  (  item_id  :   str  ):
if   item_id   not   in   fake_items_db  :
raise   HTTPException  (  status_code  =  404  ,   detail  =  "Item not found"  )
return   {  "name"  :   fake_items_db  [  item_id  ][  "name"  ],   "item_id"  :   item_id  }

@router  .  put  (
"/  {item_id}  "  ,
tags  =  [  "custom"  ],
responses  =  {  403  :   {  "description"  :   "Operation forbidden"  }},
)
async   def     update_item  (  item_id  :   str  ):
if   item_id   !=   "plumbus"  :
raise   HTTPException  (
status_code  =  403  ,   detail  =  "You can only update the item: plumbus"
)
return   {  "item_id"  :   item_id  ,   "name"  :   "The great Plumbus"  }

How relative imports work ¶

Tip

If you know perfectly how imports work, continue to the next section below.

A single dot  .
, like in:

from     .dependencies     import   get_token_header

would mean:

Starting in the same package that this module (the file  app/routers/items.py
) lives in (the directory  app/routers/
)...

find the module  dependencies
(an imaginary file at  app/routers/dependencies.py
)...

and from it, import the function  get_token_header
.

But that file doesn't exist, our dependencies are in a file at  app/dependencies.py
.

Remember how our app/file structure looks like:

The two dots  ..
, like in:

from     ..dependencies     import   get_token_header

mean:

Starting in the same package that this module (the file  app/routers/items.py
) lives in (the directory  app/routers/
)...

go to the parent package (the directory  app/
)...

and in there, find the module  dependencies
(the file at  app/dependencies.py
)...

and from it, import the function  get_token_header
.

That works correctly! 🎉

The same way, if we had used three dots  ...
, like in:

from     ...dependencies     import   get_token_header

that would mean:

Starting in the same package that this module (the file  app/routers/items.py
) lives in (the directory  app/routers/
)...

go to the parent package (the directory  app/
)...

then go to the parent of that package (there's no parent package,  app
is the top level 😱)...

and in there, find the module  dependencies
(the file at  app/dependencies.py
)...

and from it, import the function  get_token_header
.

That would refer to some package above  app/
, with its own file  __init__.py
, etc. But we don't have that. So, that would throw an error in our example. 🚨

But now you know how it works, so you can use relative imports in your own apps no matter how complex they are. 🤓

Add some custom  tags
,  responses
, and  dependencies
¶

We are not adding the prefix  /items
nor the  tags=["items"]
to each  path operation  because we added them to the  APIRouter
.

But we can still add  more   tags
that will be applied to a specific  path operation , and also some extra  responses
specific to that  path operation :

Python 3.8+

app/routers/items.py       from     fastapi     import   APIRouter  ,   Depends  ,   HTTPException

from     ..dependencies     import   get_token_header

router   =   APIRouter  (
prefix  =  "/items"  ,
tags  =  [  "items"  ],
dependencies  =  [  Depends  (  get_token_header  )],
responses  =  {  404  :   {  "description"  :   "Not found"  }},
)

fake_items_db   =   {  "plumbus"  :   {  "name"  :   "Plumbus"  },   "gun"  :   {  "name"  :   "Portal Gun"  }}

@router  .  get  (  "/"  )
async   def     read_items  ():
return   fake_items_db

@router  .  get  (  "/  {item_id}  "  )
async   def     read_item  (  item_id  :   str  ):
if   item_id   not   in   fake_items_db  :
raise   HTTPException  (  status_code  =  404  ,   detail  =  "Item not found"  )
return   {  "name"  :   fake_items_db  [  item_id  ][  "name"  ],   "item_id"  :   item_id  }

@router  .  put  (
"/  {item_id}  "  ,
tags  =  [  "custom"  ],
responses  =  {  403  :   {  "description"  :   "Operation forbidden"  }},
)
async   def     update_item  (  item_id  :   str  ):
if   item_id   !=   "plumbus"  :
raise   HTTPException  (
status_code  =  403  ,   detail  =  "You can only update the item: plumbus"
)
return   {  "item_id"  :   item_id  ,   "name"  :   "The great Plumbus"  }

Tip

This last path operation will have the combination of tags:  ["items", "custom"]
.

And it will also have both responses in the documentation, one for  404
and one for  403
.

The main  FastAPI
¶

Now, let's see the module at  app/main.py
.

Here's where you import and use the class  FastAPI
.

This will be the main file in your application that ties everything together.

And as most of your logic will now live in its own specific module, the main file will be quite simple.

Import  FastAPI
¶

You import and create a  FastAPI
class as normally.

And we can even

[Truncated snapshot to keep repository size manageable.]
```
