from invoke import task

ENV = 'dev'
ENVS = ['prod', 'dev']
SERVICES = []

BASE_COMPOSE_CMD = "docker-compose -f docker-compose.yml"

NAME_ARG_HELP = 'Name of service - i.e. postgresql, redis, flaskapp.'
ENV_ARG_HELP = 'Name of environment to use - dev, test, perf. Defaults to dev.'
NOCACHE_ARG_HELP = 'Build with no docker layer caching.'

@task(help = {
    'name': NAME_ARG_HELP,
    'env': ENV_ARG_HELP
})
def dc_stop_service(c, name, env='dev'):
    """
    Docker-compose - Stop a compose service
    """
    print('STOPPING {0} WITH ENV: {1}'.format(name, env))
    cmd1 = "{0} -f docker-compose.{1}.yml stop {2}".format(BASE_COMPOSE_CMD, env, name)
    cmd2 = "{0} -f docker-compose.{1}.yml rm -f {2}".format(BASE_COMPOSE_CMD, env, name)
    c.run(cmd1)
    c.run(cmd2)

@task(help = {
    'name': NAME_ARG_HELP,
    'env': ENV_ARG_HELP,
    'nocache': NOCACHE_ARG_HELP
})
def dc_build_service(c, name, env='dev', nocache=False):
    """
    Docker-compose - Build a compose service
    """
    print('BUILDING {0} WITH ENV: {1}'.format(name, env))
    nocache_flag = ''
    if nocache:
        nocache_flag = "--no-cache"
    cmd1 = "{0} -f docker-compose.{1}.yml build {2} {3}".format(BASE_COMPOSE_CMD, env, nocache_flag, name)
    c.run(cmd1)

@task(help = {
    'name': NAME_ARG_HELP,
    'env': ENV_ARG_HELP
})
def dc_up_service(c, name, env='dev'):
    """
    Docker-compose - Deploy (up) and daemonize a compose service
    """
    print('UP {0} WITH ENV: {1}'.format(name, env))
    cmd1 = "{0} -f docker-compose.{1}.yml up -d {2}".format(BASE_COMPOSE_CMD, env, name)
    c.run(cmd1)

@task(help = {
    'name': NAME_ARG_HELP,
    'env': ENV_ARG_HELP
})
def dc_restart_service(c, name, env='dev'):
    """
    Docker-compose - Restart a compose service
    """
    print('RESTARTING {0} WITH ENV: {1}'.format(name, env))
    cmd1 = "{0} -f docker-compose.{1}.yml restart {2}".format(BASE_COMPOSE_CMD, env, name)
    c.run(cmd1)

@task(help = {
    'name': NAME_ARG_HELP,
    'env': ENV_ARG_HELP,
    'nocache': NOCACHE_ARG_HELP
})
def dc_rebuild_service(c, name, env='dev', nocache=False):
    """
    Docker-compose - Rebuild (stop, build, and deploy) a compose service
    """
    print('REBUILDING {0} WITH ENV: {1}'.format(name, env))
    dc_stop_service(c, name, env)
    dc_build_service(c, name, env, nocache)
    dc_up_service(c, name, env)

@task(help = {
    'env': ENV_ARG_HELP
})
def dc_up_env(c, env='dev'):
    """
    Docker-compose - Deploy (up) environment
    """
    dc_rebuild_service(c, 'postgres', env=env)
    dc_rebuild_service(c, 'redis', env=env)
    dc_rebuild_service(c, 'counter-service', env=env)
    dc_rebuild_service(c, 'person-service', env=env)
    dc_rebuild_service(c, 'webapp', env=env)
    dc_rebuild_service(c, 'nginx', env=env)

@task(help = {
    'name': NAME_ARG_HELP,
    'env': ENV_ARG_HELP
})
def dc_logs(c, name, env='dev'):
    """
    Docker-compose - Print service container logs for a given service and environment.
    """
    cmd1 = "{0} -f docker-compose.{1}.yml logs -f {2}".format(BASE_COMPOSE_CMD, env, name)
    c.run(cmd1)

@task(help = {
    'env': ENV_ARG_HELP
})
def dc_ps(c, env='dev'):
    """
    Docker-compose - View status of compose services in a given environment.
    """
    cmd1 = "{0} -f docker-compose.{1}.yml ps".format(BASE_COMPOSE_CMD, env)
    c.run(cmd1)

@task()
def dc_down_all(c, env='dev'):
    """
    Docker-compose - Destroy all compose services.
    """
    print('DESTROYING ALL SERVICES IN ENV')
    cmd1 = "{0} -f docker-compose.{1}.yml down -v".format(BASE_COMPOSE_CMD, env)
    c.run(cmd1)

@task(help = {
    'env': ENV_ARG_HELP
})
def dc_stop_all(c, env='dev'):
    """
    Docker-compose - Stop all services for a given environment
    """
    print('STOPPING ALL SERVICES IN ENV: {0}'.format(env))
    cmd1 = "{0} -f docker-compose.{1}.yml stop".format(BASE_COMPOSE_CMD, env)
    c.run(cmd1)

@task(help = {})
def create_global_volumes(c):
    """
    Create required global volumes
    """
    c.run("docker volume create --name=global_pypi_cache")
    c.run("docker volume create --name=global_npm_cache")
    c.run("docker volume create --name=global_gradle_cache")

@task(help = {})
def remove_global_volumes(c):
    """
    Create required global volumes
    """
    c.run("docker volume rm global_pypi_cache")
    c.run("docker volume rm global_npm_cache")
    c.run("docker volume rm global_gradle_cache")

@task(help = {})
def skaffold_run(c):
    """
    Create all services with Skaffold
    """
    c.run("skaffold -p redis run")
    c.run("skaffold -p counter run")
    c.run("skaffold -p postgres run")
    c.run("skaffold -p person run")
    c.run("skaffold -p webapp run")
    c.run("skaffold -p nginx run")

@task(help = {})
def skaffold_delete(c):
    """
    Delete all services with Skaffold
    """
    c.run("skaffold -p redis delete")
    c.run("skaffold -p counter delete")
    c.run("skaffold -p postgres delete")
    c.run("skaffold -p person delete")
    c.run("skaffold -p webapp delete")
    c.run("skaffold -p nginx delete")
