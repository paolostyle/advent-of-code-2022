from pathlib import Path
from typing import Optional

import click

from cli.create import (
    create_if_not_exists,
    download_input,
    get_folder_path,
    open_day_description,
    starting_code,
)
from cli.run import copy_result_to_clipboard, print_results, run_code
from cli.utils import get_day_name, get_default_day


@click.group()
def cli():
    pass


@cli.command(help="Run the code for a given day")
@click.option(
    "--day",
    help="Day to run. If ran during Advent of Code, by default it runs current day.",
    **get_default_day(),
)
@click.option(
    "--test",
    "test_input_file",
    is_flag=False,
    flag_value="test_input.txt",
    default=None,
    help="Pass without any arguments to run with precreated test_input.txt or pass filename.",
)
def run(day: int, test_input_file: Optional[str]):
    part_1, part_2, exec_time = run_code(day, test_input_file)

    print_results(day, part_1, part_2, exec_time)

    copy_result_to_clipboard(part_1, part_2)


@cli.command(help="Scaffold module for a new AoC day")
@click.option("--day", help="Day to create", **get_default_day())
def create(day: int):
    day_name = get_day_name(day)
    folder_path = get_folder_path(day_name)

    create_if_not_exists(
        folder_path / Path(f"{day_name}.py"),
        text=starting_code,
        created_msg=f"Created initial solution file for day {day}",
        exists_msg=f"Solution file for day {day} already exists, skipping",
    )
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

    click.secho("Done!", bold=True, fg="green")

    open_day_description(day)
