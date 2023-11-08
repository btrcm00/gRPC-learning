from concurrent import futures
import grpc

from management_proto.model_management_pb2 import (
    SetupResponse,
    CommandType
)
from management_proto import model_management_pb2_grpc
from common.config import Config
from services.processor import Processor


class ManagementService(model_management_pb2_grpc.ManagementServicer):
    def __init__(self, config):
        self.config = config if config is not None else Config()
        self.processor = Processor(config=self.config)

    @property
    def command_to_func(self):
        return {
            CommandType.PREDICT: self.processor.predict,
            CommandType.LOGGING: self.processor.logging,
            CommandType.DOWNLOAD_CKPT: self.processor.download_ckpt,
            CommandType.DATASET_CREATE: self.processor.create_dataset,
            CommandType.TRAIN: self.processor.train
        }

    def Setup(self, request, context):
        status = self.processor.set_up(token=request.token)
        return SetupResponse(status=status)

    def Import(self, request, context):
        files = request.files
        raise NotImplementedError('Method not implemented!')

    def Commands(self, request, context):
        if request.command not in self.command_to_func.keys():
            raise ValueError("Command type not found!")
        func = self.command_to_func[request.command]
        func()


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
