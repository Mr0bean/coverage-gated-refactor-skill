# Nextjs Project Structure

- URL: https://nextjs.org/docs/app/getting-started/project-structure
- Retrieved: 2026-02-14 12:32:05 UTC
- Partition: `nextjs`
- Fetch status: `ok`

## Distilled Key Point

- Keep route-oriented project structure and clear boundary placement.

## Extracted Source Snapshot

```text
Getting Started: Project Structure | Next.js
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

Folder and file conventions
Top-level folders
Top-level files
Routing Files
Nested routes
Dynamic routes
Route groups and private folders
Parallel and Intercepted Routes
Metadata file conventions
App icons
Open Graph and Twitter images
SEO
Organizing your project
Component hierarchy
Colocation
Private folders
Route groups
src folder
Examples
Store project files outside of app
Store project files in top-level folders inside of app
Split project files by feature or route
Organize routes without affecting the URL path
Opting specific segments into a layout
Opting for loading skeletons on a specific route
Creating multiple root layouts

Edit this page on GitHub       Scroll to top
App Router        Getting Started        Project Structure
Copy page

Project structure and organization
Last updated  February 11, 2026
This page provides an overview of  all  the folder and file conventions in Next.js, and recommendations for organizing your project.

Folder and file conventions

Top-level folders

Top-level folders are used to organize your application's code and static assets.

app

App Router

pages

Pages Router

public

Static assets to be served

src

Optional application source folder

Top-level files

Top-level files are used to configure your application, manage dependencies, run proxy, integrate monitoring tools, and define environment variables.

Next.js

next.config.js

Configuration file for Next.js

package.json

Project dependencies and scripts

instrumentation.ts

OpenTelemetry and Instrumentation file

proxy.ts

Next.js request proxy

.env

Environment variables (should not be tracked by version control)

.env.local

Local environment variables (should not be tracked by version control)

.env.production

Production environment variables (should not be tracked by version control)

.env.development

Development environment variables (should not be tracked by version control)

eslint.config.mjs

Configuration file for ESLint

.gitignore

Git files and folders to ignore

next-env.d.ts

TypeScript declaration file for Next.js (should not be tracked by version control)

tsconfig.json

Configuration file for TypeScript

jsconfig.json

Configuration file for JavaScript

Routing Files

Add  page
to expose a route,  layout
for shared UI such as header, nav, or footer,  loading
for skeletons,  error
for error boundaries, and  route
for APIs.

layout

.js
.jsx
.tsx

Layout

page

.js
.jsx
.tsx

Page

loading

.js
.jsx
.tsx

Loading UI

not-found

.js
.jsx
.tsx

Not found UI

error

.js
.jsx
.tsx

Error UI

global-error

.js
.jsx
.tsx

Global error UI

route

.js
.ts

API endpoint

template

.js
.jsx
.tsx

Re-rendered layout

default

.js
.jsx
.tsx

Parallel route fallback page

Nested routes

Folders define URL segments. Nesting folders nests segments. Layouts at any level wrap their child segments. A route becomes public when a  page
or  route
file exists.
Path
URL pattern
Notes

app/layout.tsx

—
Root layout wraps all routes

app/blog/layout.tsx

—
Wraps  /blog
and descendants

app/page.tsx

/

Public route

app/blog/page.tsx

/blog

Public route

app/blog/authors/page.tsx

/blog/authors

Public route

Dynamic routes

Parameterize segments with square brackets. Use  [segment]
for a single param,  [...segment]
for catch‑all, and  [[...segment]]
for optional catch‑all. Access values via the   params
prop.
Path
URL pattern

app/blog/[slug]/page.tsx

/blog/my-first-post

app/shop/[...slug]/page.tsx

/shop/clothing
,  /shop/clothing/shirts

app/docs/[[...slug]]/page.tsx

/docs
,  /docs/layouts-and-pages
,  /docs/api-reference/use-router

Route groups and private folders

Organize code without changing URLs with route groups   (group)
, and colocate non-routable files with private folders   _folder
.
Path
URL pattern
Notes

app/(marketing)/page.tsx

/

Group omitted from URL

app/(shop)/cart/page.tsx

/cart

Share layouts within  (shop)

app/blog/_components/Post.tsx

—
Not routable; safe place for UI utilities

app/blog/_lib/data.ts

—
Not routable; safe place for utils

Parallel and Intercepted Routes

These features fit specific UI patterns, such as slot-based layouts or modal routing.
Use  @slot
for named slots rendered by a parent layout. Use intercept patterns to render another route inside the current layout without changing the URL, for example, to show a details view as a modal over a list.
Pattern (docs)
Meaning
Typical use case

@folder

Named slot
Sidebar + main content

(.)folder

Intercept same level
Preview sibling route in a modal

(..)folder

Intercept parent
Open a child of the parent as an overlay

(..)(..)folder

Intercept two levels
Deeply nested overlay

(...)folder

Intercept from root
Show arbitrary route in current view

Metadata file conventions

App icons

favicon

.ico

Favicon file

icon

.ico
.jpg
.jpeg
.png
.svg

App Icon file

icon

.js
.ts
.tsx

Generated App Icon

apple-icon

.jpg
.jpeg
,  .png

Apple App Icon file

apple-icon

.js
.ts
.tsx

Generated Apple App Icon

Open Graph and Twitter images

opengraph-image

.jpg
.jpeg
.png
.gif

Open Graph image file

opengraph-image

.js
.ts
.tsx

Generated Open Graph image

twitter-image

.jpg
.jpeg
.png
.gif

Twitter image file

twitter-image

.js
.ts
.tsx

Generated Twitter image

SEO

sitemap

.xml

Sitemap file

sitemap

.js
.ts

Generated Sitemap

robots

.txt

Robots file

robots

.js
.ts

Generated Robots file

Organizing your project

Next.js is  unopinionated  about how you organize and colocate your project files. But it does provide several features to help you organize your project.
Component hierarchy

The components defined in special files are rendered in a specific hierarchy:

layout.js

template.js

error.js
(React error boundary)

loading.js
(React suspense boundary)

not-found.js
(React error boundary for "not found" UI)

page.js
or nested  layout.js

The components are rendered recursively in nested routes, meaning the components of a route segment will be nested  inside  the components of its parent segment.
Colocation

In the  app
directory, nested folders define route structure. Each folder represents a route segment that is mapped to a corresponding segment in a URL path.
However, even though route structure is defined through folders, a route is  not publicly accessible  until a  page.js
or  route.js
file is added to a route segment.
And, even when a route is made publicly accessible, only the  content returned  by  page.js
or  route.js
is sent to the client.
This means that  project files  can be  safely colocated  inside route segments in the  app
directory without accidentally being routable.

Good to know : While you  can  colocate your project files in  app
you don't  have  to. If you prefer, you can  keep them outside the  app
directory .

Private folders

Private folders can be created by prefixing a folder with an underscore:  _folderName

This indicates the folder is a private implementation detail and should not be considered by the routing system, thereby  opting the folder and all its subfolders  out of routing.
Since files in the  app
directory can be  safely colocated by default , private folders are not required for colocation. However, they can be useful for:

Separating UI logic from routing logic.

Consistently organizing internal files across a project and the Next.js ecosystem.

Sorting and grouping files in code editors.

Avoiding potential naming conflicts with future Next.js file conventions.

Good to know :

While not a framework convention, you might also consider marking files outside private folders as "private" using the same underscore pattern.

You can create URL segments that start with an underscore by prefixing the folder name with  %5F
(the URL-encoded form of an underscore):  %5FfolderName
.

If you don't use private folders, it would be helpful to know Next.js  special file conventions  to prevent unexpected naming conflicts.

Route groups

Route groups can be created by wrapping a folder in parenthesis:  (folderName)

This indicates the folder is for organizational purposes and should  not be included  in the route's URL path.
Route groups are useful for:

Organizing routes by site section, intent, or team. e.g. marketing pages, admin pages, etc.

Enabling nested layouts in the same route segment level:

Creating multiple nested layouts in the same segment, including multiple root layouts

Adding a layout to a subset of routes in a common segment

src
folder

Next.js supports storing application code (including  app
) inside an optional   src
folder . This separates application code from project configuration files which mostly live in the root of a project.
Examples

The following section lists a very high-level overview of common strategies. The simplest takeaway is to choose a strategy that works for you and your team and be consistent across the project.

Good to know : In our examples below, we're using  components
and  lib
folders as generalized placeholders, their naming has no special framework significance and your projects might use other folders like  ui
,  utils
,  hooks
,  styles
, etc.

Store project files outside of  app

This strategy stores all application code in shared folders in the  root of your project  and keeps the  app
directory purely for routing purposes.
Store project files in top-level folders inside of  app

This strategy stores all application code in shared folders in the  root of the  app
directory .
Split project files by feature or route

This strategy stores globally shared application code in the root  app
directory and  splits  more specific application code into the route segments that use them.
Organize routes without affecting the URL path

To organize routes without affecting the URL, create a group to keep related routes together. The folders in parenthesis will be omitted from the URL (e.g.  (marketing)
or  (shop)
).
Even though routes inside  (marketing)
and  (shop)
share the same URL hierarchy, you can create a different layout for each group by adding a  layout.js
file inside their folders.
Opting specific segments into a layout

To opt specific routes into a layout, create a new route group (e.g.  (shop)
) and move the routes that share the same layout into the group (e.g.  account
and  cart
). The routes outside of the group will not share the layout (e.g.  checkout
).
Opting for loading skeletons on a specific route

To apply a  loading skeleton  via a  loading.js
file to a specific route, create a new route group (e.g.,  /(overview)
) and then move your  loading.tsx
inside that route group.
Now, the  loading.tsx
file will only apply to your dashboard → overview page instead of all your dashboard pages without affecting the URL path structure.
Creating multiple root layouts

To create multiple  root layouts , remove the top-level  layout.js
file, and add a  layout.js
file inside each route group. This is useful for partitioning an application into sections that have a completely different UI or experience. The  <html>
and  <body>
tags need to be added to each root layout.
In the example above, both  (marketing)
and  (shop)
have their own root layout.

Previous   Installation

Next   Layouts and Pages
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
