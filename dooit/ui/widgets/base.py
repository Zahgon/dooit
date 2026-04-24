from textual.widget import Widget
from dooit.ui.api.events import ModeChanged, ModeType


class HelperWidget(Widget):
    """
    Helper Widgets to Tree Widgets
    Currently base for `SortOptions` and `SearchMenu`
    """

    DEFAULT_CSS = """
    HelperWidget {
        layer: L1;
        display: none;
    }
    """

    _status: ModeType

    async def hide(self) -> None:
        pass

    async def start(self) -> None:
        pass

    async def cancel(self) -> None:
        pass

    async def stop(self):
        pass
