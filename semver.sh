#!/bin/bash

git checkout master
git pull origin master
git fetch --tags -f
docker run -it --rm -v $PWD:/git-semver mdomke/git-semver:v4.0.1 -no-hash -no-patch | sed 's/.$//'