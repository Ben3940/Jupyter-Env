# Purpose of Repo

This repo is the local environment to run a **Jupyter Notebook** server, containerized using **Docker**. Docker will need to be downloaded on the host machine attempting to run this local environment. The Docker image will also be built from this repo as well.

# Installing Docker Desktop

As mentioned, Docker will need to be installed on any machine needing to run this environment. This is the offical _Docker Desktop_ download page from Docker.

https://www.docker.com/get-started/

Installing Docker Desktop will provide the GUI application for Docker, as well as, the CLI application for Docker. The following steps to build the image will use the CLI application of Docker.

# Building the Docker Image

1. Navigate to the directory containing the _Dockerfile_ (this should be the root directory of the repo). Execute the following command to build the image

```shell
    docker build . -t <image-name>
```

NOTE:

- `<image-name>` can be whatever name you want to reference the image by

2. Verify that Docker recognizes the built image

```shell
    docker images
```

You should see a list with info about the Docker image.

# Running a Docker Container

1. Run the container with a mounted volume. This mounted volume is the **src** directory within this repo.

```shell
   docker run -it -p 5000:8888 -v ./src:/home/jovyan/work <image-name>
```

NOTE:

- `-it` specifies to run the container in _interactive mode_ (i) and with a _psuedo-terminal_ (t)
- `-p 5000:8888` specifies the port the host (port 5000) will use to communicate with the docker container, which it expects to be port 8888
- `-v ./src:/home/jovyan/work` connects the host's _src_ directory with the working directory of the container, by default this is _/home/jovyan/work_

After running this command, Docker will display a bunch of text to the terminal. Look for a portion of text that looks something like this

```shell
    To access the server, open this file in a browser:
        file:///home/jovyan/.local/share/jupyter/runtime/jpserver-7-open.html
    Or copy and paste one of these URLs:
        http://038485dcbe6c:8888/lab?token=5a9716d1168d9d6e74f13a925e9c0b99a5b96e9b0e731d19
        http://127.0.0.1:8888/lab?token=5a9716d1168d9d6e74f13a925e9c0b99a5b96e9b0e731d19
```

You will need to copy the token (5a9716d11... token string in this case) to login to the Jupyter Notebook

# Connecting to the Jupyter Notebook

1. Using a browser's address bar, connect to the Jupyter Notebook on _localhost:5000_ or _127.0.0.1:5000_

2. Paste the login token from above and you should be connected to the container
