# AGENTS.md

Guidance for AI coding agents working in this repository.

## What this is

A personal software blog ("Bodos Software Blog") built with **Jekyll** and the
**Minimal Mistakes** theme (pulled in via `remote_theme`), published through
**GitHub Pages** at `bodote.github.io`. Content is mostly in German and focuses
on Test-Driven Development (TDD), software architecture, and related talks.

There is **no application code** here — this is a static-site content repo. Work
consists of editing Markdown/HTML content, YAML config, and SCSS, then letting
Jekyll/GitHub Pages build the site.

## Tech stack

- **Jekyll** static site generator (Ruby, Bundler).
- **Minimal Mistakes** theme via `remote_theme: mmistakes/minimal-mistakes` — the
  theme is *not* vendored. Layouts, includes, and SASS come from the gem; only
  overrides live in this repo.
- **GitHub Pages** for hosting/build. Stay within the `github-pages` gem's
  supported plugin set (see `Gemfile`).
- **kramdown** Markdown, Liquid templating.

## Layout

| Path | Purpose |
|------|---------|
| `_config.yml` | Site-wide settings, theme, plugins, author/footer, defaults. **Not** hot-reloaded — restart the server after changes. |
| `_posts/` | Blog posts. Filename convention `YYYY-MM-DD-title.md`. |
| `_pages/` | Standalone pages (about, impressum, archives, 404, splash). |
| `_data/navigation.yml` | Top navigation menu. |
| `_includes/` | Custom include overrides (e.g. `mastodon_feed.html`). |
| `assets/` | `images/`, `css/main.scss`, `powerpoints/` (talk slides/PDFs). |
| `index.html` | Home page front matter (uses theme `home` layout). |
| `_site/` | Generated output — **do not edit**, git-ignored. |
| `doc/`, `*.odt`, `odt_convert.sh` | Tooling to export posts to ODT via pandoc. |

## Post / page front matter conventions

Posts use YAML front matter. A representative post:

```yaml
---
title: "..."
date: 2025-07-10
published: true   # false to keep it out of the published build
visible: true
categories:
  - Vorträge
tags:
  - TDD
toc: true         # table of contents sidebar
classes: wide     # full-width layout
---
```

Site defaults (in `_config.yml`) already set `layout: single`,
`author_profile`, `read_time`, `comments`, `share`, `related` for all posts —
don't repeat these per-post unless overriding.

## Running locally

**Ruby version matters.** GitHub Pages' native build uses the `github-pages`
gem (Jekyll 3.x / Liquid 4.0.x), which is **incompatible with Ruby 3.4+/4.0**
(removed stdlib gems, and `String#tainted?` which Liquid 4.0.3 still calls). Use
**Ruby 3.3** to match production. On Apple Silicon:

```bash
brew install ruby@3.3
export PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"
gem install bundler:2.5.7
bundle install
```

A UTF-8 locale is also required — the old `jekyll-sass-converter` reads `.scss`
as US-ASCII otherwise and fails on the theme's UTF-8 partials
(`export LANG=en_US.UTF-8`).

Serve options (helper scripts at repo root — both already pin Ruby 3.3 + locale):

```bash
./localserver.sh   # bundle exec jekyll serve
./serve.sh         # serve on 0.0.0.0, --watch, includes --unpublished drafts
```

Then open http://localhost:4000. Use `serve.sh` when you need to preview posts
with `published: false`.

`update.sh` documents how to refresh `Gemfile.lock` (`bundle update` or delete
the lockfile and `bundle install`). Dependency PRs are automated via Renovate
(`renovate.json`).

## Conventions & guardrails

- **Match the existing language** of the file you're editing — most content is
  German; comments in config files are often German too.
- **Never edit `_site/`** — it's build output.
- **Plugins must be GitHub-Pages-compatible.** Adding an arbitrary gem can break
  the hosted build even if it works locally.
- After changing `_config.yml`, **restart** the Jekyll server (it is not
  reloaded on watch).
- New posts go in `_posts/` with a `YYYY-MM-DD-` filename prefix and valid front
  matter; new images in `assets/images/`.
- This repo contains stray macOS `.DS_Store` files (untracked) — ignore them;
  don't commit them.

## Verifying changes

There are no tests. Verify by building/serving locally and visually checking the
affected page(s). A successful `bundle exec jekyll serve` with no Liquid/build
errors is the baseline check before committing.
