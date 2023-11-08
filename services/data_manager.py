import base64
import random

from common.config import BaseService

class DataManager(BaseService):
    def __init__(self, config):
        super().__init__()
        self.config = config
        
    def _data_is_base64(self, data:str):
        _data = base64.b64decode(data)
        if base64.b64encode(_data) == data:
            return _data
        return None
    
    async def import_file(self, data: str):
        image_data = self._data_is_base64(data)
        if image_data is None:
            pass
        else:
            file_idx = str(random.randint(100000,999999))
            with open(f"{self.config.data_path}/dataset/imported/image_{filename}", 'wb') as f:
                f.write(image_data)
        
    async def import_dataset(self, files: list):
        try:
            for f in files:
                await self.import_file(f)
        except Exception as e:
            self.logger.error(f"File import process encounter the error {e}")
            return False
        
        return True
