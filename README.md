# Advent of Code ⭐️
[![Stars collected](https://shields.io/static/v1?label=stars%20collected&message=114&color=yellow)]()
[![codecov](https://codecov.io/gh/marcelblijleven/adventofcode/branch/master/graph/badge.svg?token=jZ2TgfyltM)](https://codecov.io/gh/marcelblijleven/adventofcode)
[![tests](https://github.com/marcelblijleven/adventofcode/actions/workflows/tests.yaml/badge.svg)](https://github.com/marcelblijleven/adventofcode)
[![version](https://img.shields.io/github/v/release/marcelblijleven/adventofcode.svg)](https://github.com/marcelblijleven/adventofcode/releases)

![advent of code](./image_dark.svg#gh-dark-mode-only)
![advent of code](./image_light.svg#gh-light-mode-only)

Collection of my Advent of Code solutions in an overkill project setup 👻🎄.

## Features ✨
- Solutions are timed with the help of a decorator using `time.perf_counter`
- Solution and time are printed to console using the `rich` package with `truecolor`
- Solution profiler decorator using `Cprofile` and `pstats`
- Automatic listing of [completed solutions](#completed-) in the README
- [Automatic changelog](CHANGELOG.md), using semantic versioning and the conventional commit specification
- A badge that is updated automatically with the amount of stars I've collected
- A svg image that is updated automatically with the amount of stars in the style of Advent of Code
  - Has a dark mode and light mode version which are visible only when their respective mode is used by the user
  - Has an animated star emoji which helps the Elves save Christmas
- Pip installable (`pip install -e .`) with:
  - A `generate-readme` script, which updates the readme
  - A `generate-benchmarks` script, which runs all solutions and saves the duration of each solution to [these tables](#benchmarks-)
  - A `run-all` script, which dynamically calls every solution in every `adventofcode.year_*.day_*` module
  - An `add-day` script, which add a solution day file using a template and downloads the input data from the AOC site automatically
- Type checked (`mypy`) and linted (`flake8`)
- Tested against multiple python versions using `tox` on each push to master and pull request

<!-- start completed section -->
## Completed ⭐️
### 2015
<details><summary>Solutions for 2015</summary>
<p>

| day   | part one | part two |
| :---: | :------: | :------: |
| 01 | ⭐️ | ⭐️ |
| 02 | ⭐️ | ⭐️ |
| 03 | ⭐️ | ⭐️ |
| 04 | ⭐️ | ⭐️ |
| 05 | ⭐️ | ⭐️ |
| 06 | ⭐️ | ⭐️ |
| 07 | ⭐️ | ⭐️ |
| 08 | ⭐️ | ⭐️ |
| 09 | ⭐️ | ⭐️ |
| 10 | ⭐️ | ⭐️ |
| 11 | ⭐️ | ⭐️ |
| 12 | ⭐️ | ⭐️ |
| 13 | ⭐️ | ⭐️ |
| 14 | ⭐️ | ⭐️ |
| 15 | ⭐️ | ⭐️ |
| 16 | ⭐️ | ⭐️ |
| 17 | ⭐️ | ⭐️ |
| 18 | ⭐️ | ⭐️ |
| 19 | ⭐️ | ⭐️ |
| 20 | ⭐️ | ⭐️ |
| 21 | ⭐️ | ⭐️ |
| 22 | ⭐️ | ⭐️ |
| 23 | ⭐️ | ⭐️ |
| 24 | ⭐️ | ⭐️ |
| 25 | ⭐️ | ⭐️ |

</p>
</details>

### 2020
<details><summary>Solutions for 2020</summary>
<p>

| day   | part one | part two |
| :---: | :------: | :------: |
| 01 | ⭐️ | ⭐️ |
| 02 | ⭐️ | ⭐️ |
| 03 | ⭐️ | ⭐️ |
| 04 | ⭐️ | ⭐️ |
| 05 | ⭐️ | ⭐️ |
| 06 | ⭐️ | ⭐️ |
| 07 | ⭐️ | ⭐️ |
| 08 | ⭐️ | ⭐️ |
| 09 | ⭐️ | ⭐️ |
| 10 | ⭐️ | ⭐️ |
| 11 | ⭐️ | ⭐️ |
| 12 | ⭐️ | ⭐️ |
| 13 | ⭐️ | ⭐️ |
| 14 | ⭐️ | ⭐️ |
| 15 | ⭐️ | ⭐️ |
| 16 | ⭐️ | ⭐️ |

</p>
</details>

### 2021
<details><summary>Solutions for 2021</summary>
<p>

| day   | part one | part two |
| :---: | :------: | :------: |
| 01 | ⭐️ | ⭐️ |
| 02 | ⭐️ | ⭐️ |
| 03 | ⭐️ | ⭐️ |
| 04 | ⭐️ | ⭐️ |
| 05 | ⭐️ | ⭐️ |
| 06 | ⭐️ | ⭐️ |
| 07 | ⭐️ | ⭐️ |
| 08 | ⭐️ | ⭐️ |
| 09 | ⭐️ | ⭐️ |
| 10 | ⭐️ | ⭐️ |
| 11 | ⭐️ | ⭐️ |
| 12 | ⭐️ | ⭐️ |
| 13 | ⭐️ | ⭐️ |
| 14 | ⭐️ | ⭐️ |
| 15 | ⭐️ | ⭐️ |
| 16 | ⭐️ | ⭐️ |

</p>
</details>


<!-- end completed section -->

<!-- start benchmark section -->
## Benchmarks 🚀
### 2015
<details><summary>Benchmarks for 2015</summary>
<p>

|  day  | part  | duration |
| :---: | :---: | -------: |
| 01 | part one | 1.06 ms |
| 01 | part two | 0.45 ms |
| 02 | part one | 5.25 ms |
| 02 | part two | 4.74 ms |
| 03 | part one | 7.09 ms |
| 03 | part two | 9.96 ms |
| 04 | part one | 409.48 ms |
| 04 | part two | 6539.61 ms |
| 05 | part one | 2.17 ms |
| 05 | part two | 2.89 ms |
| 06 | part one | 8520.83 ms |
| 06 | part two | 9749.57 ms |
| 07 | part one | 2.46 ms |
| 07 | part two | 4.18 ms |
| 08 | part one | 2.04 ms |
| 08 | part two | 0.51 ms |
| 09 | part one | 131.21 ms |
| 09 | part two | 137.00 ms |
| 10 | part one | 434.10 ms |
| 10 | part two | 6609.51 ms |
| 11 | part one | 0.02 ms |
| 11 | part two | 0.02 ms |
| 12 | part one | 2.12 ms |
| 12 | part two | 1.40 ms |
| 13 | part one | 159.35 ms |
| 13 | part two | 1398.87 ms |
| 14 | part one | 29.53 ms |
| 14 | part two | 32.03 ms |
| 15 | part one | 1089.26 ms |
| 15 | part two | 403.07 ms |
| 16 | part one | 1.33 ms |
| 16 | part two | 1.36 ms |
| 17 | part one | 213.67 ms |
| 17 | part two | 152.82 ms |
| 18 | part one | 4531.14 ms |
| 18 | part two | 4718.72 ms |
| 19 | part one | 5.64 ms |
| 19 | part two | 0.30 ms |
| 20 | part one | 6324.19 ms |
| 20 | part two | 2048.20 ms |
| 21 | part one | 8.73 ms |
| 21 | part two | 7.35 ms |
| 22 | part one | 351.36 ms |
| 22 | part two | 246.51 ms |
| 23 | part one | 1.58 ms |
| 23 | part two | 1.80 ms |
| 24 | part one | 100.49 ms |
| 24 | part two | 3.78 ms |
| 25 | part one | 4252.91 ms |
| 25 | part two | 0.00 ms |

</p>
</details>

### 2020
<details><summary>Benchmarks for 2020</summary>
<p>

|  day  | part  | duration |
| :---: | :---: | -------: |
| 01 | part one | 0.16 ms |
| 01 | part two | 161.52 ms |
| 02 | part one | 5.24 ms |
| 02 | part two | 5.44 ms |
| 03 | part one | 0.22 ms |
| 03 | part two | 0.68 ms |
| 05 | part one | 13.53 ms |
| 05 | part two | 4.07 ms |
| 05 | part one binary version | 0.53 ms |
| 06 | part one | 1.41 ms |
| 06 | part two | 1.61 ms |
| 07 | part one | 120.07 ms |
| 07 | part two | 1.63 ms |
| 08 | part one | 0.63 ms |
| 08 | part two | 34.73 ms |
| 09 | part one | 1.09 ms |
| 09 | part two | 1352.88 ms |
| 10 | part one | 0.04 ms |
| 10 | part two | 0.07 ms |
| 11 | part one | 4940.09 ms |
| 11 | part two | 4574.01 ms |
| 12 | part one | 0.88 ms |
| 12 | part two | 0.77 ms |
| 13 | part one | 0.35 ms |
| 13 | part two | 0.15 ms |
| 14 | part one | 2.99 ms |
| 14 | part two | 446.27 ms |
| 15 | part one | 0.32 ms |
| 15 | part two | 9343.14 ms |
| 16 | part one | 2.88 ms |
| 16 | part two | 0.01 ms |

</p>
</details>

### 2021
<details><summary>Benchmarks for 2021</summary>
<p>

|  day  | part  | duration |
| :---: | :---: | -------: |
| 01 | part one | 0.37 ms |
| 01 | part two | 1.98 ms |
| 01 | part two reuse part one | 1.19 ms |
| 02 | part one | 0.78 ms |
| 02 | part two | 1.18 ms |
| 03 | part one | 2.06 ms |
| 03 | part two | 5.28 ms |
| 04 | part one | 18.84 ms |
| 04 | part two | 50.88 ms |
| 05 | part one | 65.13 ms |
| 05 | part two | 114.93 ms |
| 06 | part one | 0.10 ms |
| 06 | part two | 0.17 ms |
| 06 | part two faster | 0.13 ms |
| 07 | part one | 0.45 ms |
| 07 | part two | 0.82 ms |
| 08 | part one | 0.38 ms |
| 08 | part two | 3.71 ms |
| 09 | part one | 16.21 ms |
| 09 | part two | 24.48 ms |
| 09 | part two async | 43.88 ms |
| 09 | part two mp | 282.40 ms |
| 10 | part one | 1.80 ms |
| 10 | part two | 4.08 ms |
| 11 | part one | 13.46 ms |
| 11 | part two | 32.05 ms |
| 12 | part one | 31.24 ms |
| 12 | part two | 916.11 ms |
| 13 | part one | 1.31 ms |
| 13 | part two | 2.13 ms |

</p>
</details>

<!-- end benchmark section --> 

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
