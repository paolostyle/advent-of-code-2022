from pathlib import Path

import click
import requests

from cli.config import COOKIE_PATH, YEAR
from cli.utils import create_if_not_exists, get_day_name, get_folder_path


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
        click.secho(f"Successfully downloaded input file for day {day}", fg="green")
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


def save_input(day: int) -> None:
    day_name = get_day_name(day)
    folder_path = get_folder_path(day_name)
    file = folder_path / "input.txt"
    input = "" if file.exists() else download_input(day)

    create_if_not_exists(
        file,
        text=input,
        created_msg=f"Created input file for day {day}",
        exists_msg=f"Input file for day {day} already exists, skipping",
    )
    create_if_not_exists(
        folder_path / "test_input.txt",
        text="",
        created_msg=f"Created test input file for day {day}",
        exists_msg=f"Test input file for day {day} already exists, skipping",
    )
