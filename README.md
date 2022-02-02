# Docker Containerization


### Docker Containers:

- Environment Standardization
- Portability
- Isolation
- Build Once, Deploy everywhere


### Article for reference
  [Part 1](https://towardsdatascience.com/why-using-docker-for-machine-learning-74c927ceb6c4)
  - Docker allows to easily reproduce the working environment that is used to train and run the machine learning model anywhere.
  - Docker allows packaging the code and dependencies into containers that can be ported to different servers even if it’s a different hardware or operating system.
  - A training model can be developed on a local machine and be easily ported to external clusters with additional resources such as GPUs, more memory or powerful CPUs.
  
  

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
