from typing import Type
from sqlalchemy.event import listen
from sqlalchemy.orm.attributes import get_history
from textual import events, on
from textual.containers import Container
from textual.widgets import ContentSwitcher
from dooit.api import Todo, Workspace
from dooit.api.model import DooitModel
from dooit.ui.api.events import (
    DooitEvent,
    ModeChanged,
    ShowConfirm,
    StartSearch,
    StartSort,
    TodoDescriptionChanged,
    TodoDueChanged,
    TodoEffortChanged,
    TodoRecurrenceChanged,
    TodoStatusChanged,
    TodoUrgencyChanged,
    WorkspaceDescriptionChanged,
    WorkspaceSelected,
    SwitchTab,
    SpawnHelp,
    BarNotification,
)
from dooit.ui.widgets.trees import WorkspacesTree, TodosTree
from dooit.ui.widgets import BarSwitcher, Dashboard
from .base import BaseScreen


class DualSplit(Container):
    DEFAULT_CSS = """
    DualSplit {
        layout: grid;
        grid-size: 2 1;
        grid-columns: 2fr 8fr;
    }
    """


class DualSplitLeft(Container):
    pass


class DualSplitRight(Container):
    pass


class MainScreen(BaseScreen):
    DEFAULT_CSS = """
    MainScreen {
        layout: grid;
        grid-size: 1 2;
        grid-rows: 1fr 1;
    }
    """

    def compose(self):
        pass

    async def handle_key(self, event: events.Key) -> bool:
        # NOTE: Investigate why keys are sent to this screen
        pass

    @on(BarNotification)
    def show_notification(self, event: BarNotification):
        pass

    @on(SwitchTab)
    def switch_tab(self, event: SwitchTab) -> None:
        pass

    @on(SpawnHelp)
    async def spawn_help(self, _: SpawnHelp) -> None:
        pass

    @on(StartSearch)
    def start_search(self, event: StartSearch):
        pass

    @on(StartSort)
    def start_sort(self, event: StartSort):
        pass

    @on(ShowConfirm)
    def show_confirm(self, event: ShowConfirm):
        pass

    @on(WorkspaceSelected)
    async def workspace_selected(self, event: WorkspaceSelected):
        pass

    # SQLAlchemy event listeners

    def _track_field(
        self, table: Type[DooitModel], field: str, event: Type[DooitEvent]
    ) -> None:
        pass

    def on_mount(self):
        pass
