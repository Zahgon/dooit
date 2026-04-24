from pathlib import Path
from typing import Optional

import click
from platformdirs import user_config_dir, user_data_dir

OLD_CONFIG = Path(user_data_dir("dooit")) / "todo.yaml"
VERSION = "3.3.4"


def run_dooit(config: Optional[str] = None, db_path: Optional[str] = None):
    pass


@click.group(
    context_settings={"help_option_names": ["-h", "--help"]},
    invoke_without_command=True,
)
@click.option(
    "--version",
    "-v",
    is_flag=True,
    help="Show version and exit.",
)
@click.option("-c", "--config", default=None, help="Path to config file")
@click.option("--db", default=None, help="Path to database file")
@click.pass_context
def main(ctx, version: bool, config: str, db: str) -> None:
    pass


@main.command(help="Migrate data from v2 to v3.")
def migrate() -> None:
    pass


@main.command(help="Show config location.")
def config_loc() -> None:
    """Print the location of the configuration file."""
    pass


if __name__ == "__main__":
    main()
