# Author : sjh8543@gmail.com
# This images is made for ab-testing web apllication server, which is based on ubuntu16.10 
FROM ubuntu:16.10

#install essential modules and dependency
RUN apt-get update && apt-get -y install \
    git \
    wget \
    vim \
    curl \
    python3.6 \
 && rm -rf /var/lib/apt/lists/*

#create working directory to manage applicaion
WORKDIR /home/runtime

#pip setting with get-pip.oy then install flask using pip3
RUN wget https://bootstrap.pypa.io/get-pip.py && python3.6 get-pip.py && rm get-pip.py && pip3 install flask

#deploy application
RUN mkdir flask_app
COPY main.py flask_app/main.py

ENV FLASK_APP flask_app/main.py && LC_ALL=C.UTF-8 && LANG=C.UTF-8

CMD [ "flask" , "run" , "--host=0.0.0.0" ]
