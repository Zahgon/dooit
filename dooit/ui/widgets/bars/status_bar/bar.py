from typing import List
from rich.console import RenderableType
from rich.table import Table

from .._base import BarBase
from .bar_widget import StatusBarWidget


class StatusBar(BarBase):
    bar_widgets = []

    def set_widgets(self, widgets: List[StatusBarWidget]) -> None:
        pass

    def render(self) -> RenderableType:
        pass
