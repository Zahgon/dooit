from rich.console import RenderableType
from dooit.ui.api.events.events import NotificationType
from .._base import BarBase


class NotificationBar(BarBase):
    DEFAULT_CSS = """
    NotificationBar {
        padding-left: 1;
        padding-right: 1;
    }
    """

    def __init__(
        self,
        message: str,
        level: NotificationType = "info",
        auto_exit: bool = True,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.message = message
        self.level = level
        self.auto_exit = auto_exit
        self.focused = not auto_exit
        self.add_class(self.level)

    def perform_action(self, cancel: bool):
        pass

    def on_mount(self):
        pass

    async def handle_keypress(self, key: str) -> None:
        pass

    def render(self) -> RenderableType:
        pass
