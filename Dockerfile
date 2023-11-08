FROM py3.8

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN python -m pip install --upgrade pip
RUN cd app
RUN python -m pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ./protobufs --python_out=./management_proto \
    --grpc_python_out=./management_proto ./protobufs/model_management.proto

EXPOSE 50051
ENTRYPOINT [ "python", "server.py" ]