from abc import ABC
from enum import Enum


class LogLevel(Enum):
    ERROR = "ERROR"
    DEBUG = "DEBUG"
    NA = "NA"

class LogProcessor(ABC):
    def __init__(self, log_processor: 'LogProcessor'):
        self.next_log_processor = log_processor

    def log(self, logLevel, message):
        if self.next_log_processor is not None:
            self.next_log_processor.log(logLevel, message)
