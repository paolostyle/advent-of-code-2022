from datetime import datetime
from pathlib import Path
from typing import Optional

import click
import pytz

from cli.config import MODULE_NAME, YEAR


def get_aoc_timezone():
    return pytz.timezone("America/New_York")


def get_default_day() -> dict:
    current_date = datetime.now(get_aoc_timezone())
    if current_date.year == YEAR and current_date.month == 12:
        return {"default": str(current_date.day), "required": False}
    return {"default": None, "required": True}


def get_day_name(day: int) -> str:
    return f"day{day:0>2}"


def create_if_not_exists(
    path: Path,
    text: str,
    created_msg: Optional[str] = None,
    exists_msg: Optional[str] = None,
) -> bool:
    if not path.exists():
        path.write_text(text)
        if created_msg:
            click.secho(created_msg, fg="green")
        return True
    elif exists_msg:
        click.secho(exists_msg, fg="yellow")

    return False


def get_folder_path(day_name: str) -> Path:
    folder_path = Path(f"{MODULE_NAME}") / day_name
    folder_path.mkdir(exist_ok=True)

    create_if_not_exists(folder_path / Path("__init__.py"), text="")

    return folder_path


def parse_range(days: str) -> list[int]:
    result: list[int] = []

    for part in days.split(","):
        if "-" in part:
            a, b = [int(day) for day in part.split("-")]
            result.extend(range(a, b + 1))
        else:
            a = int(part)
            result.append(a)

    return result
