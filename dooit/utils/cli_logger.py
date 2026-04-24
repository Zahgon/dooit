from enum import Enum
from rich.style import Style
from rich.text import Text
from rich.console import Console


class LogLevel(Enum):
    INFO = "INFO"
    WARN = "WARN"
    ERROR = "ERROR"
    SUCCESS = "SUCCESS"


class CliLogger:
    def __init__(self) -> None:
        self.console = Console()
        self.print = self.console.print

    def _log(self, level: LogLevel, *messages: str) -> None:
        pass

    def info(self, *messages: str) -> None:
        pass

    def warn(self, *messages: str) -> None:
        pass

    def error(self, *messages: str) -> None:
        pass

    def success(self, *messages: str) -> None:
        pass


logger = CliLogger()
