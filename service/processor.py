import multiprocessing

from common.config import BaseService, SystemStatus
from service.data_manager import DataManager
from service.trainer import Trainer


class Processor(BaseService):
    def __init__(self, config):
        super(Processor, self).__init__()
        self.config = config
        self.data_manager = DataManager(config=self.config)
        self.trainer = Trainer(config=self.config)
        self.training_process = None
        self._status: SystemStatus = SystemStatus.IDLE
        self._create_training_process()

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, _status):
        if _status not in SystemStatus:
            raise ValueError("status is not valid")
        self._status = _status

    def set_up(self, token: str):
        if self.status == SystemStatus.IDLE:
            self.status = SystemStatus.ACTIVE
        return self.status

    def _create_training_process(self):
        self.training_process = multiprocessing.Process(target=self._train, args=(), daemon=True)

    def _train(self):
        self.trainer.train()
        self.status = SystemStatus.ACTIVE

    def train(self):
        self.logger.info("System triggered to training YOLOv8 ...")
        self.status = SystemStatus.TRAINING
        try:
            self.training_process.start()
        except Exception as e:
            self.logger.error(f"Encounter the error when triggering training process: {e}")
            self.status = SystemStatus.ACTIVE
            return False
        return True

    def stop_training(self):
        if self.status == SystemStatus.TRAINING:
            self.logger.info("STOPPING the training process ...")
            self.training_process.terminate()
            self._create_training_process()
            self.status = SystemStatus.ACTIVE
            return True
        return False

    def import_file(self, image_data):
        self.data_manager.import_file(image_data=image_data)

    def get_ckpt(self):
        return self.trainer.get_ckpt_path(mode="best")

    def predict(self, image: str):
        return self.trainer.predict(image)
