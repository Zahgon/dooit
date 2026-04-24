from typing import List, Optional, Union
from sqlalchemy import ForeignKey, asc, select
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..api.todo import Todo
from .model import DooitModel
from .manager import manager

ModelType = Union["Workspace", "Todo"]
ModelTypeList = Union[List["Workspace"], List["Todo"]]


class Workspace(DooitModel):
    # id: Mapped[int] = mapped_column(primary_key=True, default=generate_unique_id)
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    order_index: Mapped[int] = mapped_column(default=-1)
    description: Mapped[str] = mapped_column(default="")
    is_root: Mapped[bool] = mapped_column(default=False)

    # --------------------------------------------------------------
    # ------------------- Relationships ----------------------------
    # --------------------------------------------------------------

    parent_workspace_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("workspace.id"), default=None
    )
    parent_workspace: Mapped[Optional["Workspace"]] = relationship(
        "Workspace",
        back_populates="workspaces",
        remote_side=[id],
    )

    workspaces: Mapped[List["Workspace"]] = relationship(
        "Workspace",
        back_populates="parent_workspace",
        cascade="all",
        order_by="Workspace.order_index",
    )
    todos: Mapped[List["Todo"]] = relationship(
        "Todo",
        back_populates="parent_workspace",
        cascade="all, delete-orphan",
        order_by="Todo.order_index",
    )

    @classmethod
    def _get_or_create_root(cls) -> "Workspace":
        pass

    @classmethod
    def from_id(cls, _id: str) -> "Workspace":
        pass

    @property
    def parent(self) -> Optional["Workspace"]:
        pass

    @property
    def has_same_parent_kind(self) -> bool:
        pass

    @property
    def siblings(self) -> List["Workspace"]:
        pass

    def sort_siblings(self, field: str):
        pass

    def add_workspace(self) -> "Workspace":
        pass

    def add_todo(self) -> "Todo":
        pass

    def _add_sibling(self) -> "Workspace":
        pass

    def save(self) -> None:
        pass

    @classmethod
    def all(cls) -> List["Workspace"]:
        pass

    @staticmethod
    def clone_from_id(id: int, order_index: int) -> "Workspace":
        pass

    @staticmethod
    def _clone_workspace_recursively(
        source_workspace: "Workspace", parent_clone: "Workspace"
    ) -> None:
        pass
