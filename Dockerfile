# Author : sjh8543@gmail.com
# This images is made for ab-testing web apllication server, which is based on ubuntu16.10 
FROM ubuntu:16.10

#install essential modules and dependency
RUN apt-get update && apt-get -y install \
    git \
    python3.6 \
    wget \
    vim \
    curl \
 && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get -y install python3-pip

WORKDIR /home/
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3.6 get-pip.py
RUN pip3 install flask
#upgrde pip and then install flask
#RUN pip3 install --upgrade pip && pip3 install flask

#create directory to install and manage flask application
#RUN mkdir /home/runtime
#WORKDIR /home/runtime

#COPY flask_app flask_app
