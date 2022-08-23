#!/bin/bash
set -x
set -o allexport
source .env
set +o allexport

CMD=${1:-/bin/bash}

docker network create $EKORPKIT_APP_DOCKER_NETWORK
