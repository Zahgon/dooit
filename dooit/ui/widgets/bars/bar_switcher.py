from typing import Callable, Optional
from textual.await_complete import AwaitComplete
from textual.widget import Widget
from textual.widgets import ContentSwitcher
from dooit.api.model import DooitModel
from dooit.ui.api.events.events import BarNotification
from dooit.ui.widgets.bars._base import BarBase
from .status_bar import StatusBar
from .search_bar import SearchBar
from .confirm_bar import ConfirmBar
from .notification_bar import NotificationBar
from .sort_bar import SortBar


class BarSwitcher(ContentSwitcher):
    DEFAULT_CSS = """
    BarSwitcher {
        height: 1;
        width: 100%;
    }
    """

    @property
    def search_bar(self):
        pass

    @property
    def visible_content(self) -> BarBase:
        pass

    @property
    def is_focused(self):
        pass

    def add_content(
        self, widget: Widget, *, id: Optional[str] = None, set_current: bool = False
    ) -> AwaitComplete:
        pass

    async def on_mount(self):
        pass

    def switch_to_search(self, callback: Callable):
        pass

    def switch_to_confirm(self, callback: Callable):
        pass

    def switch_to_sort(self, model: DooitModel, callback: Callable):
        pass

    def switch_to_notification(self, event: BarNotification):
        pass

    async def handle_keypress(self, key: str) -> None:
        pass
