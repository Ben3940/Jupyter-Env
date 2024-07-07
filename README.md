# Purpose of Repo

This repo is the local environment to run a **Jupyter Notebook** server, containerized using **Docker**. Docker will need to be downloaded on the host machine attempting to run this local environment. The Docker image will also be built from this repo as well.

# Installing Docker Desktop

As mentioned, Docker will need to be installed on any machine needing to run this environment. This is the offical _Docker Desktop_ download page from Docker.

https://www.docker.com/get-started/

Installing Docker Desktop will provide the GUI application for Docker, as well as, the CLI application for Docker. The following steps to build the image will use the CLI application of Docker.

# Composing Docker Containers

1. Navigate to the directory containing the _compose.yaml_ file(this should be in the root directory of this repo). Execute the following command to build the image

```shell
    docker compose up
```

NOTE:

- This will setup the Docker containers based on the configurations set in _compose.yaml_

2. Verify that containers are running

```shell
    docker ps
```

# Starting/Stopping Containers

### Stopping

1. To stop all running containers, simply type:

```shell
   docker compose stop
```

### Starting

1. To start the containers again:

```shell
    docker compose start
```

NOTE:

- _up/down_ commands creates/removes (respectively) the containers associated with the _compose.yaml_ file. _start/stop_ should be used unless you update the _compose.yaml_ file and need to re-create the containers.

# Connecting to the Jupyter Notebook

1. Using a web browser, connect to the Jupyter Notebook on _localhost:5000_ or _127.0.0.1:5000_

2. Enter the same password specified in the _jupyter_ container's config, specifically the _JUPYTER-TOKEN_ under _environment_ property
