FROM python:3.7-alpine
LABEL maintainer="pgooligo@synamedia.com"
RUN mkdir -p /usr/src &&\
    mkdir -p /usr/src/database
WORKDIR /usr/src

RUN apk add build-base libressl-dev libffi-dev python3-dev

#install the dependencies
COPY requirements.txt /usr/src
RUN pip install -r requirements.txt

#Path where DB will be created
ENV SQLALCHEMY_DATABASE_URI="/usr/src/database"
#ENV FLASK_APP=/usr/src/app
EXPOSE 5000

#Copy source code
COPY app /usr/src/app
COPY start_app.py /usr/src

#From docker run cmd mount a volume to /usr/src/database, required for persisting DB data
CMD ["python", "start_app.py"]

#Run command
#docker container run -idt -p 5000:5000 --rm -v sql-data:/usr/src/database pgooligo/app:v1

#Pre-requisite, create volume sql-data. This is required so that the data in DB persists container reboots
#docker volume create sql-data

