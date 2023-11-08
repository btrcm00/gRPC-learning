from common.config import BaseService, SystemStatus
from services.data_manager import DataManager
from services.trainer import Trainer


class Processor(BaseService):
    def __init__(self, config):
        super(Processor, self).__init__()
        self.config = config
        self.data_manager = DataManager(config=self.config)
        self.trainer = Trainer(config=self.config)
        self._status: SystemStatus = SystemStatus.IDLE

    def start(self):
        self._status = SystemStatus.ACTIVE

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, _status):
        if _status not in SystemStatus:
            raise ValueError("status is not valid")
        self._status = _status

    def set_up(self):
        if self.status == SystemStatus.IDLE:
            self.status = SystemStatus.ACTIVE
        return self.status

    def train(self):
        self.status = SystemStatus.TRAINING
        self.trainer.train()
        self.status = SystemStatus.ACTIVE

    def create_dataset(self):
        pass

    def download_ckpt(self):
        pass

    def predict(self, image: str):
        return self.trainer.predict(image)

    def logging(self):
        pass