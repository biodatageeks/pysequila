#!/bin/sh

cd docs
echo $VERSION
if  echo $VERSION | grep -Eq "SNAPSHOT$"; then
    docker build --no-cache -t biodatageeks/$CI_PROJECT_NAME-snap-doc .
    if [ $(docker ps | grep $CI_PROJECT_NAME-snap-doc | wc -l) -gt 0 ]; then docker stop $CI_PROJECT_NAME-snap-doc && docker rm $CI_PROJECT_NAME-snap-doc; fi
    docker run -p ${DOC_PORT_PREFIX}81:80 -d --name $CI_PROJECT_NAME-snap-doc biodatageeks/$CI_PROJECT_NAME-snap-doc
else
    docker build --no-cache -t biodatageeks/$CI_PROJECT_NAME-doc .
    if [ $(docker ps | grep $CI_PROJECT_NAME-doc | wc -l) -gt 0 ]; then docker stop $CI_PROJECT_NAME-doc && docker rm $CI_PROJECT_NAME-doc; fi
    docker run -d -p ${DOC_PORT_PREFIX}80:80 --name $CI_PROJECT_NAME-doc biodatageeks/$CI_PROJECT_NAME-doc
fi


