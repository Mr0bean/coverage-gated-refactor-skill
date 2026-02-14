# Nuxt Directory Structure App

- URL: https://nuxt.com/docs/guide/directory-structure/app
- Retrieved: 2026-02-14 12:32:02 UTC
- Partition: `fornt`
- Fetch status: `ok`

## Distilled Key Point

- Use predictable app directory and routing conventions.

## Extracted Source Snapshot

```text
app.vue · Nuxt Directory Structure v4
v4.3.1
Docs
Modules
Templates
Resources
Enterprise
Blog

Search…             k
59.6K

Get Started
Structure
Guide
API
Deploy
Examples
Community

.nuxt
.output
app                            assets
components
composables
layouts
middleware
pages
plugins
utils
app.vue
app.config.ts
error.vue

content
layers
modules
node_modules
public
server
shared
.env
.gitignore
.nuxtignore
.nuxtrc
nuxt.config.ts
package.json
tsconfig.json

Directory Structure

app

app.vue
Copy page

The app.vue file is the main component of your Nuxt application.

If you have a   app/pages/
directory, the   app.vue
file is optional. Nuxt will automatically include a default   app.vue
, but you can still add your own to customize the structure and content as needed.
Usage
Minimal Usage
With Nuxt, the       app/pages/
directory is optional. If it is not present, Nuxt will not include the      vue-router      dependency. This is useful when building a landing page or an application that does not require routing.
app/app.vue
<  template  >
<  h1  >  Hello World!  </  h1  >
</  template  >

Read and edit a live example in  Docs > 4 X > Examples > Hello World .
Usage with Pages
When you have a       app/pages/
directory, you need to use the       <NuxtPage>
component to display the current page:
app/app.vue
<  template  >
<  NuxtPage   />
</  template  >

You can also define the common structure of your application directly in   app.vue
. This is useful when you want to include global elements such as a header or footer:
app/app.vue
<  template  >
<  header  >
Header content
</  header  >
<  NuxtPage   />
<  footer  >
Footer content
</  footer  >
</  template  >

Remember that   app.vue
acts as the main component of your Nuxt application. Anything you add to it (JS and CSS) will be global and included in every page.
Learn more about how to structure your pages using the   app/pages/
directory.
Usage with Layouts
When your application requires different layouts for different pages, you can use the   app/layouts/
directory with the       <NuxtLayout>
component. This allows you to define multiple layouts and apply them per page.
app/app.vue
<  template  >
<  NuxtLayout  >
<  NuxtPage   />
</  NuxtLayout  >
</  template  >

Learn more about how to structure your layouts using the   app/layouts/
directory.

Was this helpful?             🤩                  🙂                  ☹️                  😰

Report an issue          or          Edit this page on GitHub

utils
Use the utils/ directory to auto-import your utility functions throughout your application.

app.config.ts
Expose reactive configuration within your application with the App Config file.

On this page
On this page

Usage         Minimal Usage
Usage with Pages
Usage with Layouts

Community
Become a Sponsor
Master Nuxt
Nuxt Certification

Nuxt on Discord                   Nuxt on Bluesky                   Nuxt on X                   Nuxt on GitHub

Menu                       On this page

Community
Nuxters
Team
Design Kit

Explore
Modules
Templates
Showcase

Enterprise
Agencies
Sponsors

Subscribe to our newsletter
Stay updated on new releases and features, guides, and community updates.

Subscribe

Nuxt on X                   Nuxt on BlueSky                   Nuxt on LinkedIn                   Nuxt on Discord                   Nuxt on GitHub

Copyright © 2016-2026 Nuxt -   MIT License
```
