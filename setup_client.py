import grpc
from management_proto.model_management_pb2_grpc import ManagementStub
from management_proto.model_management_pb2 import SetupRequest


channel = grpc.insecure_channel("localhost:8888")
client = ManagementStub(channel=channel)

request = SetupRequest(token="1263")
print(client.Setup(request))