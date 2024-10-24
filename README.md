# Data Science Dashboard

This is a personal portfolio dashboard designed to showcase the skills and experiences of Dr. Mathew Divine, an expert Data Scientist and AI Strategist. This dashboard features a detailed breakdown of both hard and soft skills through interactive charts and tables. The content for the dashboard was created with ChatGPT, the Job Profile for a Product Owner, my resume, and one prompt. 

## Features
- **Interactive Hard Skills Radar Plot**: Visualizes the technical proficiencies.
- **Soft Skills Self-Assessment**: Showcased through tables and radar plots.
- **Downloadable Full Resume**: Available as a PDF.
- **Hosted with Docker and AWS Lightsail**: Containerized and cloud-deployed.

## Setup

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [AWS CLI](https://aws.amazon.com/cli/) configured for your account
- [Make](https://www.gnu.org/software/make/)

### Configuration
Before deploying, ensure that you have a `.env` file in the `.lightsail` directory with the following variables defined:

```bash
IMAGE_NAME=your-image-name
REGION=your-region
LIGHTSAIL_SERVICE_NAME=your-service-name
CONTAINER_NAME=your-container-name
```
### Running Locally
1. **Clone the repository**:
```bash   
git clone https://github.com/mrdivine/Data-Science-Dashboard.git
cd Data-Science-Dashboard
```
2. **Build Docker Image dependencies**:
```bash   
  make 
```
3. **Run the Streamlit app**:
```bash
streamlit run app/Home.py
```
4. **Building and running Docker locally**:
```bash
docker build -t your-image-name .
docker run -p 8501:8501 your-image-name
```
### Using Makefile for Deployment

This project utilizes `Makefile` commands to automate deployment steps.

1. **Create and Initialize Lightsail Service**:  
This command will create the Lightsail instance and container service for your app.  
```make init```

2. **Build and Push Docker Image to Lightsail**:  
This command will build the Docker image and push it to Lightsail.  
```make build```

3. **Deploy the Application**:  
This command deploys the latest Docker image to the Lightsail service.  
```make deploy```

4. **Build, Push, and Deploy**:  
This command runs both the `build` and `deploy` steps in one go.  
```make build_and_deploy```

## Deployment

This project is currently deployed on AWS Lightsail using Docker. The deployment process involves the following steps:

1. **Build Docker image** and **push to Lightsail**.
2. **Create a Lightsail container service** (done during initialization).
3. **Deploy the Docker image** to the service.

You can use the provided `Makefile` commands to simplify this process.

## Contact
- **Dr. Mathew Divine**
- [LinkedIn](https://www.linkedin.com/in/dr-mathew-divine/)
- [Google Scholar](https://scholar.google.de/citations?user=wGJeTZQAAAAJ&hl=en)
