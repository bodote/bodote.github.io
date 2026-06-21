# Bodos Software Blog

Personal software blog by Bodo Teichmann — *"Gedanken und Ideen zu
Softwareentwicklung"* — published at
[bodote.github.io](https://bodote.github.io). Content is mostly in German and
centers on Test-Driven Development (TDD), software architecture, and conference
talks.

Built with [Jekyll](https://jekyllrb.com/) and the
[Minimal Mistakes](https://github.com/mmistakes/minimal-mistakes) theme (used
via `remote_theme`), hosted on **GitHub Pages**.

## Running locally

Requires **Ruby 3.3** (the `github-pages` / Jekyll 3.x stack does not work on
Ruby 3.4+/4.0). On macOS / Apple Silicon:

```bash
brew install ruby@3.3
export PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"
gem install bundler:2.5.7
bundle install      # install dependencies

./localserver.sh    # bundle exec jekyll serve  -> http://localhost:4000
```

The `localserver.sh` / `serve.sh` scripts already pin Ruby 3.3 and a UTF-8
locale, so day to day you can just run them.

To also preview unpublished drafts (posts with `published: false`):

```bash
./serve.sh          # serve on 0.0.0.0, --watch, --unpublished
```

`update.sh` documents how to refresh `Gemfile.lock`. Dependency updates are
automated via Renovate.

## Project structure

| Path | Purpose |
|------|---------|
| `_config.yml` | Site settings, theme, plugins (restart server after edits) |
| `_posts/` | Blog posts (`YYYY-MM-DD-title.md`) |
| `_pages/` | Standalone pages (about, impressum, archives) |
| `_data/navigation.yml` | Top navigation menu |
| `_includes/` | Custom theme include overrides |
| `assets/` | Images, `css/main.scss`, talk slides (`powerpoints/`) |
| `_site/` | Generated output (git-ignored, do not edit) |

## Writing a post

Add a Markdown file to `_posts/` named `YYYY-MM-DD-title.md` with front matter:

```yaml
---
title: "Post title"
date: 2025-07-10
published: true
categories:
  - Vorträge
tags:
  - TDD
toc: true
classes: wide
---
```

## Contributing with AI agents

See [AGENTS.md](AGENTS.md) for conventions, guardrails, and build/verify
instructions aimed at AI coding agents.

---

Based on the [Minimal Mistakes Jekyll theme](https://github.com/mmistakes/minimal-mistakes).
