FROM python:3.7-slim-buster

WORKDIR /usr/src/app 
COPY . ./

RUN apt-get update && \
    apt-get install -y -q python3-dev \
    gcc \
    build-essential \
    bash

RUN pip install -r requirements.txt

CMD [ "python", "predict.py"]
