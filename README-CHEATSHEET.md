# Sev1Tech DevOps Code Challenge Cheatsheet

## Pre-Requisites
- `docker-for-mac` or `docker-for-windows`
	- Includes `docker`, `docker-compose`, `kubectl`, and `kubernetes`
- `invoke` - `pip install invoke`

## Challenge - Part 1
1. `invoke create-global-volumes` - Create global docker volumes for dependency caching
1. `invoke dc-up-env` - Deploy all services
1. `invoke dc-ps` - View the stack in docker-compose
1. App available at `http://localhost:8000`
1. `invoke dc-down-all` - Tear down entire docker compose stack
1. `invoke remove-global-volumes` - Remove global docker volumes

## Challenge - Part 2
1. Activate Kubernetes in `Docker for Mac` (Docker Preferences > Kubernetes > Enable Kubernetes)
1. `brew install skaffold kustomize`
1. `kubectl cluster-info` - Make sure your local cluster is working
1. `invoke skaffold-run` - Build and deploy all services
1. `kubectl get pods` - View all pods
1. App available at `http://localhost:30500`
1. `invoke skaffold-delete` - Tear down the entire stack

## Criteria
- Scalability
- Security
- Best Practices

### Other Invoke examples
Most tasks have optional flags to set the `environment`, `nocache`, etc.

- `inv --list` - View available tasks
- `inv -h dc-rebuild-service` - View help for `dc-rebuild-service` task
- `inv dc-ps -e test` - View all services in `test` env
- `inv dc-ps` - View all services in `dev` env
- `inv dc-rebuild-service [service_name]` - Rebuild service
- `inv dc-restart-service [service_name]` - Restart service
- `inv dc-stop-service [service_name]` - Stop and remove service
- `inv dc-stop-all` - Stop all services for given environment
