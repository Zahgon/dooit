import re
from datetime import datetime, timedelta
from typing import Any, Optional, Tuple

from .simple_input import SimpleInput
from dooit.api import Todo, Workspace
from dooit.utils import parse


class TodoDescription(SimpleInput[Todo, str]):
    @property
    def _property(self) -> str:
        pass


class WorkspaceDescription(SimpleInput[Workspace, str]):
    @property
    def _property(self) -> str:
        pass


class Due(SimpleInput[Todo, datetime]):
    def _get_default_value(self) -> str:
        pass

    def _typecast_value(self, value: str) -> Any:
        pass


class Urgency(SimpleInput[Todo, int]):
    @property
    def value(self) -> str:
        pass

    def _typecast_value(self, value: str) -> Any:
        pass


class Effort(SimpleInput[Todo, int]):
    def _typecast_value(self, value: str) -> Any:
        pass


class Status(SimpleInput[Todo, str]):
    def _get_default_value(self) -> str:
        pass

    def _typecast_value(self, value: str) -> Any:
        pass


class Recurrence(SimpleInput[Todo, timedelta]):
    @staticmethod
    def parse_recurrence(recurrence: str) -> timedelta:
        pass

    def _typecast_value(self, value: str) -> Optional[timedelta]:
        pass

    @staticmethod
    def timedelta_to_simple_string(td: timedelta):
        pass

    def _get_default_value(self) -> str:
        pass
