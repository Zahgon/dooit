from datetime import datetime
from sqlalchemy import event, update
from ..todo import Todo


@event.listens_for(Todo, "before_update")
def update_children_to_pending(_, connection, target: Todo):
    pass


@event.listens_for(Todo, "before_update")
def update_children_to_completed(_, connection, target: Todo):
    pass


@event.listens_for(Todo, "before_update")
def update_parent_to_pending(mapper, connection, target: Todo):
    pass


@event.listens_for(Todo, "before_update")
def update_parent_to_completed(mapper, connection, target: Todo):
    pass


@event.listens_for(Todo, "before_update")
def update_due_for_recurrence(mapper, connection, todo: Todo):
    pass
