FROM python:3.8-slim

WORKDIR /app
COPY . .

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install --upgrade pip
RUN pip3 install grpcio-tools==1.59.2
RUN pip3 install numpy==1.22.1
RUN pip3 install protobuf==3.20.3
RUN pip3 install ultralytics==8.0.207

EXPOSE 8080
ENTRYPOINT [ "python", "server.py" ]