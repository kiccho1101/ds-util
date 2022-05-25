import sys


class LoggerUtil:
    @staticmethod
    def get_logger(name: str):
        from loguru import logger

        logger.remove()
        custom_format = "<green>[{extra[name]} {time:YYYY-MM-DD HH:mm:ss}]</green> <level>{level} {message}</level>"
        logger.add(sys.stdout, colorize=True, format=custom_format)
        logger = logger.bind(name=name)
        return logger
