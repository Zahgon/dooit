from typing import TYPE_CHECKING, Optional
from textual import on
from textual.widgets.option_list import Option

from dooit.api import Workspace
from dooit.ui.api.events import (
    WorkspaceRemoved,
    WorkspaceSelected,
)
from .model_tree import ModelTree
from ._render_dict import WorkspaceRenderDict


if TYPE_CHECKING:  # pragma: no cover
    from dooit.ui.api.api_components.formatters.model_formatters import (
        WorkspaceFormatter,
    )


class WorkspacesTree(ModelTree[Workspace, WorkspaceRenderDict]):
    BORDER_TITLE = "Workspaces"

    def __init__(self, model: Workspace) -> None:
        render_dict = WorkspaceRenderDict(self)
        super().__init__(model, render_dict)

    def _get_parent(self, id: str) -> Optional[Workspace]:
        pass

    def is_node_expaned(self, _id: str) -> bool:
        pass

    @property
    def formatter(self) -> "WorkspaceFormatter":
        pass

    @property
    def render_layout(self):
        pass

    def add_workspace(self) -> str:
        pass

    def _create_child_node(self) -> Workspace:
        pass

    def _add_first_item(self) -> Workspace:
        pass

    def _remove_node(self) -> None:
        pass

    @on(ModelTree.OptionHighlighted)
    def workspace_highlighted(self, event: ModelTree.OptionHighlighted):
        pass
