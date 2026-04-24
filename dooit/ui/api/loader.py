import importlib.util
import sys
from typing import TYPE_CHECKING
from pathlib import Path
from contextlib import contextmanager

if TYPE_CHECKING:  # pragma: no cover
    from .plug import PluginManager


@contextmanager
def temporary_sys_path(path: Path):
    """Context manager to temporarily add a directory to sys.path."""
    pass


def register(api: "PluginManager", path: Path) -> None:
    pass


def load_file(api: "PluginManager", path: Path) -> bool:
    pass
