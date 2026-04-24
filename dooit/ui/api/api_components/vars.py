from typing import TYPE_CHECKING, Optional

from textual.widgets import ContentSwitcher

from dooit.api import Workspace
from dooit.api.theme import DooitThemeBase
from dooit.api.todo import Todo
from dooit.ui.widgets.trees import WorkspacesTree, TodosTree
from ._base import ApiComponent


if TYPE_CHECKING:  # pragma: no cover
    from dooit.ui.api.dooit_api import DooitAPI


class VarManager(ApiComponent):
    def __init__(self, api: "DooitAPI") -> None:
        super().__init__()
        self.api = api
        self._show_confirm = True
        self._always_expand_workspaces = False
        self._always_expand_todos = False

    @property
    def always_expand_workspaces(self) -> bool:
        pass

    @always_expand_workspaces.setter
    def always_expand_workspaces(self, value: bool):
        pass

    @property
    def always_expand_todos(self) -> bool:
        pass

    @always_expand_todos.setter
    def always_expand_todos(self, value: bool):
        pass

    @property
    def show_confirm(self):
        pass

    @show_confirm.setter
    def show_confirm(self, value: bool):
        pass

    @property
    def mode(self) -> str:
        pass

    @property
    def theme(self) -> DooitThemeBase:
        pass

    @property
    def workspaces_tree(self) -> WorkspacesTree:
        pass

    @property
    def current_workspace(self) -> Optional[Workspace]:
        pass

    @property
    def todos_tree(self) -> Optional[TodosTree]:
        pass

    @property
    def current_todo(self) -> Optional[Todo]:
        pass
