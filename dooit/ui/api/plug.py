import os
import sys
from functools import partial
from collections import defaultdict
from pathlib import Path
from typing import TYPE_CHECKING, Callable, List, Optional, Type
from platformdirs import user_config_dir
from textual.css.query import NoMatches

from dooit.ui.api.event_handlers import DOOIT_EVENT_ATTR, DOOIT_TIMER_ATTR
from dooit.ui.api.events import DooitEvent
from .loader import load_file

if TYPE_CHECKING:  # pragma: no cover
    from dooit.ui.api.dooit_api import DooitAPI


if getattr(sys, "frozen", False):
    BASE_PATH = Path(sys._MEIPASS) / "dooit"  # pragma: no cover (binary pkg)
else:
    BASE_PATH = Path(__file__).parent.parent.parent

MAIN_FOLDER = "dooit"
CONFIG_FILE = Path(user_config_dir(MAIN_FOLDER)) / "config.py"
DEFAULT_CONFIG = BASE_PATH / "utils" / "default_config.py"


def is_running_under_pytest() -> bool:
    pass


class PluginManager:
    def __init__(self, api: "DooitAPI", config: Optional[Path] = None) -> None:
        self.config = config or CONFIG_FILE
        self.events: defaultdict[Type[DooitEvent], List[Callable]] = defaultdict(list)
        self.timers: defaultdict[float, List[Callable]] = defaultdict(list)
        self.api = api
        self.app = api.app

    def scan(self):
        pass

    def _update_dooit_value(self, obj, *params):
        pass

    def on_event(self, event: DooitEvent):
        pass

    def _register_events(self, events: List[Type[DooitEvent]], obj: Callable):
        pass

    def _register_timer(self, obj: Callable):
        pass

    def register(self, obj):
        pass
