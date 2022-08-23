#!/bin/bash
set -x
set -o allexport
source .env
set +o allexport

docker run -it --rm \
  --env-file .env \
  --net $EKORPKIT_APP_DOCKER_NETWORK \
  --publish $EKORPKIT_FRONTEND_HOST_PORT:$EKORPKIT_FRONTEND_DOCKER_PORT \
  --volume ${PWD}${EKORPKIT_FRONTEND_APP_DIR}:${EKORPKIT_FRONTEND_APP_DIR} \
  --volume $HOST_WORKSPACE_ROOT:$EKORPKIT_WORKSPACE_ROOT \
  --name $EKORPKIT_FRONTEND_DOCKER_CONTAINER_NAME \
  $EKORPKIT_FRONTEND_DOCKER_IMAGE_NAME:latest
  