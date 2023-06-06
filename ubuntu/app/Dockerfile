FROM ubuntu:latest
RUN apt-get update -y 
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip install numpy
RUN pip install pymongo
WORKDIR /usr/app/src
COPY . /app.py ./
CMD ["python3", "app.py"]