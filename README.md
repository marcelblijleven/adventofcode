# Advent of Code ⭐️
[![Stars collected](https://shields.io/static/v1?label=stars%20collected&message=0&color=yellow)]()

Collection of my Advent of Code solutions in a slightly overkill project setup 👻.

## Features ✨
- Solutions are timed with the help of a decorator using `time.perf_counter`
- Solution and time are printed to console using the `rich` package with `truecolor`
- Automatic listing of completed solutions in the README
- Automatic changelog, using semantic versioning and the conventional commit specification
- A badge that is updated automatically with the amount of stars I've collected
- Pip installable (`pip install -e .`) with:
  - A generate-readme script, which updates the readme
  - A run-all script, which dynamically calls every solution in every `adventofcode.year_*.day_*` module
- Type checked (`mypy`) and linted (`flake8`)
- Tested against multiple python versions using `tox` on each push to master and pull request

<!-- start completed section -->

<!-- end completed section -->


**Note**: _not all years/solutions have been migrated yet from my previous repositories_
