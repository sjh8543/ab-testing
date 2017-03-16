# Author : sjh8543@gmail.com
# This images is made to test ab-testing engine. It can be rebuild later with another structure. 
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
RUN wget https://bootstrap.pypa.io/get-pip.py && python3.6 get-pip.py && rm get-pip.py

#install flask
RUN pip3 install flask

#pull source from git repository
RUN git clone https://github.com/sjh8543/ab-testing.git
