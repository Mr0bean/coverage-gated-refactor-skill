# Nextjs Data Fetching

- URL: https://nextjs.org/docs/app/building-your-application/data-fetching
- Retrieved: 2026-02-14 12:32:06 UTC
- Partition: `nextjs`
- Fetch status: `ok`

## Distilled Key Point

- Keep data fetching close to route/component boundaries and avoid duplication.

## Extracted Source Snapshot

```text
Getting Started: Fetching Data | Next.js
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

Fetching data
Server Components
With the fetch API
With an ORM or database
Client Components
Streaming data with the use API
Community libraries
Deduplicate requests and cache data
Streaming
With loading.js
With <Suspense>
Creating meaningful loading states
Examples
Sequential data fetching
Parallel data fetching
Preloading data
API Reference

Edit this page on GitHub       Scroll to top
App Router        Getting Started        Fetching Data
Copy page

Fetching Data
Last updated  February 11, 2026
This page will walk you through how you can fetch data in  Server and Client Components , and how to  stream  components that depend on data.

Fetching data

Server Components

You can fetch data in Server Components using any asynchronous I/O, such as:

The   fetch
API

An  ORM or database

Reading from the filesystem using Node.js APIs like  fs

With the  fetch
API

To fetch data with the  fetch
API, turn your component into an asynchronous function, and await the  fetch
call. For example:

app/blog/page.tsx
TypeScript
JavaScript  TypeScript

export     default     async     function     Page  () {
const     data     =     await     fetch  (  'https://api.vercel.app/  blog  '  )
const     posts     =     await     data  .json  ()
return   (
<  ul  >
{  posts  .map  ((post)   =>   (
<  li     key  =  {  post  .id}>{  post  .title}</  li  >
))}
</  ul  >
)
}

Good to know:

fetch
responses are not cached by default. However, Next.js will  pre-render  the route and the output will be cached for improved performance. If you'd like to opt into  dynamic rendering , use the  { cache: 'no-store' }
option. See the   fetch
API Reference .

During development, you can log  fetch
calls for better visibility and debugging. See the   logging
API reference .

With an ORM or database

Since Server Components are rendered on the server, you can safely make database queries using an ORM or database client. Turn your component into an asynchronous function, and await the call:

app/blog/page.tsx
TypeScript
JavaScript  TypeScript

import   { db  ,   posts }   from     '@/lib/db'

export     default     async     function     Page  () {
const     allPosts     =     await     db  .select  ()  .from  (posts)
return   (
<  ul  >
{  allPosts  .map  ((post)   =>   (
<  li     key  =  {  post  .id}>{  post  .title}</  li  >
))}
</  ul  >
)
}

Client Components

There are two ways to fetch data in Client Components, using:

React's   use
API

A community library like  SWR        or  React Query

Streaming data with the  use
API

You can use React's   use
API        to  stream  data from the server to client. Start by fetching data in your Server component, and pass the promise to your Client Component as prop:

app/blog/page.tsx
TypeScript
JavaScript  TypeScript

import   Posts   from     '@/app/ui/posts'
import   { Suspense }   from     'react'

export     default     function     Page  () {
// Don't await the data fetching function
const     posts     =     getPosts  ()

return   (
<  Suspense     fallback  =  {<  div  >Loading...</  div  >}>
<  Posts     posts  =  {posts} />
</  Suspense  >
)
}

Then, in your Client Component, use the  use
API to read the promise:

app/ui/posts.tsx
TypeScript
JavaScript  TypeScript

'use client'
import   { use }   from     'react'

export     default     function     Posts  ({
posts  ,
}  :   {
posts  :     Promise  <{ id  :     string  ; title  :     string   }[]>
}) {
const     allPosts     =     use  (posts)

return   (
<  ul  >
{  allPosts  .map  ((post)   =>   (
<  li     key  =  {  post  .id}>{  post  .title}</  li  >
))}
</  ul  >
)
}

In the example above, the  <Posts>
component is wrapped in a   <Suspense>
boundary       . This means the fallback will be shown while the promise is being resolved. Learn more about  streaming .

Community libraries

You can use a community library like  SWR        or  React Query        to fetch data in Client Components. These libraries have their own semantics for caching, streaming, and other features. For example, with SWR:

app/blog/page.tsx
TypeScript
JavaScript  TypeScript

'use client'
import   useSWR   from     'swr'

const     fetcher     =   (url)   =>     fetch  (url)  .then  ((r)   =>     r  .json  ())

export     default     function     BlogPage  () {
const   {   data  ,     error  ,     isLoading   }   =     useSWR  (
'https://api.vercel.app/  blog  '  ,
fetcher
)

if   (isLoading)   return   <  div  >Loading...</  div  >
if   (error)   return   <  div  >Error: {  error  .message}</  div  >

return   (
<  ul  >
{  data  .map  ((post  :   { id  :     string  ; title  :     string   })   =>   (
<  li     key  =  {  post  .id}>{  post  .title}</  li  >
))}
</  ul  >
)
}

Deduplicate requests and cache data

One way to deduplicate  fetch
requests is with  request memoization . With this mechanism,  fetch
calls using  GET
or  HEAD
with the same URL and options in a single render pass are combined into one request. This happens automatically, and you can  opt out  by passing an Abort signal to  fetch
.

Request memoization is scoped to the lifetime of a request.

You can also deduplicate  fetch
requests by using Next.js’  Data Cache , for example by setting  cache: 'force-cache'
in your  fetch
options.

Data Cache allows sharing data across the current render pass and incoming requests.

If you are  not  using  fetch
, and instead using an ORM or database directly, you can wrap your data access with the  React  cache
function.

app/lib/data.ts
TypeScript
JavaScript  TypeScript

import   { cache }   from     'react'
import   { db  ,   posts  ,   eq }   from     '@/  lib  /db'

export     const     getPost     =     cache  (  async   (id  :     string  )   =>   {
const     post     =     await     db  .  query  .  posts  .findFirst  ({
where  :     eq  (  posts  .id  ,     parseInt  (id))  ,
})
})

Streaming

Warning:  The content below assumes the   cacheComponents
config option  is enabled in your application. The flag was introduced in Next.js 15 canary.

When you fetch data in Server Components, the data is fetched and rendered on the server for each request. If you have any slow data requests, the whole route will be blocked from rendering until all the data is fetched.

To improve the initial load time and user experience, you can use streaming to break up the page's HTML into smaller chunks and progressively send those chunks from the server to the client.

There are two ways you can leverage streaming in your application:

Wrapping a page with a   loading.js
file

Wrapping a component with   <Suspense>

With  loading.js

You can create a  loading.js
file in the same folder as your page to stream the  entire page  while the data is being fetched. For example, to stream  app/blog/page.js
, add the file inside the  app/blog
folder.

app/blog/loading.tsx
TypeScript
JavaScript  TypeScript

export     default     function     Loading  () {
// Define the Loading UI here
return   <  div  >Loading...</  div  >
}

On navigation, the user will immediately see the layout and a  loading state  while the page is being rendered. The new content will then be automatically swapped in once rendering is complete.

Behind-the-scenes,  loading.js
will be nested inside  layout.js
, and will automatically wrap the  page.js
file and any children below in a  <Suspense>
boundary.

This approach works well for route segments (layouts and pages), but for more granular streaming, you can use  <Suspense>
.

With  <Suspense>

<Suspense>
allows you to be more granular about what parts of the page to stream. For example, you can immediately show any page content that falls outside of the  <Suspense>
boundary, and stream in the list of blog posts inside the boundary.

app/blog/page.tsx
TypeScript
JavaScript  TypeScript

import   { Suspense }   from     'react'
import   BlogList   from     '@/components/BlogList'
import   BlogListSkeleton   from     '@/components/BlogListSkeleton'

export     default     function     BlogPage  () {
return   (
<  div  >
{  /* This content will be sent to the client immediately */  }
<  header  >
<  h1  >Welcome to the Blog</  h1  >
<  p  >Read the latest posts below.</  p  >
</  header  >
<  main  >
{  /* If there's any dynamic content inside this boundary, it will be streamed in */  }
<  Suspense     fallback  =  {<  BlogListSkeleton   />}>
<  BlogList   />
</  Suspense  >
</  main  >
</  div  >
)
}

Creating meaningful loading states

An instant loading state is fallback UI that is shown immediately to the user after navigation. For the best user experience, we recommend designing loading states that are meaningful and help users understand the app is responding. For example, you can use skeletons and spinners, or a small but meaningful part of future screens such as a cover photo, title, etc.

In development, you can preview and inspect the loading state of your components using the  React Devtools       .

Examples

Sequential data fetching

Sequential data fetching happens when one request depends on data from another.

For example,  <Playlists>
can only fetch data after  <Artist>
completes because it needs the  artistID
:

app/artist/[username]/page.tsx
TypeScript
JavaScript  TypeScript

export     default     async     function     Page  ({
params  ,
}  :   {
params  :     Promise  <{ username  :     string   }>
}) {
const   {   username   }   =     await   params
// Get   artist   information
const     artist     =     await     getArtist  (username)

return   (
<>
<  h1  >{  artist  .name}</  h1  >
{  /* Show fallback UI while the Playlists component is loading */  }
<  Suspense     fallback  =  {<  div  >Loading...</  div  >}>
{  /* Pass the   artist   ID to the Playlists component */  }
<  Playlists     artist  ID  =  {  artist  .id} />
</  Suspense  >
</>
)
}

async     function     Playlists  ({   artist  ID }  :   {   artist  ID  :     string   }) {
// Use the   artist   ID to fetch playlists
const     playlists     =     await     getArtistPlaylists  (  artist  ID)

return   (
<  ul  >
{  playlists  .map  ((playlist)   =>   (
<  li     key  =  {  playlist  .id}>{  playlist  .name}</  li  >
))}
</  ul  >
)
}

In this example,  <Suspense>
allows the playlists to stream in after the artist data loads. However, the page still waits for the artist data before displaying anything. To prevent this, you can wrap the entire page component in a  <Suspense>
boundary (for example, using a   loading.js
file ) to show a loading state immediately.

Ensure your data source can resolve the first request quickly, as it blocks everything else. If you can't optimize the request further, consider  caching  the result if the data changes infrequently.

Parallel data fetching

Parallel data fetching happens when data requests in a route are eagerly initiated and start at the same time.

By default,  layouts and pages  are rendered in parallel. So each segment starts fetching data as soon as possible.

However, within  any  component, multiple  async
/ await
requests can still be sequential if placed after the other. For example,  getAlbums
will be blocked until  getArtist
is resolved:

app/artist/[username]/page.tsx
TypeScript
JavaScript  TypeScript

import   { getArtist  ,   getAlbums }   from     '@/app/lib/data'

export     default     async     function     Page  ({ params }) {
// These requests will be sequential
const   {   username   }   =     await   params
const     artist     =     await     getArtist  (username)
const     albums     =     await     getAlbums  (username)
return   <  div  >{  artist  .name}</  div  >
}

Start multiple requests by calling  fetch
, then await them with   Promise.all
. Requests begin as soon as  fetch
is called.

app/artist/[username]/page.tsx
TypeScript
JavaScript  TypeScript

import   Albums   from     './albums'

async     function     getArtist  (username  :     string  ) {
const     res     =     await     fetch  (  `https://api.example.com/  artist  /  ${  username  }  `  )
return     res  .json  ()
}

