#!/bin/bash

# Source environment variables
source .lightsail/config.env

# Step 1: Create a new Lightsail container service
echo "Creating new Lightsail container service..."
aws lightsail create-container-service \
  --service-name $SERVICE_NAME \
  --power $POWER \
  --scale $SCALE \
  --region $REGION

echo "Lightsail container service '$SERVICE_NAME' created successfully!"
