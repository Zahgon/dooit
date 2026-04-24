from typing import TYPE_CHECKING, Optional, Union
from datetime import datetime, timedelta
from typing import List
from sqlalchemy import ForeignKey, select, nulls_last
from sqlalchemy.orm import Mapped, mapped_column, relationship, validates
from .model import DooitModel
from .manager import manager


if TYPE_CHECKING:  # pragma: no cover
    from dooit.api.workspace import Workspace


class Todo(DooitModel):
    # id: Mapped[int] = mapped_column(primary_key=True, default=generate_unique_id)
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    order_index: Mapped[int] = mapped_column(default=-1)
    description: Mapped[str] = mapped_column(default="")
    due: Mapped[Optional[datetime]] = mapped_column(default=None)
    effort: Mapped[int] = mapped_column(default=0)
    recurrence: Mapped[Optional[timedelta]] = mapped_column(default=None)
    urgency: Mapped[int] = mapped_column(default=1)
    pending: Mapped[bool] = mapped_column(default=True)

    # --------------------------------------------------------------
    # ------------------- Relationships ----------------------------
    # --------------------------------------------------------------

    parent_workspace_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("workspace.id")
    )
    parent_workspace: Mapped[Optional["Workspace"]] = relationship(
        "Workspace",
        back_populates="todos",
    )

    parent_todo_id: Mapped[Optional[int]] = mapped_column(ForeignKey("todo.id"))
    parent_todo: Mapped[Optional["Todo"]] = relationship(
        "Todo",
        back_populates="todos",
        remote_side=[id],
    )

    todos: Mapped[List["Todo"]] = relationship(
        "Todo",
        back_populates="parent_todo",
        cascade="all, delete-orphan",
        order_by=order_index,
    )

    @validates("recurrence")
    def validate_pending(self, key, value):
        pass

    @classmethod
    def from_id(cls, _id: str) -> "Todo":
        pass

    @property
    def parent(self) -> Union["Workspace", "Todo"]:
        pass

    @property
    def has_same_parent_kind(self) -> bool:
        pass

    @property
    def tags(self) -> List[str]:
        pass

    @property
    def status(self) -> str:
        pass

    @property
    def siblings(self) -> List["Todo"]:
        pass

    def sort_siblings(self, field: str):
        pass

    def add_todo(self) -> "Todo":
        pass

    def _add_sibling(self) -> "Todo":
        pass

    # ----------- HELPER FUNCTIONS --------------

    def increase_urgency(self) -> None:
        pass

    def decrease_urgency(self) -> None:
        pass

    def toggle_complete(self) -> None:
        pass

    def is_due_today(self) -> bool:
        pass

    @property
    def is_completed(self) -> bool:
        pass

    @property
    def is_pending(self) -> bool:
        pass

    @property
    def is_overdue(self) -> bool:
        pass

    @classmethod
    def all(cls) -> List["Todo"]:
        pass

    @staticmethod
    def clone_from_id(id: int, order_index: int) -> "Todo":
        pass

    @staticmethod
    def _clone_todo_recursively(source_todo: "Todo", parent_clone: "Todo") -> None:
        pass
