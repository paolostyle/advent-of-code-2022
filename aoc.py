#!/usr/bin/env python
from pathlib import Path
import click
import importlib
import time


@click.group()
def cli():
    pass


@click.command()
@click.option("--day", help="AoC 2022 day file to run", required=True)
@click.option("--test", is_flag=True, help="Use default")
def run(day, test):
    folder = "test_inputs" if test is True else "inputs"
    input = Path(f"advent_of_code_2022/{folder}/day{day:0>2}.txt").read_text()
    module = importlib.import_module(f"advent_of_code_2022.solutions.day{day:0>2}")

    start_time = time.time()

    print(f"Part 1: {module.part_1(input)}")
    print(f"Part 2: {module.part_2(input)}")

    exec_time = time.time() - start_time
    print(f"Execution time: {exec_time:.5f}s")


@click.command()
@click.option("--day", help="AoC 2022 day", required=True)
def create(day):
    starting_code = """def part_1(input: str):
    pass


def part_2(input: str):
    pass
    """

    input_path = Path(f"advent_of_code_2022/inputs/day{day:0>2}.txt")
    if not input_path.exists():
        input_path.write_text("")
        click.echo(f"Created input file for day {day}")
    else:
        click.echo(f"Input file for day {day} already exists, skipping")

    test_input_path = Path(f"advent_of_code_2022/test_inputs/day{day:0>2}.txt")
    if not test_input_path.exists():
        test_input_path.write_text("")
        click.echo(f"Created test input file for day {day}")
    else:
        click.echo(f"Test input file for day {day} already exists, skipping")

    solution_path = Path(f"advent_of_code_2022/solutions/day{day:0>2}.py")
    if not solution_path.exists():
        solution_path.write_text(starting_code)
        click.echo(f"Created initial solution file for day {day}")
    else:
        click.echo(f"Solution file for day {day} already exists, skipping")

    click.echo("Done!")


cli.add_command(run)
cli.add_command(create)

if __name__ == "__main__":
    cli()
