FROM python:3.8-bullseye AS dev
RUN apt-get -qq update && apt-get install -qq -y git curl bash zip

ENV DOCKER_VERSION=20.10.11
RUN curl -fsSLO https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz \
        && tar xzvf docker-${DOCKER_VERSION}.tgz --strip 1 \
        -C /usr/local/bin docker/docker \
        && rm docker-${DOCKER_VERSION}.tgz

COPY requirements-dev.txt ./
RUN pip3 install -r requirements-dev.txt
