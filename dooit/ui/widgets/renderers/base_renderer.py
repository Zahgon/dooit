from typing import TYPE_CHECKING, Generic, List, TypeVar, Union
from rich.console import RenderableType
from rich.table import Table
from dooit.api import Todo, Workspace
from ..inputs.simple_input import SimpleInput

ModelType = TypeVar("ModelType", bound=Union[Todo, Workspace])

if TYPE_CHECKING:  # pragma: no cover
    from dooit.ui.widgets.trees.model_tree import ModelTree


class BaseRenderer(Generic[ModelType]):
    editing: str = ""

    def __init__(self, model: ModelType, tree: "ModelTree"):
        self._model = model
        self.tree = tree
        self.post_init()

    def post_init(self):  # pragma: no cover
        pass

    def matches_filter(self, filter: str) -> bool:
        pass

    def _get_component(self, component: str) -> SimpleInput:
        pass

    @property
    def id(self) -> str:
        pass

    @property
    def table_layout(self) -> List:
        pass

    @property
    def prompt(self) -> RenderableType:
        pass

    @property
    def model(self) -> ModelType:
        raise NotImplementedError  # pragma: no cover

    def _get_attr_width(self, attr: str) -> int:
        pass

    def _get_max_width(self, attr: str) -> int:
        pass

    def make_renderable(self) -> Table:
        pass

    def start_edit(self, param: str) -> bool:
        pass

    def stop_edit(self):
        pass

    def handle_keypress(self, key: str) -> bool:
        pass
