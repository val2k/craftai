Dockerized Asynchronous REST API w/ Traefik, Flask, Celery (Redis)
===================================================== 

Usage
====
* `docker-compose build`
* `docker-compose up`
* `curl -H Host:host.example.com http://localhost:80/factors/24`

URLs
====
*	API Endpoint: http://localhost:80/factors/<int>
*	Traefik dashboard: http://localhost:8080
*       Monitoring Task queue: http://localhost:5555

Requirements
====
* docker
* docker-compose

Tested with:

 
