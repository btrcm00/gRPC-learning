from concurrent import futures
import grpc

from management_proto.model_management_pb2 import (
    SetupResponse,
    ImportStatus,
    CommandType
)
from management_proto import model_management_pb2_grpc
from services.common.config import Config
from services.setup import set_up
from services.data_manager import DataManager
from services.trainer import Trainer


class ManagementService(model_management_pb2_grpc.ManagementServicer):
    def __init__(self, config):
        self.config = config if config is not None else Config()
        self.data_manager = DataManager(config=self.config)
        self.trainer = Trainer(config=self.config)

    def Setup(self, request, context):
        status = set_up(token=request.token)
        return SetupResponse(status=status)

    def Import(self, request, context):
        files = request.files
        raise NotImplementedError('Method not implemented!')

    def Commands(self, request, context):
        if request.command not in CommandType:
            raise ValueError("Command type not found!")

        raise NotImplementedError('Method not implemented!')


def serve(api_port: str):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    model_management_pb2_grpc.add_ManagementServicer_to_server(
        ManagementService(), server
    )
    server.add_insecure_port(f"[::]:{api_port}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve(api_por="5051")
