from concurrent import futures
import grpc

from management_proto.model_management_pb2 import (
    SetupResponse,
    CommandType,
    ServiceStatus,
    ImportResponse
)
from management_proto import model_management_pb2_grpc
from common.config import Config, SystemStatus
from services.processor import Processor


class ManagementService(model_management_pb2_grpc.ManagementServicer):
    def __init__(self, config):
        self.config = config if config is not None else Config()
        self.processor = Processor(config=self.config)

    @property
    def _command_to_func(self):
        return {
            CommandType.PREDICT: self.processor.predict,
            CommandType.LOGGING: self.processor.logging,
            CommandType.DOWNLOAD_CKPT: self.processor.download_ckpt,
            CommandType.DATASET_CREATE: self.processor.create_dataset,
            CommandType.TRAIN: self.processor.train
        }
    
    @property
    def _sys_status_to_response(self):
        return {
            SystemStatus.IDLE: ServiceStatus.IDLE,
            SystemStatus.TRAINING: ServiceStatus.TRAINING,
            SystemStatus.ACTIVE: ServiceStatus.ACTIVE,
        }

    def Setup(self, request, context):
        status = self.processor.set_up(token=request.token)
        return SetupResponse(status=self._sys_status_to_response[status])

    def Import(self, request, context):
        files = request.files
        status = self.processor.import_files(files)
        return ImportResponse(status=status)

    def Commands(self, request, context):
        if request.command not in self._command_to_func.keys():
            raise ValueError("Command type not found!")
        func = self._command_to_func[request.command]
        func()


def serve(config: Config):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=config.max_workers))
    model_management_pb2_grpc.add_ManagementServicer_to_server(
        ManagementService(config=config), server
    )
    server.add_insecure_port(f"[::]:{config.api_port}")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    config = Config(api_port="5050")
    serve(config=config)
