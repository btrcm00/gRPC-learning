import grpc
from management_proto.model_management_pb2_grpc import ManagementStub
import management_proto.model_management_pb2 as pb


channel = grpc.insecure_channel("localhost:5050")
client = ManagementStub(channel=channel)

request = pb.CommandRequest(command=pb.CommandType.STOP_TRAINING)
print(client.Commands(request))