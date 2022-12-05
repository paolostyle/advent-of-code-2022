from datetime import datetime
from pathlib import Path

import pytz
import tomllib

now = datetime.now(pytz.timezone("America/New_York"))

YEAR = now.year - 1 if now.month < 12 else now.year
MODULE_NAME = f"advent_of_code_{YEAR}"
COOKIE_PATH = "./cookie"

pyproject = Path("pyproject.toml")

if pyproject.exists():
    with pyproject.open(mode="rb") as file:
        data = tomllib.load(file)
        aoc_config = data.get("tool", {}).get("aoc")
        if aoc_config:
            YEAR = aoc_config.get("year", YEAR)
            MODULE_NAME = aoc_config.get("module-name", MODULE_NAME)
            COOKIE_PATH = aoc_config.get("cookie-path", COOKIE_PATH)
