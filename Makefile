# Makefile

# Load environment variables from .lightsail/config.env
include .lightsail/config.env

# Define default target
.PHONY: init build deploy all

# Target to initialize: container service
init:
	@echo "Initializing Lightsail container service..."
	@bash .lightsail/create_service.sh

# Target to build Docker image and push to Lightsail
build:
	@echo "Building and pushing Docker image..."
	@bash .lightsail/build_and_push_image.sh

# Target to deploy the Docker image to Lightsail service
deploy:
	@echo "Deploying Docker image to Lightsail service..."
	@bash .lightsail/deploy_image.sh

# Combined target to build and deploy
build_and_deploy: build deploy
	@echo "Build and deployment complete!"

# locally deploy
local: local
	@echo "Building and running Docker image locally..."
	@bash .lightsail/local_build_deploy.sh


# Default target
all: init build deploy
	@echo "All steps completed!"
