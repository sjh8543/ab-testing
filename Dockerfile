# Author : sjh8543@gmail.com
# This images is made for ab-testing web apllication server, which is based on ubuntu16.10 
FROM ubuntu:16.10

#install essential modules and dependency
RUN apt-get update && apt-get -y install \
    git \
    wget \
    vim \
    curl \
 && rm -rf /var/lib/apt/lists/*

#install python3.6
RUN apt-get update && apt-get -y install python3.6 && rm -rf /var/lib/apt/lists/*

#create working directory to manage applicaion
WORKDIR /home/runtime

#pip setting with get-pip.oy
RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3.6 get-pip.py
RUN rm get-pip.py

#install flask
RUN pip3 install flask

#deploy application
COPY flask_app flask_app
