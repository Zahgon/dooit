from collections import defaultdict
from functools import cache
from typing import TYPE_CHECKING, Any, Generic, Optional, TypeVar, Union
from textual.app import ComposeResult
from textual.widgets import Label
from textual.widgets.option_list import Option
from dooit.api import Todo, Workspace
from dooit.ui.api.events import (
    ModeChanged,
    StartSearch,
    StartSort,
    BarNotification,
)
from dooit.ui.widgets.renderers import BaseRenderer
from .base_tree import BaseTree
from ._render_dict import RenderDict
from ._decorators import (
    fix_highlight,
    refresh_tree,
    require_highlighted_node,
    require_confirmation,
)

if TYPE_CHECKING:  # pragma: no cover
    from dooit.ui.api.api_components.formatters._model_formatter_base import (
        ModelFormatterBase,
    )

ModelType = TypeVar("ModelType", bound=Union[Todo, Workspace])
RenderDictType = TypeVar("RenderDictType", bound=RenderDict)


class ModelTree(BaseTree, Generic[ModelType, RenderDictType]):
    DEFAULT_CSS = """
    ModelTree {
        height: 1fr;
        width: 1fr;
        align: center middle;

        & > Label {
            align: center middle;
        }
    }
    """

    def __init__(self, model: ModelType, render_dict: RenderDictType) -> None:
        tree = self.__class__.__name__
        super().__init__(id=f"{tree}_{model.uuid}")
        self._model = model
        self.expaned = defaultdict(bool)
        self._renderers: RenderDictType = render_dict
        self._filter_refresh = False
        self._model_clipboard = None

    @cache
    def get_column_width(self, attr: str) -> int:
        pass

    @property
    def formatter(self) -> "ModelFormatterBase":
        raise NotImplementedError  # pragma: no cover

    @property
    def render_layout(self) -> Any:
        raise NotImplementedError  # pragma: no cover

    @property
    def filter_refresh(self):
        pass

    @filter_refresh.setter
    def filter_refresh(self, value: bool):
        pass

    @property
    def current(self) -> BaseRenderer:
        pass

    @property
    def current_model(self) -> ModelType:
        pass

    def update_prompt_at_index(self, index: int):
        pass

    def update_prompt_by_id(self, _id: str):
        pass

    def update_current_prompt(self):
        pass

    def set_filter(self, filter: str) -> None:
        pass

    @property
    def is_editing(self) -> bool:
        pass

    @property
    def model(self) -> ModelType:
        pass

    @property
    def empty_message(self) -> Label:
        pass

    @fix_highlight
    def force_refresh(self) -> None:
        pass

    def is_node_expaned(self, _id: str) -> bool:
        pass

    def _force_refresh(self) -> None:
        pass

    def on_mount(self):
        pass

    @require_highlighted_node
    def start_sort(self):
        pass

    @require_highlighted_node
    def start_search(self):
        pass

    def start_edit(self, property: str) -> bool:
        pass

    def stop_edit(self):
        pass

    def reset_state(self):
        """
        Reset tree of any modified status for e.g. search
        """
        pass

    async def handle_keypress(self, key: str) -> bool:
        pass

    def refresh_options(self) -> None:
        pass

    def _get_parent(self, id: str) -> Optional[ModelType]:
        pass

    @require_highlighted_node
    def copy_description_to_clipboard(self):
        pass

    @refresh_tree
    def _expand_node(self, _id: str) -> None:
        pass

    def expand_node(self) -> None:
        pass

    @refresh_tree
    def _collapse_node(self, _id: str) -> None:
        pass

    def _toggle_expand_node(self, _id: str) -> None:
        pass

    @require_highlighted_node
    def toggle_expand(self) -> None:
        pass

    def _toggle_expand_parent(self, _id: str) -> None:
        pass

    @require_highlighted_node
    def toggle_expand_parent(self) -> None:
        pass

    def _create_child_node(self) -> ModelType:
        pass

    def add_child_node(self):
        pass

    def _create_sibling_node(self) -> ModelType:
        pass

    def highlight_id(self, _id: str):
        pass

    @refresh_tree
    def _add_sibling_node(self) -> ModelType:
        pass

    @refresh_tree
    def add_first_item(self) -> ModelType:
        pass

    def _add_first_item(self) -> ModelType:
        pass

    def add_sibling(self):
        pass

    @require_confirmation
    @refresh_tree
    def _remove_node(self):
        pass

    @require_highlighted_node
    def copy_model_to_clipboard(self):
        pass

    def paste_model_from_clipboard(
        self, position: str = "below"
    ) -> Optional[ModelType]:
        pass

    @require_highlighted_node
    def remove_node(self):
        pass

    @refresh_tree
    def shift_up(self) -> None:
        pass

    @refresh_tree
    def shift_down(self):
        pass

    @refresh_tree
    def sort(self, attr: str):
        pass

    def show_help(self):
        pass

    def compose(self) -> ComposeResult:
        pass
