#!/bin/bash

function print_usage() {
  echo -e "Usage: ./build.sh <Docker Image version> \nExample: ./build.sh v1"
}

echo "number of arguments is " $#

if [ "$#" -lt 1 ]; then
  print_usage
  exit 1
fi

IMAGE_VERSION=$1
IMAGE_TAG="punithmgp/flask-ipl:"$IMAGE_VERSION

docker image build -t $IMAGE_TAG . 

docker image push $IMAGE_TAG

