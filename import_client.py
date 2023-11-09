import grpc
from management_proto.model_management_pb2_grpc import ManagementStub
from management_proto.model_management_pb2 import ImportRequest

channel = grpc.insecure_channel("localhost:5050")
client = ManagementStub(channel=channel)

with open("test_images/img1.png", "rb") as f1:
    img1 = f1.read()

with open("test_images/img2.jpg", "rb") as f1:
    img2 = f1.read()

request = ImportRequest(data=[img1, img2])
print(client.Import(request))
