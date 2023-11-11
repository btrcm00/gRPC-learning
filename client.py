import grpc
from management_proto.model_management_pb2_grpc import ManagementStub
import management_proto.model_management_pb2 as pb


class Client:
    def __init__(self, server_address: str):
        channel = grpc.insecure_channel(server_address)
        self.client = ManagementStub(channel=channel)
        
    def stop_training(self):
        request = pb.CommandRequest(command=pb.CommandType.STOP_TRAINING)
        return self.client.Commands(request)
    
    def setup(self):
        request = SetupRequest(token="1263")
        return client.Setup(request)
    
    def training(self):
        request = pb.CommandRequest(command=pb.CommandType.TRAIN)
        future_result = self.client.Commands.future(request)
        print("STARTING TRAINING ...")
        return future_result.result()
    
    def import_data(self):
        with open("test_images/img1.png", "rb") as f1:
            img1 = f1.read()

        with open("test_images/img2.jpg", "rb") as f1:
            img2 = f1.read()

        request = pb.ImportRequest(data=[img1, img2])
        return client.Import(request)
    
if __name__ == "__main__":
    client = Client(server_address="localhost:8888")
    