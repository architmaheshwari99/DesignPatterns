from LoggingSystem_ChainOfResponsibility.log_processor import LogProcessor, LogLevel


class ErrorLogProcessor(LogProcessor):
    def __init__(self, log_processor: LogProcessor):
        super().__init__(log_processor)

    def log(self, logLevel, message):
        if logLevel == LogLevel.ERROR.value:
            print("Error: ", message)
        else:
            self.next_log_processor.log(logLevel, message)