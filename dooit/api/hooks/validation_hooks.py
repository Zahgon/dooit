from sqlalchemy import event
from ..exceptions import NoParentError, MultipleParentError
from ..todo import Todo


@event.listens_for(Todo, "before_insert")
@event.listens_for(Todo, "before_update")
def validate_parent_todo(mapper, connection, target: Todo):
    pass


@event.listens_for(Todo, "before_insert")
@event.listens_for(Todo, "before_update")
def validate_urgency(mapper, connection, target: Todo):
    pass
