## v2.0.0 (2024-12-03)

### Feat

- add 2024 day 1 part 1 & 2
- add 2023 day 09
- add 2023 day 08 part 02
- add 2023 day 07 part 01
- add 2023 day 7 part 1 & 2
- add 2023 day 6 part 2
- add 2023 day 06 part 1
- add 2023 day 05 part 2
- add 2023 day 05 part 1
- add 2023 day 4 part 2
- add 2023 day 4 part 1
- add 2023 day 03

### Fix

- send user agent with input retrieval request
- add return value
- remove extra number in range
- formatting
- type hints


- migrate to poetry

## v1.10.0 (2023-12-02)

### Feat

- add 2023 day 2 part 2
- add 2023 day 2 part 1

### Fix

- apply linting outputs

## v1.9.0 (2023-12-02)

### Feat

- add 2023 day 2
- add 2023 day 1

## v1.8.2 (2022-12-11)

## v1.8.1 (2022-12-11)

## v1.8.0 (2022-12-07)

### Feat

- add registry

### Fix

- mypy issues
- mypy errors
- flake8 errors
- flake8 and black
- don't use None as default for str type

### Refactor

- use httpx instead of requests and add docstrings

## v1.7.0 (2021-12-17)

### Feat

- add grid helpers
- add dark and light mode svg
- add dark and light mode svg
- gather average solution durations
- add dynamic star counter svg

### Fix

- fix issue where both light and dark images would show side by side
- remove multiprocessing from benchmarks to prevent adding overhead

## v1.5.0 (2021-12-10)

### Feat

- make solution timer return duration when running benchmarks
- replace solution lists with tables
- add benchmarks

### Fix

- checkout git repository in release.yaml

## v1.4.2 (2021-12-09)

## v1.4.1 (2021-12-09)

## v1.4.0 (2021-12-08)

### Feat

- make test template use test input by default
- add math helpers
- add test template to add-day script

### Fix

- fix incorrect default data for filter list
- fix incorrect turn waypoint function
- fix incompatible types in assignment
- fix incorrect day replacement in test template

## v1.3.2 (2021-12-01)

### Fix

- display correct amount of microseconds in solution timer
- remove hardcoded day - year from get_input function

## v1.3.1 (2021-11-30)

### Fix

- flake 8 issues

## v1.3.0 (2021-11-30)

### Feat

- add memoization decorator
- add profiler decorator
- add clean-repo script
- add add-day script
- add codecov reports to tox

## v1.2.0 (2021-11-21)

### Feat

- add template for day

### Fix

- strip _year suffix from day in clean_day
- check for None explicitly to prevent incorrect behaviour when answer is 0
- make all files unique to prevent issues in the global import namespace
- flake8 and mypy issues
- mypy and flake8 issues

## v1.1.0 (2021-11-19)

### Feat

- add run-all script
- modify solution timer output when run-all is used
- add functions to download input from aoc website using session cookie
- add run-all script
- add module helpers
- add function to retrieve input as string

### Refactor

- use GenericAlias for long layout type hint
- move console to own file
- move helper functions out of generate_readme.py and add emoji

## v1.0.0 (2021-11-18)

### Feat

- automatically update amount of stars collected
- add input helper functions

### Fix

- don't commit when nothing to commit
- **ci**: fix incorrect indentation
