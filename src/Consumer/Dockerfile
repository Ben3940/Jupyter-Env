# FROM jupyter/base-notebook:latest
# COPY ./src/requirements.txt /home/jovyan/work
# RUN python -m pip install --no-cache -r /home/jovyan/work/requirements.txt
FROM python:latest
WORKDIR /usr/src/app
COPY . .
RUN python -m pip install --no-cache -r ./requirements.txt
CMD ["python3", "Consumer.py"]