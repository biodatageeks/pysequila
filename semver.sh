#!/bin/bash

# Test version, without pushing tag to repo
git checkout master && git pull origin master && git fetch --tags -f && docker run -it --rm -v $PWD:/git-semver mdomke/git-semver:v4.0.1 -format x.y.z | sed 's/.$//'


# Full version, with pushing tag to repo
# git checkout master && git pull origin master && git fetch --tags -f && docker run -it --rm -v $PWD:/git-semver mdomke/git-semver:v4.0.1 -format x.y.z | sed 's/.$//' | xargs -I {} sh -c "echo {} && git tag {} && git push origin {}"
