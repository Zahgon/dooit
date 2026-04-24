from typing import TYPE_CHECKING, Callable
from textual.widgets import Static


from ...api.events import ModeChanged

if TYPE_CHECKING:  # pragma: no cover
    from .bar_switcher import BarSwitcher
    from dooit.ui.tui import Dooit
    from dooit.ui.api.dooit_api import DooitAPI


class BarBase(Static):
    DEFAULT_CSS = """
    BarBase {
        height: 1;
        width: 100%;
    }
    """

    focused: bool = True

    def __init__(self, callback: Callable = lambda: None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.callback = callback

    @property
    def app(self) -> "Dooit":
        pass

    @property
    def api(self) -> "DooitAPI":  # pragma: no cover
        pass

    @property
    def switcher(self) -> "BarSwitcher":
        pass

    async def on_unmount(self):
        pass

    def perform_action(self, cancel: bool):
        pass

    def dismiss(self, cancel: bool):
        pass

    async def handle_keypress(self, key: str) -> None:  # pragma: no cover
        pass
