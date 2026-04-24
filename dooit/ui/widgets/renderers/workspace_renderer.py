from .base_renderer import BaseRenderer, Workspace
from ..inputs.model_inputs import WorkspaceDescription


class WorkspaceRender(BaseRenderer[Workspace]):
    @property
    def model(self) -> Workspace:
        pass

    def post_init(self):
        pass
