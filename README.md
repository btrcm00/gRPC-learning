# gRPC API for manage ML system

- This source is to practice gRPC to interact with ML system.
- We can use gRPC API to trigger training process, import data, checking system status, ...
- Try training process with YOLOv8

## Demo:

- [Demo](demo/demo_gRPC_docker.mp4)

## Development steps:

- Install required packages: `pip install -r requirements.txt`
- Run the following
  command: `python -m grpc_tools.protoc -I ./protobufs --python_out=./management_proto --grpc_python_out=./management_proto ./protobufs/model_management.proto`
    - `python -m grpc_tools.protoc`: this piece runs the protobuf compiler, which will generate python code from
      protobuf code.
    - `-I ./protobufs`: this piece tells the compiler where to find files that protobuf code imports.
    - `--python_out=./management_proto --grpc_python_out=./management_proto`: tells the compiler where to output the
      python files.
    - `./protobufs/model_management.proto`: is the path to protobuf file which will be used to generate python code.
- Then we have two files in folder management_proto, it has Interfaces for use to implement Client and Server.
- Download the YOLOv8 checkpoint, locate it at `services/models/ckpt/base` folder
    - Checkpoint: [yolov8n.pt](https://github.com/ultralytics/ultralytics#:~:text=FLOPs%0A(B)-,YOLOv8n,8.7,-YOLOv8s)
- Download the dataset at [Dataset](https://github.com/entbappy/YOLO-v8-Object-Detection/blob/main/data.zip), then
  locate it in `services/data/dataset`

## Steps to test the system:

- Run docker compose: `docker-compose up`
- Use pre-defined client scripts to try call to server.
    - Import image file to system: `python import_client.py`
    - Setup: `python setup_client.py`
    - Stop training process of system: `python stop_client.py`
    - Send request to trigger the system to start training YOLOv8: `python training_client.py`