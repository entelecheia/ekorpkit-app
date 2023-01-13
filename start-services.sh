#!/bin/bash
BUILD_PATH="$PWD"
export BUILD_PATH

docker-compose --project-directory ./ --file .docker/docker-compose.yaml --env-file .docker/.env.docker up 
