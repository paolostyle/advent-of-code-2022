import textwrap
from datetime import datetime

import click

from cli.config import YEAR
from cli.utils import get_aoc_timezone

starting_code = textwrap.dedent(
    """
    def part_1(input: str) -> int:
        pass


    def part_2(input: str) -> int:
        pass
    """
).lstrip()


def open_day_description(day: int) -> None:
    if datetime.now(get_aoc_timezone()) > datetime(
        YEAR, 12, day, tzinfo=get_aoc_timezone()
    ):
        click.launch(f"https://adventofcode.com/{YEAR}/day/{day}")
