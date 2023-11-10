from concurrent import futures
import grpc
import base64

import management_proto.model_management_pb2 as manager_pb2
from management_proto import model_management_pb2_grpc
from common.config import Config, SystemStatus
from service.processor import Processor


class ManagementService(model_management_pb2_grpc.ManagementServicer):
    def __init__(self, config):
        self.config = config if config is not None else Config()
        self.processor = Processor(config=self.config)

    @property
    def _command_to_func(self):
        return {
            manager_pb2.CommandType.PREDICT: self.processor.predict,
            manager_pb2.CommandType.DOWNLOAD_CKPT: self.processor.get_ckpt,
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

    def _check_base64(self, data):
        _data = base64.b64decode(data)
        if base64.b64encode(_data) == data:
            return _data
        return data

    def Setup(self, request, context):
        status = self.processor.set_up(token=request.token)
        return manager_pb2.SetupResponse(status=self._sys_status_to_response[status])

    def Import(self, request, context):
        try:
            for i, image_data in enumerate(request.data):
                image_data = self._check_base64(image_data)
                self.processor.import_file(image_data)
        except Exception as e:
            return manager_pb2.ImportResponse(
                status=manager_pb2.Status.FAIL,
                message=f"Encounter error while importing data: {e}"
            )
        return manager_pb2.ImportResponse(status=manager_pb2.Status.SUCCESSFUL)

    def Commands(self, request, context):
        if request.command == manager_pb2.CommandType.DOWNLOAD_CKPT:
            ckpt_path = self.processor.get_ckpt()
            with open(ckpt_path, 'rb') as f:
                content = f.read()
            return manager_pb2.CommandResponse(file=content)

        elif request.command == manager_pb2.CommandType.PREDICT:
            import random
            idx  = str(random.randint(1000,9999))
            with open(f"image_{idx}.jpg", 'wb') as f:
                f.write(request.file)
            prediction = self.processor.predict(image=f"image_{idx}.jpg")
            return manager_pb2.CommandResponse(message=prediction)

        elif request.command == manager_pb2.CommandType.TRAIN:
            done = self.processor.train()

        elif request.command == manager_pb2.CommandType.STOP_TRAINING:
            done = self.processor.stop_training()

        else:
            raise ValueError("Command type not found!")

        if done:
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
    config = Config()
    serve(config=config)
