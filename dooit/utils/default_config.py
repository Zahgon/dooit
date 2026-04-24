from datetime import datetime, timedelta
import os
from typing import Optional
from rich.style import Style
from dooit.api import Todo
from dooit.ui.api import DooitAPI, subscribe, timer
from dooit.ui.api.widgets import TodoWidget, WorkspaceWidget
from dooit.ui.api.events import ModeChanged, Startup
from dooit.ui.widgets.bars import StatusBarWidget
from dooit.ui.widgets.inputs.model_inputs import Recurrence
from rich.text import Text


@subscribe(ModeChanged)
def get_mode(api: DooitAPI, event: ModeChanged):
    pass


@timer(1)
def get_clock(api: DooitAPI):
    pass


@subscribe(Startup)
def get_user(api: DooitAPI, _: Startup):
    pass


# Todo formatters


def todo_status_formatter(status: str, _: Todo, api: DooitAPI):
    pass


def todo_due_formatter(due, _):
    pass


def todo_urgency_formatter(urgency, _, api: DooitAPI):
    pass


def todo_recurrence_formatter(recurrence: Optional[timedelta], _):
    pass


# Workspace formatters


@subscribe(Startup)
def key_setup(api: DooitAPI, _):
    pass


@subscribe(Startup)
def layout_setup(api: DooitAPI, _):
    pass


@subscribe(Startup)
def formatter_setup(api: DooitAPI, _):
    pass


@subscribe(Startup)
def bar_setup(api: DooitAPI, _):
    pass


@subscribe(Startup)
def dashboard_setup(api: DooitAPI, _):
    pass
