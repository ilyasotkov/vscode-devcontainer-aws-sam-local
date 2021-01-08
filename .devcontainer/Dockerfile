FROM python:3.8-slim-buster AS dev
RUN apt-get -qq update && apt-get install -qq -y git curl bash zip

ENV DOCKER_VERSION=19.03.9
RUN curl -fsSLO https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKER_VERSION}.tgz \
        && tar xzvf docker-${DOCKER_VERSION}.tgz --strip 1 \
        -C /usr/local/bin docker/docker \
        && rm docker-${DOCKER_VERSION}.tgz

COPY requirements-dev.txt ./
RUN pip3 install -r requirements-dev.txt

# Patch for https://github.com/aws/aws-sam-cli/issues/2492
RUN find /usr/local/lib/python3.8/site-packages/samcli/local/docker/container.py \
        -type f -exec sed -i 's/localhost/host\.docker\.internal/g' {} \;
