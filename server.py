from concurrent import futures
import grpc

import management_proto.model_management_pb2 as manager_pb2
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
            manager_pb2.CommandType.PREDICT: self.processor.predict,
            manager_pb2.CommandType.DOWNLOAD_CKPT: self.processor.download_ckpt,
            manager_pb2.CommandType.TRAIN: self.processor.train,
            manager_pb2.CommandType.STOP_TRAINING: self.processor.stop_training
        }

    @property
    def _sys_status_to_response(self):
        return {
            SystemStatus.IDLE: manager_pb2.ServiceStatus.IDLE,
            SystemStatus.TRAINING: manager_pb2.ServiceStatus.TRAINING,
            SystemStatus.ACTIVE: manager_pb2.ServiceStatus.ACTIVE
        }

    def Setup(self, request, context):
        status = self.processor.set_up(token=request.token)
        return manager_pb2.SetupResponse(status=self._sys_status_to_response[status])

    def Import(self, request, context):
        files = request.files
        status = self.processor.import_files(files)
        return manager_pb2.ImportResponse(status=status)

    def Commands(self, request, context):
        if request.command not in self._command_to_func.keys():
            raise ValueError("Command type not found!")
        func = self._command_to_func[request.command]
        output = func()
        if output:
            status = manager_pb2.Status.SUCCESSFUL
        else:
            status = manager_pb2.Status.FAIL
        return manager_pb2.CommandResponse(status=status)


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
