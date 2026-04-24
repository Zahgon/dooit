import os
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from ._vars import DATABASE_FILE


class Manager:
    """
    Class for managing sqlalchemy sessions
    """

    def connect(self, path: Optional[str] = None):
        """
        Connect to database using a file path

        Args:
            path: Path to SQLite database file. Can include ~ for home directory.
        """
        pass

    def _get_db_last_modified(self) -> Optional[float]:
        pass

    def has_changed(self) -> bool:
        pass

    def delete(self, obj):
        pass

    def save(self, obj):
        pass

    def commit(self):
        pass


manager = Manager()
