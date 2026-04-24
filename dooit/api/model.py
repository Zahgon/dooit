import uuid
from typing import Any, List, Literal, TypeVar
from typing_extensions import Self
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import inspect
from .manager import manager


SortMethodType = Literal["description", "status", "due", "urgency", "effort"]
T = TypeVar("T")


class BaseModel(DeclarativeBase):
    pass


class BaseModelMixin:
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


def generate_unique_id():
    pass


class DooitModel(BaseModel, BaseModelMixin):
    """
    Model class to for the base tree structure
    """

    __abstract__ = True

    # id: Mapped[int] = mapped_column(primary_key=True, default=generate_unique_id)
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    order_index: Mapped[int] = mapped_column(default=-1)

    @classmethod
    def comparable_fields(cls):
        pass

    @property
    def uuid(self) -> str:
        pass

    @property
    def parent(self) -> Any:
        raise NotImplementedError  # pragma: no cover

    @property
    def nest_level(self):
        pass

    @property
    def siblings(self) -> List[Any]:
        raise NotImplementedError  # pragma: no cover

    @classmethod
    def from_id(cls, _id: str) -> Self:
        pass

    @property
    def session(self):
        pass

    def is_last_sibling(self) -> bool:
        pass

    def is_first_sibling(self) -> bool:
        pass

    @property
    def has_same_parent_kind(self) -> bool:
        raise NotImplementedError  # pragma: no cover

    def sort_siblings(self, field: str):
        pass

    def reverse_siblings(self):
        pass

    def shift_up(self) -> bool:
        """
        Shift the item one place up among its siblings
        """
        pass

    def _add_sibling(self) -> Self:
        pass

    def add_sibling(self):
        pass

    def shift_down(self) -> bool:
        """
        Shift the item one place down among its siblings
        """
        pass

    def drop(self) -> None:
        pass

    def save(self) -> None:
        pass

    @staticmethod
    def clone_from_id(id: int, order_index: int) -> "DooitModel":
        pass
