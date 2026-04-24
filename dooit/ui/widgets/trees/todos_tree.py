from typing import TYPE_CHECKING, Optional, Union
from textual import on
from textual.widgets.option_list import Option

from dooit.api import Todo, Workspace
from dooit.ui.api.events import TodoRemoved
from dooit.ui.api.events.events import TodoSelected
from .model_tree import ModelTree
from ..renderers.todo_renderer import TodoRender
from ._render_dict import TodoRenderDict

if TYPE_CHECKING:  # pragma: no cover
    from ...api.api_components.formatters.model_formatters import (
        TodoFormatter,
    )

Model = Union[Todo, Workspace]


class TodosTree(ModelTree[Model, TodoRenderDict]):
    BORDER_TITLE = "Todos"

    def __init__(self, model: Model) -> None:
        super().__init__(model, TodoRenderDict(self))

    def _get_parent(self, id: str) -> Optional[Todo]:
        pass

    def is_node_expaned(self, _id: str) -> bool:
        pass

    @property
    def formatter(self) -> "TodoFormatter":
        pass

    @property
    def render_layout(self):
        pass

    def add_todo(self) -> str:
        pass

    def _add_first_item(self) -> Todo:
        pass

    def _create_child_node(self) -> Todo:
        pass

    def _remove_node(self) -> None:
        pass

    def toggle_complete(self):
        pass

    def increase_urgency(self):
        pass

    def decrease_urgency(self):
        pass

    @on(ModelTree.OptionHighlighted)
    def todo_highlighted(self, event: ModelTree.OptionHighlighted):
        pass
