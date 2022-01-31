# Docker Containerization


Docker Containers:

- Environment Standardization
- Portability
- Isolation
- Build Once, Deploy everywhere


Creating a simple application with Flask, Postman and Docker

1. Imported bank data 
2. Created a simple classification model
3. Created a Flask application
4. 



To create a new container from image

docker run


To start an existing container docket start


For list of containers started and stopped
doscker ps -a

look at logs
docker logs (id of container) [use docker ps to get id and/or name]

Create a container with custom name
docker run -d -p6001:6379 --name redis-older   redis:4.0

In the above specify a host machine port (6001) and the port typically taken by redis 6379 The bive is creating a redis 4.0 version container

Get Docker bash inside the container

docker exec -it "dockerid"  /bin/bash

To exit out of the container
exit


Create a docker network

docker network create mongo-network



View available docker network

docker network ls


USE a docker-compose.yaml file

docker run -d\
--name   mongodb\
-p 27017:27107\
-e MONGO-INITDB_ROOT_USERNAME
=admin\
-e MONGO-INITDB_ROOT_PASSWORD
=password\

--net mongo-network\
mongo


Start a docker from yaml file

docker-compose -f momgo.yaml


The network is created automatically by docker-compose


https://aws.amazon.com/blogs/opensource/why-use-docker-containers-for-machine-learning-development/
