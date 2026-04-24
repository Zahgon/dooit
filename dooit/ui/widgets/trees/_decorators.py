from functools import partial
from typing import Any, Callable, TYPE_CHECKING
from textual.widgets.option_list import OptionDoesNotExist

from dooit.api.exceptions import NoNodeError
from dooit.ui.api.events import ShowConfirm

if TYPE_CHECKING:  # pragma: no cover
    from .model_tree import ModelTree


def fix_highlight(func: Callable) -> Callable:
    pass


def refresh_tree(func: Callable) -> Callable:
    pass


def require_highlighted_node(func: Callable) -> Callable:
    pass


def require_confirmation(func: Callable) -> Callable:
    pass
