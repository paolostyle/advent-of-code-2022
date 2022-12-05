import importlib
import os
import sys
import time
from pathlib import Path
from types import ModuleType
from typing import Any, Optional

import click
import pyperclip  # type: ignore

from cli.config import MODULE_NAME
from cli.utils import get_day_name


def load_input_file(day: int, test_input_file: Optional[str]) -> str:
    day_name = get_day_name(day)

    try:
        input_file = test_input_file or "input.txt"
        path_to_file = Path(MODULE_NAME) / day_name / input_file
        return path_to_file.read_text()
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


def load_module(day: int) -> ModuleType:
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


def run_code(day: int, test_input_file: Optional[str]) -> tuple[Any, Any, float]:
    input = load_input_file(day, test_input_file)
    module = load_module(day)

    start_time = time.perf_counter_ns()
    part_1 = module.part_1(input)
    part_2 = module.part_2(input)
    exec_time = (time.perf_counter_ns() - start_time) / pow(10, 6)

    return (part_1, part_2, exec_time)


def print_results(day: int, part_1: Any, part_2: Any, exec_time: float):
    click.secho(f"** DAY {day} **", bold=True, fg="blue")
    click.secho("Part 1: ", fg="green", nl=False)
    click.secho(part_1, bold=True)
    click.secho("Part 2: ", fg="green", nl=False)
    click.secho(part_2, bold=True)
    click.secho("Execution time: ", fg="magenta", nl=False)
    click.secho(f"{exec_time:.5f}ms", fg="magenta", bold=True)


def copy_result_to_clipboard(part_1: Any, part_2: Any):
    if any([part_1, part_2]):
        pyperclip.copy(part_1 if part_2 is None else part_2)
