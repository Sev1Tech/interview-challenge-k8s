# Sev1Tech DevOps Code Challenge

## The Challenge

#### Part 1
The development teams on your project have been working on a set of microservices. They need help getting the docker containers build and running.

#### Part 2
In addition, the team would like to use Kubernetes to deploy these services in continuous integration and production environments. Because `Docker for Mac` and `Docker for Windows` provides Kubernetes out-of-the-box, the team would like to be able to test their services locally in Kubernetes before progressing to CI pipelines. Your goal is to prepare Kubernetes configuration in order to deploy the services in a local Kubernetes cluster.

![Ideal Scenario image](./ideal-scenario.png)

## Pre-Requisites
- `docker-for-mac` or `docker-for-windows`
	- Includes `docker`, `docker-compose`, `kubectl`, and `kubernetes`

## Provided Architecture
<pre>																			  
Web Browser Client -->  webapp --> person-service --> postgres
</pre>

## Service Details
- `postgres` - Postgres database used by the `person-service`
	- Base Docker hub image tag: `postgres:11`
	- Exposed port: `5432`
- `person-service` - A spring-boot/Java backend microservice that provides `persons` REST endpoints
	- Base Docker hub image tags: `gradle:5.4-jdk11` and `openjdk:11.0-jdk` (Use multi-stage Dockerfiles)
	- Exposed port: `8080`
- `webapp` - React SPA frontend that consumes the `person-service` and `counter-service`
	- Base Docker hub image tags: `node:12-alpine` and `nginx:1.14.2` (Use multi-stage Dockerfiles)
	- Exposed port: `8000` and/or `80`

## Requirements
- Use `docker` - `Dockerfiles`
- Use `docker-compose` stack(s) unless a suitable alternative is provided
- Use `kubernetes`
	- You may use `Docker for Mac` Kubernetes, `Docker for Windows` Kubernetes, or `minikube`
	- For deployment tools, you may use `vanilla Kubernetes yaml`, `Helm`, `Kustomize`, or any other tool/scripting that you are comfortable with.


## Steps
- build the docker images. Ensure they run
- standup a Kubernetes cluster: use K3d or Minikube
- deploy the solution to Kubernetes