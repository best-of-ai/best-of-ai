---
title: 'How the Site Works'
slug: 'how-the-site-works'
subtitle: 'Hugo, flat files, and a GitHub Actions pipeline. No database.'
order: 8
---

## No database, just files

Every tool is a Markdown file in `content/tools/`. Every category lives in `data/categories.yaml`. There's no admin panel and no backend to manage; the entire site is flat files in a Git repository. The whole thing builds with [Hugo](https://gohugo.io/), a static site generator, into plain HTML.

## What GitHub Actions handles

Three workflows do the boring parts:

- **Deploy** builds and publishes the site on every push to `main`.
- **Issue to PR** reviews tool-submission issues automatically and opens a pull request for anything that fits the format.
- **Update README** regenerates `README.md` whenever tool data changes.

## Why it's built this way

Flat files mean anyone can clone the repository and see exactly what's on the site and why. There's no hidden database to trust; the data is the same file you'd edit to fix it.

## Look at the code

The full source, site templates, scripts, and data, is public at [github.com/best-of-ai/best-of-ai](https://github.com/best-of-ai/best-of-ai).
