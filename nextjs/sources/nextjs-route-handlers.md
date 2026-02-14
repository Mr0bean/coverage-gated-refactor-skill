# Nextjs Route Handlers

- URL: https://nextjs.org/docs/app/building-your-application/routing/route-handlers
- Retrieved: 2026-02-14 12:32:07 UTC
- Partition: `nextjs`
- Fetch status: `ok`

## Distilled Key Point

- Use Route Handlers for app-owned API endpoints and boundary control.

## Extracted Source Snapshot

```text
File-system conventions: route.js | Next.js
Skip to content
Search documentation...  Search... ⌘K

Showcase  Docs  Blog  Templates      Enterprise
Search documentation...  Search... ⌘K          Feedback    Learn

Menu

Using App Router
Features available in /app

Latest Version
16.1.6

Getting Started
Installation

Project Structure

Layouts and Pages

Linking and Navigating

Server and Client Components

Cache Components

Fetching Data

Updating Data

Caching and Revalidating

Error Handling

CSS

Image Optimization

Font Optimization

Metadata and OG images

Route Handlers

Proxy

Deploying

Upgrading

Guides
Analytics

Authentication

Backend for Frontend

Caching

CI Build Caching

Content Security Policy

CSS-in-JS

Custom Server

Data Security

Debugging

Draft Mode

Environment Variables

Forms

ISR

Instrumentation

Internationalization

JSON-LD

Lazy Loading

Development Environment

Next.js MCP Server

MDX

Memory Usage

Migrating
App Router

Create React App

Vite

Multi-tenant

Multi-zones

OpenTelemetry

Package Bundling

Prefetching

Production

PWAs

Public pages

Redirecting

Sass

Scripts

Self-Hosting

SPAs

Static Exports

Tailwind CSS v3

Testing
Cypress

Jest

Playwright

Vitest

Third Party Libraries

Upgrading
Codemods

Version 14

Version 15

Version 16

Videos

API Reference
Directives
use cache

use cache: private

use cache: remote

use client

use server

Components
Font

Form Component

Image Component

Link Component

Script Component

File-system conventions
default.js

Dynamic Segments

error.js

forbidden.js

instrumentation.js

instrumentation-client.js

Intercepting Routes

layout.js

loading.js

mdx-components.js

not-found.js

page.js

Parallel Routes

proxy.js

public

route.js

Route Groups

Route Segment Config

src

template.js

unauthorized.js

Metadata Files
favicon, icon, and apple-icon

manifest.json

opengraph-image and twitter-image

robots.txt

sitemap.xml

Functions
after

cacheLife

cacheTag

connection

cookies

draftMode

fetch

forbidden

generateImageMetadata

generateMetadata

generateSitemaps

generateStaticParams

generateViewport

headers

ImageResponse

NextRequest

NextResponse

notFound

permanentRedirect

redirect

refresh

revalidatePath

revalidateTag

unauthorized

unstable_cache

unstable_noStore

unstable_rethrow

updateTag

useLinkStatus

useParams

usePathname

useReportWebVitals

useRouter

useSearchParams

useSelectedLayoutSegment

useSelectedLayoutSegments

userAgent

Configuration
next.config.js
experimental.adapterPath

allowedDevOrigins

appDir

assetPrefix

authInterrupts

basePath

browserDebugInfoInTerminal

cacheComponents

cacheHandlers

cacheLife

compress

crossOrigin

cssChunking

devIndicators

distDir

env

expireTime

exportPathMap

generateBuildId

generateEtags

headers

htmlLimitedBots

httpAgentOptions

images

cacheHandler

inlineCss

isolatedDevBuild

logging

mdxRs

onDemandEntries

optimizePackageImports

output

pageExtensions

poweredByHeader

productionBrowserSourceMaps

proxyClientMaxBodySize

reactCompiler

reactMaxHeadersLength

reactStrictMode

redirects

rewrites

sassOptions

serverActions

serverComponentsHmrCache

serverExternalPackages

staleTimes

staticGeneration*

taint

trailingSlash

transpilePackages

turbopack

turbopackFileSystemCache

typedRoutes

typescript

urlImports

useLightningcss

viewTransition

webpack

webVitalsAttribution

TypeScript

ESLint

CLI
create-next-app

next CLI

Edge Runtime

Turbopack

Glossary

Getting Started
Installation

Project Structure

Images

Fonts

CSS

Deploying

Guides
Analytics

Authentication

Babel

CI Build Caching

Content Security Policy

CSS-in-JS

Custom Server

Debugging

Draft Mode

Environment Variables

Forms

ISR

Instrumentation

Internationalization

Lazy Loading

MDX

Migrating
App Router

Create React App

Vite

Multi-Zones

OpenTelemetry

Package Bundling

PostCSS

Preview Mode

Production

Redirecting

Sass

Scripts

Self-Hosting

Static Exports

Tailwind CSS

Testing
Cypress

Jest

Playwright

Vitest

Third Party Libraries

Upgrading
Codemods

Version 10

Version 11

Version 12

Version 13

Version 14

Version 9

Building Your Application
Routing
Pages and Layouts

Dynamic Routes

Linking and Navigating

Custom App

Custom Document

API Routes

Custom Errors

Rendering
Server-side Rendering (SSR)

Static Site Generation (SSG)

Automatic Static Optimization

Client-side Rendering (CSR)

Data Fetching
getStaticProps

getStaticPaths

Forms and Mutations

getServerSideProps

Client-side Fetching

Configuring
Error Handling

API Reference
Components
Font

Form

Head

Image

Image (Legacy)

Link

Script

File-system conventions
instrumentation.js

Proxy

public

src Directory

Functions
getInitialProps

getServerSideProps

getStaticPaths

getStaticProps

NextRequest

NextResponse

useParams

useReportWebVitals

useRouter

useSearchParams

userAgent

Configuration
next.config.js Options
experimental.adapterPath

allowedDevOrigins

assetPrefix

basePath

bundlePagesRouterDependencies

compress

crossOrigin

devIndicators

distDir

env

exportPathMap

generateBuildId

generateEtags

headers

httpAgentOptions

images

isolatedDevBuild

onDemandEntries

optimizePackageImports

output

pageExtensions

poweredByHeader

productionBrowserSourceMaps

experimental.proxyClientMaxBodySize

reactStrictMode

redirects

rewrites

serverExternalPackages

trailingSlash

transpilePackages

turbopack

typescript

urlImports

useLightningcss

webpack

webVitalsAttribution

TypeScript

ESLint

CLI
create-next-app CLI

next CLI

Edge Runtime

Turbopack

Architecture
Accessibility

Fast Refresh

Next.js Compiler

Supported Browsers

Community
Contribution Guide

Rspack

On this page

Reference
HTTP Methods
Parameters
request (optional)
context (optional)
Route Context Helper
Examples
Cookies
Headers
Revalidating Cached Data
Redirects
Dynamic Route Segments
Static Generation with generateStaticParams
URL Query Parameters
Streaming
Request Body
Request Body FormData
CORS
Webhooks
Non-UI Responses
Segment Config Options
Version History

Edit this page on GitHub       Scroll to top
API Reference        File-system conventions        route.js
Copy page

route.js
Last updated  February 11, 2026
Route Handlers allow you to create custom request handlers for a given route using the Web  Request        and  Response        APIs.

route.ts
TypeScript
JavaScript  TypeScript

export     async     function     GET  () {
return     Response  .json  ({ message  :     'Hello World'   })
}

Reference

HTTP Methods

A  route  file allows you to create custom request handlers for a given route. The following  HTTP methods        are supported:  GET
,  POST
,  PUT
,  PATCH
,  DELETE
,  HEAD
, and  OPTIONS
.

route.ts
TypeScript
JavaScript  TypeScript

export     async     function     GET  (request  :     Request  ) {}

export     async     function     HEAD  (request  :     Request  ) {}

export     async     function     POST  (request  :     Request  ) {}

export     async     function     PUT  (request  :     Request  ) {}

export     async     function     DELETE  (request  :     Request  ) {}

export     async     function     PATCH  (request  :     Request  ) {}

// If `OPTIONS` is not defined, Next.js will automatically implement `OPTIONS` and set the appropriate Response `Allow` header depending on the other methods defined in the Route Handler.
export     async     function     OPTIONS  (request  :     Request  ) {}

Parameters

request
(optional)

The  request
object is a  NextRequest  object, which is an extension of the Web  Request        API.  NextRequest
gives you further control over the incoming request, including easily accessing  cookies
and an extended, parsed, URL object  nextUrl
.

route.ts
TypeScript
JavaScript  TypeScript

import     type   { NextRequest }   from     'next/server'

export     async     function     GET  (request  :     NextRequest  ) {
const     url     =     request  .nextUrl
}

context
(optional)

params
: a promise that resolves to an object containing the  dynamic route parameters  for the current route.

app/dashboard/[team]/route.ts
TypeScript
JavaScript  TypeScript

export     async     function     GET  (
request  :     Request  ,
{ params }  :   { params  :     Promise  <{ team  :     string   }> }
) {
const   {   team   }   =     await   params
}

Example
URL
params

app/dashboard/[team]/route.js

/dashboard/1

Promise<{ team: '1' }>

app/shop/[tag]/[item]/route.js

/shop/1/2

Promise<{ tag: '1', item: '2' }>

app/blog/[...slug]/route.js

/blog/1/2

Promise<{ slug: ['1', '2'] }>

Route Context Helper

You can type the Route Handler context using  RouteContext
to get strongly typed  params
from a route literal.  RouteContext
is a globally available helper.

app/users/[id]/route.ts

import     type   { NextRequest }   from     'next/server'

export     async     function     GET  (_req  :     NextRequest  ,   ctx  :     RouteContext  <  '/  users  /[id]'  >) {
const   {   id   }   =     await     ctx  .params
return     Response  .json  ({ id })
}

Good to know

Types are generated during  next dev
,  next build
or  next typegen
.

After type generation, the  RouteContext
helper is globally available. It doesn't need to be imported.

Examples

Cookies

You can read or set cookies with   cookies
from  next/headers
.

route.ts
TypeScript
JavaScript  TypeScript

import   { cookies }   from     'next/headers'

export     async     function     GET  (request  :     NextRequest  ) {
const     cookieStore     =     await     cookies  ()

const     a     =     cookieStore  .get  (  'a'  )
const     b     =     cookieStore  .set  (  'b'  ,     '1'  )
const     c     =     cookieStore  .delete  (  'c'  )
}

Alternatively, you can return a new  Response
using the   Set-Cookie
header.

app/api/route.ts
TypeScript
JavaScript  TypeScript

import   { cookies }   from     'next/headers'

export     async     function     GET  (request  :     Request  ) {
const     cookieStore     =     await     cookies  ()
const     token     =     cookieStore  .get  (  'token'  )

return     new     Response  (  'Hello, Next.js!'  ,   {
status  :     200  ,
headers  :   {   'Set-Cookie'  :     `token=  ${  token  .value  }  `   }  ,
})
}

You can also use the underlying Web APIs to read cookies from the request (  NextRequest
):

app/api/route.ts
TypeScript
JavaScript  TypeScript

import   {   type   NextRequest }   from     'next/server'

export     async     function     GET  (request  :     NextRequest  ) {
const     token     =     request  .  cookies  .get  (  'token'  )
}

Headers

You can read headers with   headers
from  next/headers
.

route.ts
TypeScript
JavaScript  TypeScript

import   { headers }   from     'next/headers'
import     type   { NextRequest }   from     'next/server'

export     async     function     GET  (request  :     NextRequest  ) {
const     headersList     =     await     headers  ()
const     referer     =     headersList  .get  (  'referer'  )
}

This  headers
instance is read-only. To set headers, you need to return a new  Response
with new  headers
.

app/api/route.ts
TypeScript
JavaScript  TypeScript

import   { headers }   from     'next/headers'

export     async     function     GET  (request  :     Request  ) {
const     headersList     =     await     headers  ()
const     referer     =     headersList  .get  (  'referer'  )

return     new     Response  (  'Hello, Next.js!'  ,   {
status  :     200  ,
headers  :   { referer  :   referer }  ,
})
}

You can also use the underlying Web APIs to read headers from the request (  NextRequest
):

app/api/route.ts
TypeScript
JavaScript  TypeScript

import   {   type   NextRequest }   from     'next/server'

export     async     function     GET  (request  :     NextRequest  ) {
const     requestHeaders     =     new     Headers  (  request  .headers)
}

Revalidating Cached Data

You can  revalidate cached data  using the  revalidate
route segment config option.

app/posts/route.ts
TypeScript
JavaScript  TypeScript

export     const     revalidate     =     60

export     async     function     GET  () {
const     data     =     await     fetch  (  'https://api.vercel.app/blog'  )
const     posts     =     await     data  .json  ()

return     Response  .json  (  posts  )
}

Redirects

app/api/route.ts
TypeScript
JavaScript  TypeScript

import   { redirect }   from     'next/navigation'

export     async     function     GET  (request  :     Request  ) {
redirect  (  'https://nextjs.org/'  )
}

Dynamic Route Segments

Route Handlers can use  Dynamic Segments  to create request handlers from dynamic data.

app/items/[slug]/route.ts
TypeScript
JavaScript  TypeScript

export     async     function     GET  (
request  :     Request  ,
{ params }  :   { params  :     Promise  <{ slug  :     string   }> }
) {
const   {   slug   }   =     await   params   // 'a', 'b', or 'c'
}

Route
Example URL
params

app/items/[slug]/route.js

/items/a

Promise<{ slug: 'a' }>

app/items/[slug]/route.js

/items/b

Promise<{ slug: 'b' }>

app/items/[slug]/route.js

/items/c

Promise<{ slug: 'c' }>

Static Generation with  generateStaticParams

You can use   generateStaticParams
with dynamic Route Handlers to statically generate responses at build time for specified params, while handling other params dynamically at request time.

When using  Cache Components , you can combine  generateStaticParams
with  use cache
to enable data caching for both prerendered and runtime params.

See the  generateStaticParams with Route Handlers  documentation for examples and details.

URL Query Parameters

The request object passed to the Route Handler is a  NextRequest
instance, which includes  some additional convenience methods , such as those for more easily handling query parameters.

app/api/search/route.ts
TypeScript
JavaScript  TypeScript

import   {   type   NextRequest }   from     'next/server'

export     function     GET  (request  :     NextRequest  ) {
const     searchParams     =     request  .  nextUrl  .searchParams
const     query     =     searchParams  .get  (  'query'  )
// query is "hello" for /  api  /search?query=hello
}

Streaming

Streaming is commonly used in combination with Large Language Models (LLMs), such as OpenAI, for AI-generated content. Learn more about the  AI SDK       .

app/api/chat/route.ts
TypeScript
JavaScript  TypeScript

import   { openai }   from     '@ai-sdk/openai'
import   { StreamingTextResponse  ,   streamText }   from     'ai'

export     async     function     POST  (req  :     Request  ) {
const   {   messages   }   =     await     req  .json  ()
const     result     =     await     streamText  ({
model  :     openai  (  'gpt-4-turbo'  )  ,
messages  ,
})

return     new     StreamingTextResponse  (  result  .toAIStream  ())
}

These abstractions use the Web APIs to create a stream. You can also use the underlying Web APIs directly.

app/api/route.ts
TypeScript
JavaScript  TypeScript

// https://developer.mozilla.org/docs/Web/API/ReadableStream#convert_async_iterator_to_stream
function     iteratorToStream  (iterator  :     any  ) {
return     new     ReadableStream  ({
async     pull  (controller) {
const   {   value  ,     done   }   =     await     iterator  .next  ()

if   (done) {
controller  .close  ()
}   else   {
controller  .enqueue  (value)
}
}  ,
})
}

function     sleep  (time  :     number  ) {
return     new     Promise  ((resolve)   =>   {
setTimeout  (resolve  ,   time)
})
}

const     encoder     =     new     TextEncoder  ()

async     function*     makeIterator  () {
yield     encoder  .encode  (  '<p>One</p>'  )
await     sleep  (  200  )
yield     encoder  .encode  (  '<p>Two</p>'  )
await     sleep  (  200  )
yield     encoder  .encode  (  '<p>Three</p>'  )
}

export     async     function     GET  () {
const     iterator     =     makeIterator  ()
const     stream     =     iteratorToStream  (iterator)

return     new     Response  (stream)
}

Request Body

You can read the  Request
body using the standard Web API methods:

app/items/route.ts
TypeScript
JavaScript  TypeScript

export     async     function     POST  (request  :     Request  ) {
const     res     =     await     request  .json  ()
return     Response  .json  ({ res })
}

Request Body FormData

You can read the  FormData
using the  request.formData()
function:

app/items/route.ts
TypeScript
JavaScript  TypeScript

export     async     function     POST  (request  :     Request  ) {
const     formData     =     await     request  .formData  ()
const     name     =     formData  .get  (  'name'  )
const     email     =     formData  .get  (  'email'  )
return     Response  .json  ({ name  ,   email })
}

Since  formData
data are all strings, you may want to use   zod-form-data
to validate the request and retrieve data in the format you prefer (e.g.  number
).

CORS

You can set CORS headers for a specific Route Handler using the standard Web API methods:

app/api/route.ts
TypeScript
JavaScript  TypeScript

export     async     function     GET  (request  :     Request  ) {
return     new     Response  (  'Hello, Next.js!'  ,   {
status  :     200  ,
headers  :   {
'Access-Control-Allow-Origin'  :     '*'  ,
'Access-Control-Allow-Methods'  :     'GET, POST, PUT, DELETE, OPTIONS'  ,
'Access-Control-Allow-Headers'  :     'Content-Type, Authorization'  ,
}  ,
})
}

Good to know :

To add CORS headers to multiple Route Handlers, you can use  Proxy  or the   next.config.js
file .

Webhooks

You can use a Route Handler to receive webhooks from third-party services:

app/api/route.ts
TypeScript
JavaScript  TypeScript

export     async     function     POST  (request  :     Request  ) {
try   {
const     text     =     await     request  .text  ()
// Process the webhook payload
}   catch   (error) {
return     new     Response  (  `Webhook error:   ${  error  .message  }  `  ,   {
status  :     400  ,
})
}

return     new     Response  (  'Success!'  ,   {
status  :     200  ,
})
}

Notably, unlike API Routes with the Pages Router, you do not need to use  bodyParser
to use any additional configuration.

Non-UI Responses

You can use Route Handlers to return non-UI content. Note that   sitemap.xml
,   robots.txt
,   app icons
, and  open graph images  all have built-in support.

app/rss.xml/route.ts
TypeScript
JavaScript  TypeScript

export     async     function     GET  () {
return     new     Response  (
`<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">

