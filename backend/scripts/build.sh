#!/bin/bash
set -x
set -o allexport
source .env
set +o allexport

docker build \
    --network=host --rm \
    . -t $EKORPKIT_BACKEND_DOCKER_IMAGE_NAME:$DATESTAMP

docker tag ${EKORPKIT_BACKEND_DOCKER_IMAGE_NAME}:${DATESTAMP} ${EKORPKIT_BACKEND_DOCKER_IMAGE_NAME}:latest
