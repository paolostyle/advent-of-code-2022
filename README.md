# Advent of Code 2022

...this time in Python because I'm lazy, but I guess I made a cool CLI so maybe not _that_ lazy

## Setup

Poetry 1.2+ is required.

`poetry install`

`poetry shell`

## Create template

`aoc create --day 1`

`--day` is optional, running only `aoc create` will create files for current day,
if it's December 2022, of course.

## Run

`aoc run --day 1`

Similar as above, `--day` is optional with the same rules. You can also pass `--test` to run it with `test_input.txt` file located in the day's folder or `--test filename.txt` to run it with input located in `filename.txt`.
