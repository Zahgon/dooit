import pyperclip
from typing import Optional


class Input:
    """
    A simple single line Text Input
    """

    _cursor: str = "|"
    highlight_pattern = ""
    is_editing = False

    def __init__(self, value="") -> None:
        self._value = value
        self._cursor_position = len(self._value)

    @property
    def value(self) -> str:
        pass

    def draw(self) -> str:
        pass

    def render(self) -> str:
        pass

    def _render_text_with_cursor(self) -> str:
        """
        Produces renderable Text object combining value and cursor
        """
        pass

    def start_edit(self) -> None:
        pass

    def stop_edit(self) -> None:
        pass

    def _insert_text(self, text: Optional[str] = None) -> None:
        """
        Inserts text where the cursor is
        """
        pass

    def _move_cursor_backward(self, word=False, delete=False) -> None:
        """
        Moves the cursor backwards..
        Optionally jumps over a word when pressed ctrl+left
        Optionally deletes the letter in case of backspace
        """
        pass

    def _move_cursor_forward(self, word=False, delete=False) -> None:
        """
        Moves the cursor forward..
        Optionally jumps over a word when pressed ctrl+right
        Optionally deletes the letter in case of del or ctrl+del
        """
        pass

    def clear_input(self) -> None:
        pass

    def move_cursor_to_end(self) -> None:
        pass

    def keypress(self, key: str) -> None:
        # Moving backward
        pass
