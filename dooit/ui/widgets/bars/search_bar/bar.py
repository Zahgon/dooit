from typing import Callable
from rich.console import RenderableType

from .._base import BarBase
from ...inputs._input import Input


class SearchBar(BarBase):
    def __init__(self, callback: Callable, *args, **kwargs):
        super().__init__(callback, *args, **kwargs)
        self._search = Input(value="/")
        self._search.is_editing = True

    def perform_action(self, cancel: bool):
        pass

    async def handle_keypress(self, key: str) -> None:
        pass

    def render(self) -> RenderableType:
        pass
