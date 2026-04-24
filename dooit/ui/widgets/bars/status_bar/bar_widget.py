from collections.abc import Callable
from rich.text import TextType, Text
from typing import Optional


class StatusBarWidget:
    def __init__(
        self, func: Callable[..., TextType], width: Optional[int] = None
    ) -> None:
        self.func = func
        self.width = width

    @property
    def value(self) -> str:
        pass

    def render(self) -> TextType:
        pass
