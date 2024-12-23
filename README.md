# Data Science Dashboard

This is a personal portfolio dashboard designed to showcase the skills and experiences of Dr. Mathew Divine, an expert Data Scientist and AI Strategist. 
This dashboard features a detailed breakdown of both hard and soft skills through interactive charts and tables. 
The content is automatically generated based upon the extsenive project list from Dr. Mathew Divine,
the job profile at hand, a a combination of prompts with instructions on how to handle the assessment.

## Features
- **Interactive Hard Skills Radar Plot**: Visualizes the technical proficiencies.
- **Soft Skills Self-Assessment**: Showcased through tables and radar plots.
- **Downloadable Full Resume**: Available as a PDF.
- **Hosted with Docker and AWS Lightsail**: Containerized and cloud-deployed.

## Roadmap
- [ ] Introduction Video
	- [ ] create the script
	- [ ] record first iteration
- [x] Top Five Job Profiles ✅ 2024-11-04
- [ ] Custom Assessment for Dr. Mathew Divine
	- We have the Top Five automatically created.. This is good. But, the quality is falling behind. Therefore, we need to do something to ensure consistency and the legitimacy of the assessment. I'm thinking about a few different methods.
		- [ ] Change the prompt: use one-shot learning
		- UI Changes
			- [x] ~~Show output in collapsable units~~
			- [x] ~~Show the job-profile in a collapsable format~~
			- [ ] Look into better mechanisms for showing the newly generated page and saving in streamlit
		- [ ] Add a moderation step for assessing the quality of the generated skills-assessment and cover letter
- [ ] Custom Assessment for any Freelancer for any Project
	- [ ] Add extra page for uploading both job-profile and projects list
- [ ] Metrics with automatic posts
	- [ ] Ask for consent for data usage
	- [ ] prototype tracking changes for session
	- [ ] create mechanism for making log files for the assessments
	- [ ] Set up a routine for running analysis on extracted data

## Setup

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/)
- [AWS CLI](https://aws.amazon.com/cli/) configured for your account
- [Make](https://www.gnu.org/software/make/)


### Running Locally
1. **Clone the repository**:
```bash   
git clone https://github.com/mrdivine/Data-Science-Dashboard.git
cd Data-Science-Dashboard

make local
```

This will build the image for your device, and then start the docker container so that 
the app will be available on port `8050`.

### Configuration for AWS Lightsail
Before deploying to lightsail, ensure that you have a `.env` file in the `.lightsail` directory with the following variables defined:

1. **Fill out enviornment file**:
```bash
IMAGE_NAME=your-image-name
REGION=your-region
LIGHTSAIL_SERVICE_NAME=your-service-name
CONTAINER_NAME=your-container-name
```

2. **Build Docker Image dependencies**:
```bash   
  make all
```
And, that's it. Now, if your credentials for AWS are working on your computer, 
you should be able to go to the lightsail console to see your newly running container service.

### Using Makefile for Deployment

This project utilizes `Makefile` commands to automate deployment steps.

1. **Create and Initialize Lightsail Service**:  
This command will create the Lightsail instance and container service for your app.  
```make init```

2. **Build and Push Docker Image to Lightsail**:  
This command will build the Docker image for aws linux 2 image and push it to Lightsail.  
```make build```

3. **Deploy the Application**:  
This command deploys the latest Docker image to the Lightsail service.  
```make deploy```

4. **Build, Push, and Deploy**:  
This command runs both the `build` and `deploy` steps in one go.  
```make build_and_deploy``` or ```make all```



## Contact
- **Dr. Mathew Divine**
- [LinkedIn](https://www.linkedin.com/in/dr-mathew-divine/)
- [Google Scholar](https://scholar.google.de/citations?user=wGJeTZQAAAAJ&hl=en)
