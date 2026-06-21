#!/usr/bin/env bash
set -v

# GitHub Pages' native build uses the github-pages gem (Jekyll 3.x), which is
# incompatible with Ruby 3.4+/4.0. Pin to Homebrew's Ruby 3.3 to match prod.
export PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"

# Old jekyll-sass-converter reads .scss as US-ASCII unless a UTF-8 locale is set,
# which fails on the theme's UTF-8 partials.
export LANG="${LANG:-en_US.UTF-8}"
export LC_ALL="${LC_ALL:-en_US.UTF-8}"

bundle exec jekyll serve --host 0.0.0.0 --watch --unpublished
