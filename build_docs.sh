#!/bin/sh

echo $VERSION

function build_run() {
  CONTAINER_SUFIX=$1
  if  echo $VERSION | grep -Eq "SNAPSHOT$"; then
      docker build --no-cache -t biodatageeks/$CI_PROJECT_NAME-snap-$CONTAINER_SUFIX .
      if [ $(docker ps | grep $CI_PROJECT_NAME-snap-$CONTAINER_SUFIX | wc -l) -gt 0 ]; then docker stop $CI_PROJECT_NAME-snap-$CONTAINER_SUFIX && docker rm $CI_PROJECT_NAME-snap-$CONTAINER_SUFIX; fi
      docker run -p ${DOC_PORT_PREFIX}81:80 -d --name $CI_PROJECT_NAME-snap-$CONTAINER_SUFIX biodatageeks/$CI_PROJECT_NAME-snap-$CONTAINER_SUFIX
  else
      docker build --no-cache -t biodatageeks/$CI_PROJECT_NAME-$CONTAINER_SUFIX .
      if [ $(docker ps | grep $CI_PROJECT_NAME-$CONTAINER_SUFIX | wc -l) -gt 0 ]; then docker stop $CI_PROJECT_NAME-$CONTAINER_SUFIX && docker rm $CI_PROJECT_NAME-$CONTAINER_SUFIX; fi
      docker run -d -p ${DOC_PORT_PREFIX}80:80 --name $CI_PROJECT_NAME-$CONTAINER_SUFIX biodatageeks/$CI_PROJECT_NAME-$CONTAINER_SUFIX
  fi
}

cd docs
build_run "doc"

cd ../page
build_run "page"