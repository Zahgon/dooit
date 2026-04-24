from typing import TYPE_CHECKING, Any, Callable, Dict, List, Optional, Tuple, Union
from uuid import uuid4
from dataclasses import dataclass

from rich.text import Text
from dooit.api.workspace import ModelType
from dooit.ui.api.api_components.formatters._decorators import MUTLIPLE_FORMATTER_ATTR

if TYPE_CHECKING:  # pragma: no cover
    from dooit.ui.api.dooit_api import DooitAPI

FormatterReturnType = Union[str, Tuple[str, bool]]


@dataclass
class FormatterFunc:
    name: str
    func: Callable
    disabled: bool = False


def trigger_refresh(func: Callable) -> Callable:
    pass


class FormatterStore:
    def __init__(self, trigger: Callable, api: "DooitAPI") -> None:
        self.formatters = dict()
        self.trigger = trigger
        self.api = api

    @trigger_refresh
    def add(self, func: Callable, id: Optional[str] = None) -> str:
        pass

    def get_formatter_by_id(self, id: str) -> Optional[FormatterFunc]:
        pass

    @trigger_refresh
    def remove(self, id: str) -> None:
        pass

    @trigger_refresh
    def disable(self, id: str) -> bool:
        pass

    @trigger_refresh
    def enable(self, id: str) -> bool:
        pass

    @property
    def type1_formatter_functions(self) -> List[Callable]:
        pass

    @property
    def type2_formatter_functions(self) -> List[Callable]:
        pass

    def _get_function_params(self, func: Callable) -> List[str]:
        pass

    def format_value(self, value: Any, model: ModelType) -> Text:
        pass
