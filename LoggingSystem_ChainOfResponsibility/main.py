from LoggingSystem_ChainOfResponsibility.debug_log_processor import DebugLogProcessor
from LoggingSystem_ChainOfResponsibility.error_log_processor import ErrorLogProcessor
from LoggingSystem_ChainOfResponsibility.log_processor import LogLevel

if __name__ == "__main__":
    logger = ErrorLogProcessor(DebugLogProcessor(None))
    logger.log(LogLevel.NA, "Help!!!!")
    logger.log(LogLevel.DEBUG, "Help!!!!")
    logger.log(LogLevel.ERROR, "Help!!!!")
