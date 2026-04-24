from typing import TYPE_CHECKING
from dooit.ui.api.events import BarNotification, NotificationType
from dooit.ui.api.plug import PluginManager
from .events import DooitEvent, SwitchTab, QuitApp
from dooit.ui.widgets import ModelTree
from dooit.ui.widgets.trees import TodosTree
from dooit.utils import CssManager

from .api_components import (
    KeyManager,
    KeyMatchType,
    LayoutManager,
    Formatter,
    BarManager,
    VarManager,
    DashboardManager,
)

if TYPE_CHECKING:  # pragma: no cover
    from ..tui import Dooit


class DooitAPI:
    def __init__(
        self,
        app: "Dooit",
    ) -> None:
        self.app = app
        self.plugin_manager = PluginManager(self, app.config)
        self.css = CssManager()
        self.keys = KeyManager(self.app.get_dooit_mode)
        self.layouts = LayoutManager(self.app)
        self.formatter = Formatter(self)
        self.bar = BarManager(self)
        self.vars = VarManager(self)
        self.dashboard = DashboardManager(self.app)

        self.css.refresh_css()

    def no_op(self):
        """<NOP>"""
        pass

    def quit(self):
        """Quit dooit"""
        pass

    def notify(self, message: str, level: NotificationType = "info") -> None:
        pass

    async def handle_key(self, key: str) -> None:
        pass

    def trigger_event(self, event: DooitEvent):
        pass

    # -----------------------------------------

    @property
    def focused(self) -> ModelTree:
        pass

    def copy_description_to_clipboard(self):
        """Copy the description of the focused item to the clipboard"""
        pass

    def copy_model(self):
        """Copy the current highlighted node to clipboard"""
        pass

    def paste_model_above(self):
        """Paste the copied node in the list (puts above the highlighted)"""
        pass

    def paste_model_below(self):
        """Paste the copied node in the list (puts below the highlighted)"""
        pass

    def switch_focus(self):
        """Switch focus between the workspace and the todo list"""
        pass

    def move_down(self):
        """Move the cursor down in the focused list"""
        pass

    def move_up(self):
        """Move the cursor up in the focused list"""
        pass

    def shift_up(self):
        """Shift the highlighted item up"""
        pass

    def shift_down(self):
        """Shift the highlighted item down"""
        pass

    def go_to_top(self):
        """Move the cursor to the top of the list"""
        pass

    def go_to_bottom(self):
        """Move the cursor to the bottom of the list"""
        pass

    def edit(self, property: str):
        """Start editing a property of the focused item"""
        pass

    def edit_description(self):
        """Start editing the description of the focused item"""
        pass

    def edit_due(self):
        """Start editing the due date of the todo"""
        pass

    def edit_recurrence(self):
        """Start editing the recurrence of the todo"""
        pass

    def edit_effort(self):
        pass

    def add_sibling(self):
        """Add a sibling to highlighted item"""
        pass

    def toggle_expand(self):
        """Toggle the expansion of the highlighted item"""
        pass

    def toggle_expand_parent(self):
        """Toggle the expansion of the parent of the highlighted item"""
        pass

    def add_child_node(self):
        """Add a child to the highlighted item"""
        pass

    def remove_node(self):
        """Remove the highlighted item"""
        pass

    def start_search(self):
        """Start a search within the list"""
        pass

    def start_sort(self):
        """Start sorting the siblings of the highlighted item"""
        pass

    def toggle_complete(self):
        """Toggle the completion of the todo"""
        pass

    def increase_urgency(self):
        """Increase the urgency of the todo"""
        pass

    def decrease_urgency(self):
        """Decrease the urgency of the todo"""
        pass

    def show_help(self):
        """Show the help screen"""
        pass
