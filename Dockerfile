# FROM python:3.7.2-stretch
FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y python3 python3-pip
RUN apt-get install -y build-essential libssl-dev libffi-dev python-de

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Run app when the container launches
CMD ["uwsgi","app.ini"]