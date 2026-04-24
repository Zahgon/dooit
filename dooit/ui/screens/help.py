from collections.abc import Callable
from rich.console import Group, RenderableType
from rich.style import Style
from rich.table import Table
from rich.text import Text
from textual.app import ComposeResult
from textual.widgets import Static

from dooit.ui.api.api_components.keys import KeyManager
from .base import BaseScreen


class HelpWidget(Static):
    DEFAULT_CSS = """
    HelpWidget {
        content-align: center middle;
        width: 80%;
        margin: 1;
    }
    """


class Header(HelpWidget):
    def render(self) -> RenderableType:
        pass


class Outro(HelpWidget):
    COMPONENT_CLASSES = {
        "exit",
        "thanks",
        "github",
    }

    def render(self) -> RenderableType:
        pass


class DooitKeyTable(HelpWidget):
    DEFAULT_CSS = """
    DooitKeyTable {
        padding: 1 2;
    }
    """

    COMPONENT_CLASSES = {
        "keybind",
        "arrow",
        "description",
        "table-title",
    }
    BORDER_TITLE = "Key Bindings"

    def __init__(self, keybinds: KeyManager, no_op: Callable):
        super().__init__()
        self.keybinds = keybinds
        self.no_op = no_op

    def render(self) -> RenderableType:
        pass


class HelpScreen(BaseScreen):
    """
    Help Screen to view Help Menu
    """

    DEFAULT_CSS = """
    HelpScreen {
        align: center top;
    }
    """

    BINDINGS = [
        ("escape", "app.pop_screen", "Pop screen"),
    ]

    def compose(self) -> ComposeResult:
        pass

    def key_down(self):
        pass

    def key_up(self):
        pass

    def key_j(self):
        pass

    def key_k(self):
        pass