async     function     getAlbums  (username  :     string  ) {
const     res     =     await     fetch  (  `https://api.example.com/  artist  /  ${  username  }  /albums`  )
return     res  .json  ()
}

export     default     async     function     Page  ({
params  ,
}  :   {
params  :     Promise  <{ username  :     string   }>
}) {
const   {   username   }   =     await   params

// Initiate requests
const     artist  Data     =     getArtist  (username)
const     albumsData     =     getAlbums  (username)

const   [  artist  ,     albums  ]   =     await     Promise  .all  ([  artist  Data  ,   albumsData])

return   (
<>
<  h1  >{  artist  .name}</  h1  >
<  Albums     list  =  {albums} />
</>
)
}

Good to know:  If one request fails when using  Promise.all
, the entire operation will fail. To handle this, you can use the   Promise.allSettled
method instead.

Preloading data

You can preload data by creating a utility function that you eagerly call above blocking requests.  <Item>
conditionally renders based on the  checkIsAvailable()
function.

You can call  preload()
before  checkIsAvailable()
to eagerly initiate  <Item/>
data dependencies. By the time  <Item/>
is rendered, its data has already been fetched.

app/item/[id]/page.tsx
TypeScript
JavaScript  TypeScript

import   { getItem  ,   checkIsAvailable }   from     '@/lib/data'

