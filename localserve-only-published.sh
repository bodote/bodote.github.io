#!/usr/bin/env bash

# Match GitHub Pages' build env: Ruby 3.3 + a UTF-8 locale.
# (The github-pages gem / Jekyll 3.x does not work on Ruby 3.4+/4.0.)
# Prefer rbenv (Ruby version from .ruby-version); fall back to Homebrew's ruby@3.3.
if command -v rbenv >/dev/null 2>&1; then
  eval "$(rbenv init - bash)"
else
  export PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"
fi
export LANG="${LANG:-en_US.UTF-8}"
export LC_ALL="${LC_ALL:-en_US.UTF-8}"

bundle exec jekyll serve
