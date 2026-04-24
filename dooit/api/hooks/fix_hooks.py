from sqlalchemy import event, text
from ..workspace import Workspace
from ..todo import Todo


@event.listens_for(Workspace, "before_insert")
def fix_order_id_workspace(_, connection, target: Workspace):
    pass


@event.listens_for(Todo, "before_insert")
def fix_order_id_todo(_, connection, target: Todo):
    pass
