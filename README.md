# Advent of Code ⭐️
[![Stars collected](https://shields.io/static/v1?label=stars%20collected&message=76&color=yellow)]()
[![codecov](https://codecov.io/gh/marcelblijleven/adventofcode/branch/master/graph/badge.svg?token=jZ2TgfyltM)](https://codecov.io/gh/marcelblijleven/adventofcode)
[![tests](https://github.com/marcelblijleven/adventofcode/actions/workflows/tests.yaml/badge.svg)](https://github.com/marcelblijleven/adventofcode)
[![version](https://img.shields.io/github/v/release/marcelblijleven/adventofcode.svg)](https://github.com/marcelblijleven/adventofcode/releases)

Collection of my Advent of Code solutions in an overkill project setup 👻🎄.

## Features ✨
- Solutions are timed with the help of a decorator using `time.perf_counter`
- Solution and time are printed to console using the `rich` package with `truecolor`
- Solution profiler decorator using `Cprofile` and `pstats`
- Automatic listing of completed solutions in the README
- Automatic changelog, using semantic versioning and the conventional commit specification
- A badge that is updated automatically with the amount of stars I've collected
- Pip installable (`pip install -e .`) with:
  - A `generate-readme` script, which updates the readme
  - A `run-all` script, which dynamically calls every solution in every `adventofcode.year_*.day_*` module
  - An `add-day` script, which add a solution day file using a template and downloads the input data from the AOC site automatically
- Type checked (`mypy`) and linted (`flake8`)
- Tested against multiple python versions using `tox` on each push to master and pull request

<!-- start completed section -->
## Completed ⭐️
### 2015
- day 01: part one ⭐️, part two ⭐️
- day 02: part one ⭐️, part two ⭐️
- day 03: part one ⭐️, part two ⭐️
- day 04: part one ⭐️, part two ⭐️
- day 05: part one ⭐️, part two ⭐️
- day 06: part one ⭐️, part two ⭐️
- day 07: part one ⭐️, part two ⭐️
- day 08: part one ⭐️, part two ⭐️
- day 09: part one ⭐️, part two ⭐️
- day 10: part one ⭐️, part two ⭐️
- day 11: part one ⭐️, part two ⭐️
- day 12: part one ⭐️, part two ⭐️
- day 13: part one ⭐️, part two ⭐️
- day 14: part one ⭐️, part two ⭐️
- day 15: part one ⭐️, part two ⭐️
- day 16: part one ⭐️, part two ⭐️
- day 17: part one ⭐️, part two ⭐️
- day 18: part one ⭐️, part two ⭐️
- day 19: part one ⭐️, part two ⭐️
- day 20: part one ⭐️, part two ⭐️
- day 21: part one ⭐️, part two ⭐️
- day 22: part one ⭐️, part two ⭐️
- day 23: part one ⭐️, part two ⭐️
- day 24: part one ⭐️, part two ⭐️
- day 25: part one ⭐️, part two ⭐️
### 2020
- day 01: part one ⭐️, part two ⭐️
- day 02: part one ⭐️, part two ⭐️
- day 03: part one ⭐️, part two ⭐️
- day 04: part one ⭐️, part two ⭐️
- day 05: part one ⭐️, part two ⭐️
- day 06: part one ⭐️, part two ⭐️
- day 07: part one ⭐️, part two ⭐️
- day 08: part one ⭐️, part two ⭐️
- day 09: part one ⭐️, part two ⭐️
- day 10: part one ⭐️, part two ⭐️
- day 11: part one ⭐️, part two ⭐️
### 2021
- day 01: part one ⭐️, part two ⭐️
- day 02: part one ⭐️, part two ⭐️

<!-- end completed section -->

## Decorators
What's Christmas without decorations? 🎄

### Solution timer
The solution timer times the solution using `time.perf_counter` and outputs the answer and the duration to the console

Example:
```python
@solution_timer(2015, 9, 1)  # year, day, part
def part_one(input_data: List[str]) -> int:
    ...
```

Output:
```text
2015 day 09 part 01: 251 in 0.1356 ms
```

### Solution profiler
The solution profiler runs the `cProfiler` against the solution and outputs the profiler stats using `pstats` to the console.
It takes an optional `amount` kwarg to set the amount of stats to display, and an optional `sort` kwarg to set the sorting to either
`time` or `cumulative`.

Example:
```python
@solution_profiler(2015, 9, 1)  # year, day, part
def part_one(input_data: List[str]) -> int:
    ...
```

Output:
```text
91416 function calls (90941 primitive calls) in 0.159 seconds

Ordered by: internal time
List reduced from 217 to 3 due to restriction <10>

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
    1    0.133    0.133    0.136    0.136 /Users/marcelblijleven/.../day_09_2015.py:39(_get_route_distances)
    1    0.012    0.012    0.015    0.015 /Users/marcelblijleven/.../day_09_2015.py:30(get_all_routes)
82182    0.006    0.000    0.006    0.000 {method 'append' of 'list' objects}
```

## Scripts
### add-day
The `add-day` script creates a file based on a 'solution day' template into the correct year module. If no input is found
for that day, it will automatically download the input and save it in the inputs directory. Note: this only works if the
session cookie is stored in `.session`. To get this value:
1. Go to the [AOC site](https://adventofcode.com).
2. Make sure you're logged in, every user has unique input data
3. View the cookies and copy the value of the `session` cookie.
4. Paste the cookie value into the `.session` file

Example:
```shell
(venv) add-day 2015 14
```

Output:
```text
(venv) [adventofcode] add-day 2015 14                                                                                                                                                                   master  ✗ ✭ ✱
Creating solution day file for year 2015 day 14
Wrote template to /Users/marcelblijleven/code/github.com/marcelblijleven/adventofcode/src/adventofcode/year_2015/day_14_2015.py
Input data already exists for year 2015 day 14, skipping download
```

### generate-readme
The `generate-readme` script dynamically searches for all solutions and writes them to the README.md file.
When a solution file has a function called `part_one`, it adds a star. When it has a function called `part_two`, it adds another
star. The `star counter` badge at the top of the README.md file is then updated with the total amount of stars found.

This script is only used in the Github workflow `update_readme.yml`, but can be run locally to using `generate-readme`

### clean-repo
The `clean-repo` script is used to delete all solutions and inputs from the project. This can be useful if you want to start over,
or if you've just forked this repo. The `clean-repo` command is run in 'dry run mode' by default, to disable it and actually
start deleting directories and files, use:

```shell
(venv) clean-repo --dry-run false 
```

**Note**: _not all years/solutions have been migrated yet from my previous repositories_
