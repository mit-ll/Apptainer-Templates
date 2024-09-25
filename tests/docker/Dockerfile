FROM ubuntu:jammy-20231004

# Adding apt configuration file from host for installation.
# The /etc/apt/apt.confg file must be copied to the same location as the Dockerfile path.
# Ref: https://wiki.debian.org/AptConfiguration
COPY apt.conf /etc/apt/apt.conf

# Install basic packages needed for development
RUN apt-get update \
    && apt upgrade -y

RUN apt-get install -y --no-install-recommends \
    curl\
    g++ \
    gcc \
    git \
    vim \
    wget \
    && rm -rf /var/lib/apt/lists/*

RUN rm /etc/apt/apt.conf
