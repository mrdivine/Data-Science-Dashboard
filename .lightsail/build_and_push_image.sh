#!/bin/bash

# Source environment variables
source .lightsail/config.env

# Step 1: Build Docker image for linux/amd64 architecture
echo "Building Docker image for lightsail linux/amd64 instance..."
docker buildx build --platform linux/amd64 -t $IMAGE_NAME .

# Step 2: Push Docker image to Lightsail
echo "Pushing Docker image to Lightsail..."
aws lightsail push-container-image \
  --service-name $SERVICE_NAME \
  --label $IMAGE_NAME \
  --image $IMAGE_NAME:latest \
  --region $REGION

echo "Docker image pushed successfully!"
