# OpenFaas on Docker Swarm Tutorial, article 2
This project contains source code of any functions described on the following link

[Functions development with OpenFaas](https://blog.ineat-conseil.fr/2019/03/serverless-sur-raspberry-pi-avec-docker-swarm-et-openfaas-partie-2-developpons-quelques-fonctions/)

## How build and deploy ineat-openfaas-calculator

> Enter you login/password with the following command :

```shell
cat ~/faas_pass.txt | faas-cli login -g http://CLUSTER_IP_ADDRESS:8080 -u admin --password-stdin
```

> To build function, go to root of ineat-openfaas-calculator and enter :

```shell
faas-cli build -f ineat-openfaas-calculator.yml
```

> To deploy :

```shell
faas-cli deploy -f ineat-openfaas-calculator.yml
```

## Import Mongo Data Base

> To follow the second part of the tutorial, you need a Mongo Data Base. This project contains a dump of my own data base. You can import with :

```shell
mongorestore -d moviesDB moviesDB_dump
```

## How build and deploy ineat-openfaas-get-movies and ineat-openfaas-post-movie

> Enter you login/password with the following command :

```shell
cat ~/faas_pass.txt | faas-cli login -g http://CLUSTER_IP_ADDRESS:8080 -u admin --password-stdin
```

> To build and deploy function ineat-openfaas-get-movies, go to the root of corresponding folder and enter :

```shell
faas-cli build -f ineat-openfaas-get-movies.yml && faas-cli deploy -f ineat-openfaas-get-movies.yml
```

> To build and deploy function ineat-openfaas-post-movie, go to the root of corresponding folder and enter :

```shell
faas-cli build -f ineat-openfaas-post-movie.yml && faas-cli deploy -f ineat-openfaas-post-movie.yml
```
