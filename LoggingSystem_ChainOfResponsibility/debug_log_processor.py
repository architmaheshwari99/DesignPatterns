from LoggingSystem_ChainOfResponsibility.log_processor import LogProcessor, LogLevel


class DebugLogProcessor(LogProcessor):
    def __init__(self, log_processor: LogProcessor):
        super().__init__(log_processor)

    def log(self, logLevel, message):
        if logLevel == LogLevel.DEBUG.value:
            print("Debugging: ", message)
        else:
            super().log(logLevel, message)