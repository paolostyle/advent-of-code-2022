from pathlib import Path


def load_input(day: int, test=False) -> str:
    folder = "inputs" if test is True else "test_inputs"
    return Path(f"advent_of_code_2022/{folder}/day{day:02}.txt").read_text()
