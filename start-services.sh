#!/bin/bash
BUILD_PATH="$PWD"

docker-compose --project-directory "${BUILD_PATH}" --file .docker/docker-compose.yaml --env-file .docker/.env.docker up 
