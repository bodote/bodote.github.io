#!/usr/bin/env bash
echo "jekyll runs only on ruby 2.6.x as of 2021-05-08 , NO ruby 3.x!"
echo "update the lockfile by running bundle update (or)"
bundle update
echo "delete and then respawn the lockfile by running bundle install"
# rm Gemfile.lock
# bundle install