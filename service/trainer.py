from glob import glob
from ultralytics import YOLO

from common.config import BaseService


class Trainer(BaseService):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.model = None

    def train(self):
        self.logger.info("START TRANING YOLOv8 ...")
        self.model = YOLO(model=f"{self.config.checkpoint_path}/base/yolov8n.pt", task="detect")
        self.model.train(
            data=f"{self.config.data_path}/data.yaml",
            epochs=3,
            save_dir=f"{self.config.checkpoint_path}/trained"
        )

    def eval(self, ckpt_path: str):
        self.model = YOLO(ckpt_path)
        metrics = self.model.eval()
        self.logger.info("METRICS of model", metrics)

    def predict(self, image: str):
        self.logger.info("Predicting an image ...")
        return self.model(image)

    def get_ckpt_path(self, mode: str = "best"):
        ckpt_path = self.config.checkpoint_path
        ckpt_files = glob(f"{ckpt_path}/trained/{mode}.pt")
        if not ckpt_files:
            return f"{self.config.checkpoint_path}/yolov8n.pt"
        else:
            return ckpt_files[-1]
