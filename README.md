## Steps to run:

- Install required packages: `pip install -r requirements.txt`
- Run the following
  command: `python -m grpc_tools.protoc -I ./protobufs --python_out=./management_proto --grpc_python_out=./management_proto ./protobufs/model_management.proto`
    - `python -m grpc_tools.protoc`: this piece runs the protobuf compiler, which will generate python code from
      protobuf code.
    - `-I ./protobufs`: this piece tells the compiler where to find files that protobuf code imports.
    - `--python_out=./management_proto --grpc_python_out=./management_proto`: tells the compiler where to output the
      python files.
    - `./protobufs/model_management.proto`: is the path to protobuf file which will be used to generate python code.
- 