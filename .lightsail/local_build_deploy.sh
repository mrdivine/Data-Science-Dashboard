#!/bin/bash

# Source environment variables
source .lightsail/config.env

docker build -t $IMAGE_NAME .
docker run -p 8501:8501 -v $(pwd)/:/app $IMAGE_NAME