# Docker Containerization


### Docker Containers:

- Environment Standardization
- Portability
- Isolation
- Build Once, Deploy everywhere


### Article(s) for reference
  [From AnalyticsVidhya](https://www.analyticsvidhya.com/blog/2021/06/a-hands-on-guide-to-containerized-your-machine-learning-workflow-with-docker/)


  [Part 1](https://towardsdatascience.com/why-using-docker-for-machine-learning-74c927ceb6c4)
  
  
  #### CONTAINERIZATION
  ![VMANDDOCKER](https://github.com/sjtalkar/DockerContainerization/blob/main/VMSANDDOCKER.png)
  
   - Each VM will need an OS, libraries and binaries, and consume more hardware resources such as processor, memory and disk space even if the micro-service is not really running. 
   - WHERE AS If a Docker container is not running, the remaining resources become shared resources and accessible to other containers. You do not need to add an OS in a container. 
  
  #### TRANSPORTABILITY
  - Docker allows to easily reproduce the working environment that is used to train and run the machine learning model anywhere.
  - Docker allows packaging the code and dependencies into containers that can be ported to different servers even if it’s a different hardware or operating system.
  - A training model can be developed on a local machine and be easily ported to external clusters with additional resources such as GPUs, more memory or powerful CPUs.
  
  
  [Part 2](https://xaviervasques.medium.com/quick-install-and-first-use-of-docker-327e88ef88c7) : 
  ####  TERMINOLOGY
  -  Dockerfile :  It’s a list of commands that Docker Engine will run. To create a Dockerfile, just open a file named Dockerfile in your working environment. 
  -  Docker Images:Docker images contain all the tools, libraries, dependencies, executable application source code necessary to run the application as a container. 
      -  We can build the Docker image from common repositories or from scratch using a Dockerfile which is a text file containing instructions on how to build Docker container image. 
  -  Docker Hub: Docker Hub is the public repository of Docker images.
  -  Docker Containers : Docker containers are running instances of Docker images.
  
  [Part 3](https://towardsdatascience.com/build-and-run-a-docker-container-for-your-machine-learning-model-60209c2d7a7f)
  ![commands](https://github.com/sjtalkar/DockerContainerization/blob/main/dockerfilecommands.png)


Creating a simple application with Flask, Postman and Docker

1. Imported bank data 
2. Created a simple classification model
3. Stored the model in a pickle (.pkl file)
4. Created a Flask application
5. Created routes for Welcome page, Prediction using GET request, Prediction using POST request
6. Captured parameters from the URL using request.args.get (variance=2&cskewness=8...)
7. Captured parameters from a file using request.files.get("filename")
8. Used Postman to run API using file input. Note that in the POST method you can specify a file for the input.
9. ![Using postman for flask API](https://github.com/sjtalkar/DockerContainerization/blob/main/UsePostmantosendTestFile.png)
10. Use https://github.com/flasgger/flasgger



### You can start with
https://hub.docker.com/r/continuumio/anaconda3


#### docker build -t bank_api .
#### docker run -p 8000:8000 bank_api

### Initial set of commands

- FROM   
- COPY    (host system file directory)
- EXPOSE  (port)
- WORKDIR (file directory)
- RUN      (pip install -r requirements.txt)
- CMD


#### Creating requirements.txt
pip install pipreqs

pipreqs  --print  --encoding=utf-8 ..\<name of folder containing project>


#### To create a new container from image

docker run


#### To start an existing container docket start


#### For list of containers started and stopped
doscker ps -a

#### look at logs
docker logs (id of container) [use docker ps to get id and/or name]

#### Create a container with custom name
docker run -d -p6001:6379 --name redis-older   redis:4.0

In the above specify a host machine port (6001) and the port typically taken by redis 6379 The bive is creating a redis 4.0 version container

#### Get Docker bash inside the container

docker exec -it "dockerid"  /bin/bash

#### To exit out of the container
exit


#### Create a docker network

docker network create mongo-network



#### View available docker network

docker network ls


#### USE a docker-compose.yaml file

docker run -d\
--name   mongodb\
-p 27017:27107\
-e MONGO-INITDB_ROOT_USERNAME
=admin\
-e MONGO-INITDB_ROOT_PASSWORD
=password\

--net mongo-network\
mongo


#### Start a docker from yaml file

docker-compose -f momgo.yaml


#### The network is created automatically by docker-compose


https://aws.amazon.com/blogs/opensource/why-use-docker-containers-for-machine-learning-development/
