from dooit.api.model import DooitModel
from dooit.ui.widgets.todo import TodoWidget


class Clipboard:
    """
    Clipboard to copy models (Todos and Workspaces) as a whole
    """

    data = None

    def copy(self, widget: TodoWidget):
        pass

    @property
    def has_data(self) -> bool:
        pass
