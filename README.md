# Advent of Code 2022

...this time in Python because I'm lazy, but I guess I made a cool CLI so maybe not _that_ lazy

## Setup

Poetry 1.2+ and Python 3.11 is required. You can (and should) use `pyenv`.

`poetry install`

`poetry shell`

## Cookie setup

The CLI can download the input for your AoC account. You have to get the session token manually after you log in on the AoC website
and put it in `cookie` file in the root directory. You can name the file differently or put it somewhere else, too, but you need to configure it
in `pyproject.toml`, e.g. if you want to have it in a `session.txt` file, configure it like this:

```
[tool.aoc]
cookie-path = "./session.txt"
```

## Create template

`aoc create [days]`

The argument is optional, running only `aoc create` will create files for current day,
if it's December 2022, of course. You can pass ranges and individual items, e.g. `aoc create 3,5-6,8-9`.

This will:

- create a folder for a given day (with `__init__.py` file)
- creates a placeholder for the solution (two empty functions, one for each part)
- if possible, fetches the input file from the website (if the cookie setup is configured)
- creates empty `test_input.txt` file for experimenting
- if the placeholder did not exist or `--open` is passed, it opens the AoC website with the instruction

## Run

`aoc run [day]`

Similarly, `[day]` is optional and the same rules apply. You can also pass `--test` to run it
with `test_input.txt` file located in the day's folder or `--test filename.txt`
to run it with input located in `filename.txt`.
