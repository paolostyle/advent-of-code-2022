from datetime import datetime
import textwrap
from pathlib import Path
from typing import Optional

import click
import requests

from cli.config import COOKIE_PATH, MODULE_NAME, YEAR
from cli.utils import get_aoc_timezone

starting_code = textwrap.dedent(
    """
    def part_1(input: str) -> int:
        pass


    def part_2(input: str) -> int:
        pass
    """
).lstrip()


def download_input(day: int) -> str:
    cookie = Path(COOKIE_PATH)

    if not cookie.exists():
        click.secho("Input downloading is not configured. See README.", fg="red")
        return ""

    response = requests.get(
        f"https://adventofcode.com/{YEAR}/day/{day}/input",
        cookies={"session": cookie.read_text()},
    )

    if response.status_code == 200:
        click.secho("Successfully downloaded input file", fg="green")
        return response.text

    if response.status_code == 404:
        click.secho(
            "The input file is not yet available, saving an empty file", fg="yellow"
        )
    else:
        click.secho(
            "Unknown error occurred while downloading the file, saving an empty file",
            fg="yellow",
        )

    return ""


def open_day_description(day: int) -> None:
    if datetime.now(get_aoc_timezone()) > datetime(
        YEAR, 12, day, tzinfo=get_aoc_timezone()
    ):
        click.launch(f"https://adventofcode.com/{YEAR}/day/{day}")


def create_if_not_exists(
    path: Path,
    text: str,
    created_msg: Optional[str] = None,
    exists_msg: Optional[str] = None,
) -> None:
    if not path.exists():
        path.write_text(text)
        if created_msg:
            click.secho(created_msg, fg="green")
    elif exists_msg:
        click.secho(exists_msg, fg="yellow")


def get_folder_path(day_name: str) -> Path:
    folder_path = Path(f"{MODULE_NAME}") / day_name
    folder_path.mkdir(exist_ok=True)

    create_if_not_exists(folder_path / Path("__init__.py"), text="")

    return folder_path
