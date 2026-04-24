from typing import Callable
from rich.console import RenderableType
from rich.text import Text
from dooit.ui.widgets.bars._base import BarBase
from dooit.api import DooitModel


class SortBar(BarBase):
    COMPONENT_CLASSES = {
        "option-highlighted",
    }

    def __init__(self, model: DooitModel, callback: Callable, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model
        self.callback = callback
        self.options = ["reverse"] + self.model.comparable_fields()
        self._selected = 0

    @property
    def selected(self) -> int:
        pass

    @selected.setter
    def selected(self, val: int):
        pass

    def perform_action(self, cancel: bool):
        pass

    async def handle_keypress(self, key: str) -> None:
        pass

    def render(self) -> RenderableType:
        pass
