from datetime import datetime

import pytz

from cli.config import YEAR


def get_aoc_timezone():
    return pytz.timezone("America/New_York")


def get_default_day() -> dict:
    current_date = datetime.now(get_aoc_timezone())
    if current_date.year == YEAR and current_date.month == 12:
        return {"default": current_date.day, "required": False}
    return {"default": None, "required": True}


def get_day_name(day: int) -> str:
    return f"day{day:0>2}"
