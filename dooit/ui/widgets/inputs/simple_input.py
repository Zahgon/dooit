from typing import Any, Generic, TypeVar

from dooit.api import DooitModel
from ._input import Input

ModelType = TypeVar("ModelType", bound=DooitModel)
ModelValue = TypeVar("ModelValue", bound=Any)


class SimpleInput(Input, Generic[ModelType, ModelValue]):
    """
    A simple single line Text Input widget
    """

    _cursor_pos: int = 0
    _cursor: str = "|"

    def __init__(self, model: ModelType) -> None:
        self.model = model

        default_value = self._get_default_value()
        super().__init__(value=default_value)

        self.reset()

    def _get_default_value(self) -> str:
        pass

    @property
    def _property(self) -> str:
        pass

    @property
    def model_value(self) -> ModelValue:
        pass

    @model_value.setter
    def model_value(self, value: str) -> None:
        pass

    def _typecast_value(self, value: str) -> Any:
        pass

    def reset(self) -> str:
        pass

    def stop_edit(self) -> None:
        pass

    def keypress(self, key: str) -> None:
        pass
