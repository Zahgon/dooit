import re
from datetime import datetime, timedelta
from typing import List, Optional, Tuple
from yaml import safe_load
from pathlib import Path
from platformdirs import user_data_dir
from dooit.api import Todo, Workspace, manager
from dooit.utils.cli_logger import logger
from dooit.utils.database import delete_all_data

manager.connect()
BASE_PATH = Path(user_data_dir("dooit"))
operations = []


def parse_recurrence(recurrence: str) -> timedelta:
    pass


def parse_due(due: str) -> Optional[datetime]:
    pass


class Migrator2to3:
    old_location = BASE_PATH / "todo.yaml"
    new_location = BASE_PATH / "dooit.db"

    @classmethod
    def check_for_old_data(cls):
        pass

    def load_old(self):
        pass

    def backup_old_config(self):
        pass

    def migrate(self):
        pass

    # ------------------------------------------------

    def create_workspace(self, data, parent=None):
        pass

    def create_todo(self, data: List, parent_todo=None, parent_workspace=None):
        pass


if __name__ == "__main__":
    m = Migrator2to3()
    if m.check_for_old_data():
        m.migrate()
