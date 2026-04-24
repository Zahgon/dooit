from enum import Enum
from dataclasses import dataclass
from collections import defaultdict
from typing import Callable, List, Optional, Tuple, Union

from ._base import ApiComponent
from dooit.ui.api.events import ModeType

KeyBindType = defaultdict[str, defaultdict[str, Optional["DooitFunction"]]]
KeyType = Union[str, List[str]]


@dataclass
class DooitFunction:
    callback: Callable
    description: str = ""
    group: str = ""

    def __post_init__(self):
        self.description = self.description.strip("\n")


class KeyMatchType(Enum):
    NoMatchFound = "NoMatchFound"
    MultipleMatchFound = "MultipleMatchFound"
    MatchFound = "MatchFound"


@dataclass
class KeyMatch:
    match_type: KeyMatchType
    function: Optional[DooitFunction] = None

    @staticmethod
    def no_match():
        pass

    @staticmethod
    def multiple_match():
        pass

    @staticmethod
    def match_found(func: DooitFunction):
        pass


class KeyManager(ApiComponent):
    def __init__(self, get_mode: Callable) -> None:
        self.keybinds: KeyBindType = defaultdict(lambda: defaultdict(lambda: None))
        self._inputs: List[str] = []
        self.get_mode = get_mode

    @property
    def groups(self) -> List[str]:
        pass

    def get_keybinds_by_group(self, group: str) -> List[Tuple[str, DooitFunction]]:
        pass

    def __set_key(
        self,
        mode: ModeType,
        key: str,
        callback: Callable,
        description: Optional[str],
        group: str,
    ) -> None:
        pass

    def set(
        self,
        keys: KeyType,
        callback: Callable,
        description: Optional[str] = None,
        group: str = "",
    ) -> None:
        pass

    @property
    def input(self) -> str:
        pass

    def clear_input(self):
        pass

    def _find_matched_functions(self) -> List[DooitFunction]:
        pass

    def search_for_key(self) -> KeyMatch:
        pass

    def register_key(self, key: str) -> KeyMatch:
        pass
