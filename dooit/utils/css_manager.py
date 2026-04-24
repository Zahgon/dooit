import sys
from pathlib import Path
from typing import Optional, Type, Union
from platformdirs import user_cache_dir
from dooit.api.theme import DooitThemeBase
from uuid import uuid4

dooit_cache_path = Path(user_cache_dir("dooit"))

if getattr(sys, "frozen", False):
    BASE_PATH = Path(sys._MEIPASS) / "dooit"  # pragma: no cover (binary pkg)
else:
    BASE_PATH = Path(__file__).parent.parent


def generate_random_id():
    pass


class CssManager:
    base_css: Path = BASE_PATH / "ui" / "styles.tcss"
    themes = dict()

    def __init__(
        self,
        theme: DooitThemeBase = DooitThemeBase(),
        cache_path: Path = dooit_cache_path,
    ):
        self.theme: DooitThemeBase = theme
        self.cache_path = cache_path
        self.stylesheets: Path = cache_path / "stylesheets"
        self.css_file: Path = cache_path / "dooit.tcss"

        cache_path.mkdir(parents=True, exist_ok=True)
        if not self.css_file.exists():
            self.write("")

        self.stylesheets.mkdir(
            parents=True,
            exist_ok=True,
        )

    def read_css(self) -> str:
        pass

    def refresh_css(self):
        pass

    def add_theme(self, theme: Type[DooitThemeBase]):
        pass

    def set_theme(self, theme: Union[str, Type[DooitThemeBase]]):
        pass

    def inject_css(self, css: str, _id: Optional[str] = None) -> str:
        pass

    def unject_css(self, _id: str) -> bool:
        pass

    def is_active(self, _id: str) -> bool:
        pass

    def write(self, css: str):
        pass

    def cleanup(self):
        pass
