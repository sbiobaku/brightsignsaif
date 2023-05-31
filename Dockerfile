FROM python:slim-buster

# update the image 
RUN apt clean && apt upgrade -y && apt update -y --fix-missing

RUN apt-get -y install curl net-tools

# create a working directory
WORKDIR /etc/workdir

COPY ./ ./

# pip install request library 
RUN pip3 install --no-cache-dir -r requirements.txt

# Set locale
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

ENTRYPOINT  python3 allDataFeedMac.py