<channel>
<title>Next.js Documentation</title>
<link>https://nextjs.org/docs</link>
<description>The React Framework for the Web</description>
</channel>

</rss>`  ,
{
headers  :   {
'Content-Type'  :     'text/xml'  ,
}  ,
}
)
}

Segment Config Options

Route Handlers use the same  route segment configuration  as pages and layouts.

app/items/route.ts
TypeScript
JavaScript  TypeScript

export     const     dynamic     =     'auto'
export     const     dynamicParams     =     true
export     const     revalidate     =     false
export     const     fetchCache     =     'auto'
export     const     runtime     =     'nodejs'
export     const     preferredRegion     =     'auto'

See the  API reference  for more details.

Version History

Version
Changes

v15.0.0-RC

context.params
is now a promise. A  codemod  is available

v15.0.0-RC

The default caching for  GET
handlers was changed from static to dynamic

v13.2.0

Route Handlers are introduced.

Previous   public

Next   Route Groups
Was this helpful?

supported.

Send

Resources
Docs  Support Policy  Learn  Showcase  Blog  Team   Analytics   Next.js Conf   Previews   Evals
More
Next.js Commerce    Contact Sales   Community  GitHub  Releases  Telemetry  Governance
About Vercel
Next.js + Vercel    Open Source Software   GitHub  Bluesky  X
Legal
Privacy Policy  Cookie Preferences
Subscribe to our newsletter
Stay updated on new releases and features, guides, and case studies.
Subscribe

©  2026  Vercel, Inc.
```
