import grpc
from management_proto.model_management_pb2_grpc import ManagementStub
from management_proto import model_management_pb2 as pb


channel = grpc.insecure_channel("localhost:5050")
client = ManagementStub(channel=channel)

request = pb.CommandRequest(command=pb.CommandType.TRAIN)
future_result = client.Commands.future(request)
print("STARTING TRAINING ...")
print(future_result.result())