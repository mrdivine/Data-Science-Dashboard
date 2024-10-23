#!/bin/bash

# Source environment variables
source .lightsail/config.env

# Step 1: Deploy the container to the Lightsail service
echo "Deploying container to Lightsail..."
# Get the container images for the Lightsail service
response=$(aws lightsail get-container-images --service-name $SERVICE_NAME --region $REGION --output json)

# Extract the latest image name based on the most recent createdAt timestamp
latest_image=$(echo $response | jq -r '.containerImages | max_by(.createdAt) | .image')

# Define the deployment configuration in JSON
deployment_config=$(cat <<EOF
{
  "serviceName": "$SERVICE_NAME",
  "containers": {
    "$CONTAINER_NAME": {
      "image": "$latest_image",
      "ports": {
        "8501": "HTTP"
      }
    }
  },
  "publicEndpoint": {
    "containerName": "$CONTAINER_NAME",
    "containerPort": 8501
  }
}
EOF
)

# Deploy the container to Lightsail using the JSON configuration
aws lightsail create-container-service-deployment \
  --cli-input-json "$deployment_config" \
  --region $REGION

echo "Container deployed successfully to the Lightsail service!"