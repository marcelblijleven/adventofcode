# Advent of Code ⭐️
[![Stars collected](https://shields.io/static/v1?label=stars%20collected&message=129&color=yellow)]()
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
- Tested against multiple python versions on each push to master and pull request

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
| 17 | ⭐️ | ⭐️ |
| 18 | ⭐️ | ⭐️ |
| 19 | ⭐️ | ⭐️ |
| 20 | ⭐️ | ⭐️ |
| 21 | ⭐️ | ⭐️ |
| 22 | ⭐️ | ⭐️ |
| 25 | ⭐️ | – |

</p>
</details>

### 2022
<details><summary>Solutions for 2022</summary>
<p>

| day   | part one | part two |
| :---: | :------: | :------: |
| 01 | ⭐️ | ⭐️ |

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
| 01 | part one | 0.59 ms |
| 01 | part two | 0.20 ms |
| 02 | part one | 2.45 ms |
| 02 | part two | 2.31 ms |
| 03 | part one | 4.38 ms |
| 03 | part two | 5.65 ms |
| 04 | part one | 157.22 ms |
| 04 | part two | 5107.37 ms |
| 05 | part one | 2.69 ms |
| 05 | part two | 3.08 ms |
| 06 | part one | 8926.05 ms |
| 06 | part two | 9819.37 ms |
| 07 | part one | 2.34 ms |
| 07 | part two | 4.09 ms |
| 08 | part one | 1.89 ms |
| 08 | part two | 0.54 ms |
| 09 | part one | 132.76 ms |
| 09 | part two | 132.34 ms |
| 10 | part one | 440.87 ms |
| 10 | part two | 6289.21 ms |
| 11 | part one | 0.02 ms |
| 11 | part two | 0.02 ms |
| 12 | part one | 1.56 ms |
| 12 | part two | 1.38 ms |
| 13 | part one | 148.84 ms |
| 13 | part two | 1442.36 ms |
| 14 | part one | 37.71 ms |
| 14 | part two | 43.86 ms |
| 15 | part one | 1019.33 ms |
| 15 | part two | 382.58 ms |
| 16 | part one | 2.15 ms |
| 16 | part two | 1.93 ms |
| 17 | part one | 212.52 ms |
| 17 | part two | 132.00 ms |
| 18 | part one | 4385.13 ms |
| 18 | part two | 4604.23 ms |
| 19 | part one | 5.54 ms |
| 19 | part two | 0.43 ms |
| 20 | part one | 6489.39 ms |
| 20 | part two | 2005.31 ms |
| 21 | part one | 9.00 ms |
| 21 | part two | 9.66 ms |
| 22 | part one | 341.50 ms |
| 22 | part two | 266.26 ms |
| 23 | part one | 0.99 ms |
| 23 | part two | 1.29 ms |
| 24 | part one | 112.10 ms |
| 24 | part two | 4.55 ms |
| 25 | part one | 4324.46 ms |
| 25 | part two | 0.00 ms |

</p>
</details>

### 2020
<details><summary>Benchmarks for 2020</summary>
<p>

|  day  | part  | duration |
| :---: | :---: | -------: |
| 01 | part one | 0.28 ms |
| 01 | part two | 164.37 ms |
| 02 | part one | 6.21 ms |
| 02 | part two | 5.05 ms |
| 03 | part one | 0.15 ms |
| 03 | part two | 0.63 ms |
| 05 | part one | 13.86 ms |
| 05 | part two | 4.13 ms |
| 05 | part one binary version | 0.65 ms |
| 06 | part one | 1.50 ms |
| 06 | part two | 1.68 ms |
| 07 | part one | 121.85 ms |
| 07 | part two | 1.65 ms |
| 08 | part one | 0.72 ms |
| 08 | part two | 34.08 ms |
| 09 | part one | 1.01 ms |
| 09 | part two | 1347.52 ms |
| 10 | part one | 0.04 ms |
| 10 | part two | 0.07 ms |
| 11 | part one | 4904.47 ms |
| 11 | part two | 4403.77 ms |
| 12 | part one | 0.95 ms |
| 12 | part two | 0.80 ms |
| 13 | part one | 0.27 ms |
| 13 | part two | 0.18 ms |
| 14 | part one | 2.84 ms |
| 14 | part two | 471.49 ms |
| 15 | part one | 0.48 ms |
| 15 | part two | 9689.39 ms |
| 16 | part one | 3.57 ms |
| 16 | part two | 15.52 ms |

</p>
</details>

### 2021
<details><summary>Benchmarks for 2021</summary>
<p>

|  day  | part  | duration |
| :---: | :---: | -------: |
| 01 | part one | 0.46 ms |
| 01 | part two | 1.82 ms |
| 01 | part two reuse part one | 1.31 ms |
| 02 | part one | 1.02 ms |
| 02 | part two | 0.89 ms |
| 03 | part one | 1.66 ms |
| 03 | part two | 4.75 ms |
| 04 | part one | 19.02 ms |
| 04 | part two | 66.03 ms |
| 05 | part one | 61.24 ms |
| 05 | part two | 117.13 ms |
| 06 | part one | 0.10 ms |
| 06 | part two | 0.17 ms |
| 06 | part two faster | 0.14 ms |
| 07 | part one | 0.40 ms |
| 07 | part two | 0.95 ms |
| 08 | part one | 0.32 ms |
| 08 | part two | 2.88 ms |
| 09 | part one | 15.73 ms |
| 09 | part two | 22.42 ms |
| 09 | part two async | 40.79 ms |
| 09 | part two mp | 214.77 ms |
| 10 | part one | 1.91 ms |
| 10 | part two | 3.85 ms |
| 11 | part one | 12.64 ms |
| 11 | part two | 29.38 ms |
| 12 | part one | 31.00 ms |
| 12 | part two | 955.99 ms |
| 13 | part one | 0.99 ms |
| 13 | part two | 1.93 ms |
| 14 | part one | 0.74 ms |
| 14 | part two | 3.09 ms |
| 15 | part one | 45.01 ms |
| 15 | part two | 1465.20 ms |
| 16 | part one | 1.08 ms |
| 16 | part two | 1.07 ms |
| 17 | part one | 281.08 ms |
| 17 | part two | 2591.46 ms |
| 17 | part one quick maths | 0.01 ms |

</p>
</details>

<!-- end benchmark section --> 

## Decorators
What's Christmas without decorations? 🎄

### Solution timer
The solution timer times the solution using `time.perf_counter` and outputs the answer and the duration to the console

Example:
```python
@register_solution(2015, 9, 1)  # year, day, part
def part_one(input_data: list[str]) -> int:
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
def part_one(input_data: list[str]) -> int:
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
