from ultralytics import YOLO

from common.config import BaseService


class Trainer(BaseService):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.model = YOLO(self.config.model_path)

    def train(self):
        self.logger.info("START TRANING YOLOv8 ...")
        self.model.train(data=f"{self.config.data_path}/data.yaml", epochs=3)

    def eval(self):
        metrics = self.model.eval()
        self.logger.info("METRICS of model", metrics)

    def predict(self, image: str):
        return self.model(image)

    def download_ckpt(self):
        pass
