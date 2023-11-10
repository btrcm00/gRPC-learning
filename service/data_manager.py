from glob import glob

from common.config import BaseService


class DataManager(BaseService):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.saved_path = f"{self.config.data_path}/dataset/imported"

    def import_file(self, image_data):
        current_files = glob(f"{self.saved_path}/*.jpg")
        if not current_files:
            file_idx = 0
        else:
            current_files = [int(f.split("\\")[-1].replace(".jpg", "")) for f in current_files]
            current_files.sort()
            file_idx = current_files[-1] + 1
        with open(f"{self.saved_path}/{file_idx}.jpg", 'wb') as f:
            f.write(image_data)
