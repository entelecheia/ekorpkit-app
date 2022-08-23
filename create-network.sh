#!/bin/bash
set -x
set -o allexport
source backend/.env
set +o allexport

docker network create $EKORPKIT_APP_DOCKER_NETWORK
