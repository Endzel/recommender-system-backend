FROM python:3.6

RUN mkdir -p /opt/recommender
WORKDIR /opt/recommender

RUN apt-get update
RUN apt-get install zlib1g-dev -y

ADD requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

RUN apt-get install mysql-server -y

ADD ./ /opt/recommender/

EXPOSE 8000
