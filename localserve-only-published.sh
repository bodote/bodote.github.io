#!/usr/bin/env bash

# Match GitHub Pages' build env: Homebrew Ruby 3.3 + a UTF-8 locale.
# (The github-pages gem / Jekyll 3.x does not work on Ruby 3.4+/4.0.)
export PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"
export LANG="${LANG:-en_US.UTF-8}"
export LC_ALL="${LC_ALL:-en_US.UTF-8}"

bundle exec jekyll serve
