FROM jupyter/base-notebook:latest
COPY ./src /home/jovyan/work
RUN python -m pip install --no-cache -r /home/jovyan/work/requirements.txt
