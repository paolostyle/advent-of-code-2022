from datetime import datetime
import importlib
import os
from pathlib import Path
import sys
import textwrap
from typing import Optional
import click

import pytz
import requests

from cli.config import MODULE_NAME, YEAR


def get_default_day() -> dict:
    current_date = datetime.now(pytz.timezone("America/New_York"))
    if current_date.year == YEAR and current_date.month == 12:
        return {"default": current_date.day, "required": False}
    return {"default": None, "required": True}


def get_day_name(day: int) -> str:
    return f"day{day:0>2}"


def load_input_file(day: int, test_input_file: Optional[str]) -> str:
    day_name = get_day_name(day)

    try:
        input_file = test_input_file or "input.txt"
        return Path(f"{MODULE_NAME}/{day_name}/{input_file}").read_text()
    except FileNotFoundError:
        self_name = os.path.basename(__file__)

        click.secho("ERROR: ", fg="red", bold=True, nl=False)
        click.secho(
            f"No input file ({input_file}) found! Consider running ", fg="red", nl=False
        )
        click.secho(
            f"./{self_name} create --day {day} ",
            fg="red",
            bold=True,
            nl=False,
        )
        click.secho("or verify that file exists and try again.", fg="red")

        sys.exit(1)


def load_module(day: int):
    day_name = get_day_name(day)
    try:
        return importlib.import_module(f"{MODULE_NAME}.{day_name}.{day_name}")
    except ModuleNotFoundError as module_error:
        self_name = os.path.basename(__file__)

        click.secho("ERROR: ", fg="red", bold=True, nl=False)
        click.secho(
            f"{module_error.msg}) found! Consider running ",
            fg="red",
            nl=False,
        )
        click.secho(
            f"./{self_name} create --day {day} ",
            fg="red",
            bold=True,
            nl=False,
        )
        click.secho("or verify that file exists and try again.", fg="red")

        sys.exit(1)


def download_input(day: int) -> str:
    cookies = {"session": Path("cookie").read_text()}
    response = requests.get(
        f"https://adventofcode.com/{YEAR}/day/{day}/input", cookies=cookies
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


starting_code = textwrap.dedent(
    """
    def part_1(input: str):
        pass


    def part_2(input: str):
        pass
    """
).lstrip()
