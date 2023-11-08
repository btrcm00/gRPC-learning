import os
from enum import Enum
import logging

from common.common_keys import *


def setup_logging(logging_folder: str):
    os.makedirs(logging_folder, exist_ok=True)


class BaseService:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)


class Config:
    def __init__(
            self,
            model_path: str = None,
            logging_path: str = None,
            data_path: str = None,
            checkpoint_path: str = None,
            api_port: str = None,
            max_workers: int = None
    ):
        self.model_path = model_path if model_path is not None else os.getenv(MODEL_PATH)
        self.logging_path = logging_path if logging_path is not None else os.getenv(LOGGING_PATH)
        self.data_path = data_path if data_path is not None else os.getenv(DATA_PATH)
        self.checkpoint_path = checkpoint_path if checkpoint_path is not None else os.getenv(CHECKPOINT_PATH)
        self.api_port = api_port if api_port is not None else os.getenv(API_PORT)
        self.max_workers = max_workers if max_workers is not None else 10

class SystemStatus(Enum):
    IDLE = 0
    TRAINING = 1
    ACTIVE = 2
