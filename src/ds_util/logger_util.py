import sys
from pathlib import Path


class LoggerUtil:
    @staticmethod
    def get_logger(log_dir: Path, filename: str):
        from loguru import logger

        log_dir.mkdir(parents=True, exist_ok=True)
        log_file = log_dir / filename
        logger.remove()
        custom_format = "<green>[{time:YYYY-MM-DD HH:mm:ss}]</green> <level>{level} {message}</level>"
        logger.add(log_file, format=custom_format)
        logger.add(sys.stdout, colorize=True, format=custom_format)
        return logger
