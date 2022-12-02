#!/usr/bin/env python
from datetime import datetime
import os
from pathlib import Path
import sys
import textwrap
import click
import importlib
import time
import pytz
import requests
import pyperclip

YEAR = 2022
MODULE_NAME = f"advent_of_code_{YEAR}"


@click.group()
def cli():
    pass


def get_default_day():
    current_date = datetime.now(pytz.timezone("America/New_York"))
    if current_date.year == YEAR and current_date.month == 12:
        return current_date.day
    return None


DEFAULT_DAY = get_default_day()


@click.command()
@click.option(
    "--day",
    help="Day to run",
    default=DEFAULT_DAY,
    required=DEFAULT_DAY is None,
)
@click.option("--test", is_flag=True, help="")
def run(day: int, test: bool):
    try:
        folder = "test_inputs" if test is True else "inputs"
        input = Path(f"{MODULE_NAME}/{folder}/day{day:0>2}.txt").read_text()
    except FileNotFoundError:
        self_name = os.path.basename(__file__)

        click.secho("ERROR: ", fg="red", bold=True, nl=False)
        click.secho("No input file found! Run ", fg="red", nl=False)
        click.secho(
            f"./{self_name} create --day {day} ",
            fg="red",
            bold=True,
            nl=False,
        )
        click.secho("and try again.", fg="red")

        sys.exit(1)

    module = importlib.import_module(f"{MODULE_NAME}.solutions.day{day:0>2}")

    start_time = time.time()
    part_1 = module.part_1(input)
    part_2 = module.part_2(input)
    exec_time = time.time() - start_time

    click.secho(f"** DAY {day} **", bold=True, fg="blue")
    click.secho("Part 1: ", fg="green", nl=False)
    click.secho(part_1, bold=True)
    click.secho("Part 2: ", fg="green", nl=False)
    click.secho(part_2, bold=True)
    click.secho("Execution time: ", fg="magenta", nl=False)
    click.secho(f"{exec_time:.5f}s", fg="magenta", bold=True)

    pyperclip.copy(part_1 if part_2 is None else part_2)


def get_input(day: int):
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


@click.command()
@click.option(
    "--day",
    help="Day to create",
    default=DEFAULT_DAY,
    required=DEFAULT_DAY is None,
)
def create(day):
    starting_code = textwrap.dedent(
        """
        def part_1(input: str):
            pass


        def part_2(input: str):
            pass
        """
    ).lstrip()

    input_path = Path(f"{MODULE_NAME}/inputs/day{day:0>2}.txt")
    if not input_path.exists():
        input_path.write_text(get_input(day))
        click.secho(f"Created input file for day {day}", fg="green")
    else:
        click.secho(f"Input file for day {day} already exists, skipping", fg="yellow")

    test_input_path = Path(f"{MODULE_NAME}/test_inputs/day{day:0>2}.txt")
    if not test_input_path.exists():
        test_input_path.write_text("")
        click.secho(f"Created test input file for day {day}", fg="green")
    else:
        click.secho(
            f"Test input file for day {day} already exists, skipping", fg="yellow"
        )

    solution_path = Path(f"{MODULE_NAME}/solutions/day{day:0>2}.py")
    if not solution_path.exists():
        solution_path.write_text(starting_code)
        click.secho(f"Created initial solution file for day {day}", fg="green")
    else:
        click.secho(
            f"Solution file for day {day} already exists, skipping", fg="yellow"
        )

    click.secho("Done!", bold=True, fg="green")


cli.add_command(run)
cli.add_command(create)

if __name__ == "__main__":
    cli()
