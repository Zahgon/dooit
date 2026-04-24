from pathlib import Path
from typing import Optional
from textual import on
from textual.app import App
from textual.binding import Binding
from dooit.ui.api.events import ModeChanged, DooitEvent, ModeType, Startup, QuitApp
from dooit.ui.api.events.events import ShutDown
from dooit.ui.widgets import BarSwitcher
from dooit.ui.widgets.bars import StatusBar
from dooit.ui.widgets.trees import WorkspacesTree
from dooit.ui.screens import MainScreen, HelpScreen
from dooit.ui.widgets.trees.model_tree import ModelTree
from dooit.utils import CssManager
from .api import DooitAPI
from ..api import manager

PRINTABLE = (
    "0123456789"
    + "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    + "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "
)


class Dooit(App):
    CSS_PATH = CssManager().css_file
    ENABLE_COMMAND_PALETTE = False

    SCREENS = {
        "help": HelpScreen,
        "main": MainScreen,
    }

    BINDINGS = [
        Binding("ctrl+c", "quit", "Quit", show=False, priority=True),
    ]

    def __init__(
        self,
        db_path: Optional[str] = None,
        config: Optional[Path] = None,
    ):
        super().__init__(watch_css=True)
        self.dooit_mode: ModeType = "NORMAL"
        self.config = config
        manager.connect(db_path)

    async def base_setup(self):
        pass

    async def setup_poller(self):
        pass

    async def on_mount(self):
        pass

    async def action_quit(self) -> None:
        pass

    @property
    def workspace_tree(self) -> WorkspacesTree:
        pass

    @property
    def bar(self) -> StatusBar:
        pass

    @property
    def bar_switcher(self) -> BarSwitcher:
        pass

    def get_dooit_mode(self) -> ModeType:
        pass

    async def poll_dooit_db(self):  # pragma: no cover
        pass

    @on(DooitEvent)
    def global_message(self, event: DooitEvent):
        pass

    @on(ShutDown)
    def shutdown(self, _: ShutDown):
        pass

    @on(ModeChanged)
    def change_status(self, event: ModeChanged):
        pass

    @on(QuitApp)
    async def quit_app(self):
        pass

    async def action_open_url(self, url: str) -> None:  # pragma: no cover
        pass


if __name__ == "__main__":  # pragma: no cover
    Dooit().run()
