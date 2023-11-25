# MLOps: End-to-end-Machine-Learning-Project-with-MLflow


## Getting started:

- create a github project
- clone the github project
- cd into the project folder
- create and activate conda envirnment for the project 
    *conda env list (check the existing env)
    *conda create -name mlops python=3.10 -y  (another option: conda create -name -p venv mlops python=3.10 -y)
    *conda activate mlops 
    *conda deactivate
    *conda list (show installed package in the environment)
    *onda list > packages.yaml
    (https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment)

- create a project structure (bu running: python  template.py)
- add code into setup.py (which is used to enable the import of the local folder( with __init__) as normal python packages)
- add the required package into requirements.txt (with -e . :at the end allowing to look up for  the setup.py and install the enterprise (owner) packages
- then do: pip install -r requirements.txt 
- LOGGING: create custom logging functionality under MLOps/src/mlopsProject/__init__.py- (test it using "python main.py")
- UTILS  : create utils under mlopsProject/utils/common.py (def read_yaml(), def read_json() and more...)
  * in mlopsProject/utils/common.py following are used:
    -ensure_annotation  (decolator used to make sure input and output types are correct: type inforcement):like making sure an object is returning a    dictionary as type configbox. 
    -configbox: (allows you to access a dictionary values with dot {}) ==> from box import ConfigBox ==> then have dict = ConfigBox({a:1,b:2}) ==> print(dict.a)
         
         
## Workflows
         started with reseach/notebook  select the kernel (Create a notebook for each step. eg:data ingestion step):
		 Note: if you experience a notebook issue, close the vs code and restarted again.

		### BUILD
		1. Update config/config.yaml
		2. Update config/schema.yaml
		3. Update config/params.yaml

		4. update src/mlProject/constants/__init__()

		5. Update src/mlProject/entity/config_entity.py
		6. Update src/mlProject/config/configuration.py 
		7. Update src/mlProject/components/....
		8. Update src/mlProject/pipeline/...
		9. Update the pipeline_build.py

		### INFERENCE
		10. Update the pipeline_inference.py

		NOTE: Check search folder for more details


## MLflow locally
- Install mlflow : pip install mlflow
- Terminal1: Lunch mlflow trucking server : mlflow server --host 127.0.0.1 --port 8080
- Terminal2: lunch mlflow ui server : mlflow ui --host 127.0.0.1 --port 8090
- Terminal3: Lunch your notebook : python -m notebook ===> select the notebook to run


[Documentation](https://mlflow.org/docs/latest/index.html)



### MLflow on remote server : dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow.mlflow \
MLFLOW_TRACKING_USERNAME=entbappy \
MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow.mlflow

export MLFLOW_TRACKING_USERNAME=entbappy 

export MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0

```


# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Go to ECR and then Repositories to create one and the the URI for the created repository
    - Save the URI: 927765266034.dkr.ecr.us-east-2.amazonaws.com/mlops

	
## 4. Create EC2 machine (Ubuntu) 

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Click connect to get the CLI interface

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade -y
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    Go to github project=>setting=>actions=>runner=>new self hosted runner=> choose os=> then run command one by one on the EC2 created
	Note: if the runner is offline you might need to restart the whole process

# 7. Configure EC2 port 
    Go to EC2 ==> Security ==> security group ===> edit inbound ==> add custom TCP and specify the port 8080 - accept traffic from 0.0.0.0

# 8. Setup github secrets:

    AWS_ACCESS_KEY_ID= 

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-2

    AWS_ECR_LOGIN_URI = demo>>  927765266034.dkr.ecr.us-east-2.amazonaws.com/mlops

    ECR_REPOSITORY_NAME = simple-app


# 9. Push to git  
  

# docker help tools:
docker rm -f $(docker ps -a -q)
docker rmi $(docker images -q)

    
================================================================================================================================================     
     
         
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "test.py"
]


REFERENCE
==========
### MLOps --- MLFlow : https://www.youtube.com/watch?v=pxk1Fr33-L4
### Dashub           : https://www.youtube.com/watch?v=qdcHHrsXA48



Tech AI is a technology company that specializes in delivering advanced products and AI-powered open source and cloud solutions.