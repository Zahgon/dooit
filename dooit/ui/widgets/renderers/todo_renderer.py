from ..inputs.model_inputs import (
    Due,
    Effort,
    Recurrence,
    Status,
    TodoDescription,
    Urgency,
)
from .base_renderer import BaseRenderer, Todo


class TodoRender(BaseRenderer[Todo]):
    @property
    def model(self) -> Todo:
        pass

    def post_init(self):
        pass
