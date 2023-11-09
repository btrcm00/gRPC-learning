FROM python:3.8

WORKDIR /app
COPY . /app

RUN pip3 install --upgrade pip
RUN pip3 install grpcio-tools
RUN pip3 install numpy==1.22.1
RUN pip3 install protobuf==3.20.*
RUN pip3 install ultralytics
RUN grpc_tools.protoc -I ./protobufs --python_out=./management_proto \
    --grpc_python_out=./management_proto ./protobufs/model_management.proto

EXPOSE 50051
ENTRYPOINT [ "python", "server.py" ]