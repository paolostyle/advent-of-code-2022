from typing import Optional

import click

from cli.create import open_day_description, starting_code
from cli.fetch import save_input
from cli.run import copy_result_to_clipboard, print_results, run_code
from cli.utils import (
    create_if_not_exists,
    get_day_name,
    get_default_day,
    get_folder_path,
    parse_range,
)


@click.group()
def cli():
    pass


@cli.command(help="Run the code for a given day")
@click.argument("day", type=int, **get_default_day())
@click.option(
    "--test",
    "test_input_file",
    is_flag=False,
    flag_value="test_input.txt",
    default=None,
    help="Runs the solution with data from test_input.txt or a custom file.",
)
def run(day: int, test_input_file: Optional[str]):
    part_1, part_2, exec_time = run_code(day, test_input_file)

    print_results(day, part_1, part_2, exec_time)

    copy_result_to_clipboard(part_1, part_2)


@cli.command(help="Scaffold module for a new AoC day")
@click.argument("days", **get_default_day())
@click.option("--open", help="Open instructions", is_flag=True, default=False)
def create(days: str, open: bool):
    for day in parse_range(days):
        day_name = get_day_name(day)
        folder_path = get_folder_path(day_name)

        was_solution_template_created = create_if_not_exists(
            folder_path / f"{day_name}.py",
            text=starting_code,
            created_msg=f"Created initial solution file for day {day}",
            exists_msg=f"Solution file for day {day} already exists, skipping",
        )

        save_input(day)

        click.secho("Done!", bold=True, fg="green")

        if was_solution_template_created or open:
            open_day_description(day)


@cli.command(help="Fetch and input for day")
@click.argument("days", **get_default_day())
def fetch(days: str):
    for day in parse_range(days):
        save_input(day)