export     default     async     function     Page  ({
params  ,
}  :   {
params  :     Promise  <{ id  :     string   }>
}) {
const   {   id   }   =     await   params
// starting loading   item   data
preload  (id)
// perform another asynchronous task
const     isAvailable     =     await     checkIsAvailable  ()

return   isAvailable   ?   <  Item     id  =  {id} />   :     null
}

const     preload     =   (id  :     string  )   =>   {
// void evaluates the given expression and returns undefined
// https://developer.mozilla.org/docs/Web/JavaScript/Reference/Operators/void
void     getItem  (id)
}

export     async     function     Item  ({ id }  :   { id  :     string   }) {
const     result     =     await     getItem  (id)
// ...
}

Additionally, you can use React's   cache
function        and the   server-only
package        to create a reusable utility function. This approach allows you to cache the data fetching function and ensure that it's only executed on the server.

utils/get-item.ts
TypeScript
JavaScript  TypeScript

import   { cache }   from     'react'
import     'server-only'
import   { getItem }   from     '@/lib/data'

export     const     preload     =   (id  :     string  )   =>   {
void     getItem  (id)
}

export     const     getItem     =     cache  (  async   (id  :     string  )   =>   {
// ...
})

API Reference
Learn more about the features mentioned in this page by reading the API Reference.

Data Security
Learn the built-in data security features in Next.js and learn best practices for protecting your application's data.

fetch
API reference for the extended fetch function.

loading.js
API reference for the loading.js file.

logging
Configure how data fetches are logged to the console when running Next.js in development mode.

taint
Enable tainting Objects and Values.

Previous   Cache Components

Next   Updating Data
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
