import time
from pathlib import Path
from typing import Optional

import click
import pyperclip

from cli.config import MODULE_NAME
from cli.utils import (
    create_if_not_exists,
    get_day_name,
    get_default_day,
    download_input,
    load_input_file,
    load_module,
    starting_code,
)


@click.group()
def cli():
    pass


@cli.command()
@click.option("--day", help="Day to run", **get_default_day())
@click.option(
    "--test",
    "test_input_file",
    is_flag=False,
    flag_value="test_input.txt",
    default=None,
    help="Run with test data",
)
def run(day: int, test_input_file: Optional[str]):
    input = load_input_file(day, test_input_file)
    module = load_module(day)

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

    if any([part_1, part_2]):
        pyperclip.copy(part_1 if part_2 is None else part_2)


@cli.command()
@click.option("--day", help="Day to create", **get_default_day())
def create(day: int):
    day_name = get_day_name(day)

    folder_path = Path(f"{MODULE_NAME}/{day_name}")
    folder_path.mkdir(exist_ok=True)

    create_if_not_exists(folder_path / Path("__init__.py"), text="")
    create_if_not_exists(
        folder_path / Path("input.txt"),
        text=download_input(day),
        created_msg=f"Created input file for day {day}",
        exists_msg=f"Input file for day {day} already exists, skipping",
    )
    create_if_not_exists(
        folder_path / Path("test_input.txt"),
        text="",
        created_msg=f"Created test input file for day {day}",
        exists_msg=f"Test input file for day {day} already exists, skipping",
    )
    create_if_not_exists(
        folder_path / Path(f"{day_name}.py"),
        text=starting_code,
        created_msg=f"Created initial solution file for day {day}",
        exists_msg=f"Solution file for day {day} already exists, skipping",
    )

    click.secho("Done!", bold=True, fg="green")
