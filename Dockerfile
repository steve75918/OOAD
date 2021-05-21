FROM ubuntu

RUN apt-get update && apt-get install -y \
    python3 && \
    ln -s /usr/bin/python3.6 /usr/bin/python

WORKDIR /projects/ooad/