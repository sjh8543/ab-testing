# Author : sjh8543@gmail.com
# This images is made to test ab-testing engine. It can be rebuild later with another structure. 
FROM flask-app:latest

#install coverage test module
RUN pip3 install coverage

#copy source file for testing into images 
COPY main_test.py flask_app/test/main_test.py

#add pythonpath for application source code import
ENV PYTHONPATH=/home/runtime/flask_app
#add env value for running test flask application. Every flask application have to have APP_NAME env value, so we need to mocki that environment
ENV APP_NAME=test_application

#running test
CMD python3.6 /home/runtime/flask_app/test/main_test.py
