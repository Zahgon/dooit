from typing import Callable, Type
from dooit.ui.api.events import DooitEvent

DOOIT_EVENT_ATTR = "__dooit_event"
DOOIT_TIMER_ATTR = "__dooit_timer"


def subscribe(*events: Type[DooitEvent]):
    """
    Subscribe decorator for event handlers
    """
    pass


def timer(interval: float):
    """
    Timer decorator for event handlers
    """
    pass
