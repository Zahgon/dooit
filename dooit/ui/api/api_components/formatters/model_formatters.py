from ._model_formatter_base import ModelFormatterBase
from dooit.ui.widgets.trees import TodosTree, WorkspacesTree


class TodoFormatter(ModelFormatterBase):
    def setup_formatters(self):
        pass

    def trigger(self) -> None:
        pass


class WorkspaceFormatter(ModelFormatterBase):
    def setup_formatters(self):
        pass

    def trigger(self) -> None:
        pass
