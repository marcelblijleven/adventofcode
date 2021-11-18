import ast
import os
import re
from typing import List, Dict

from adventofcode.config import ROOT_DIR


def generate_readme():
    path = os.path.join(ROOT_DIR, '../../README.md')
    readme_file = os.path.abspath(path)

    with open(readme_file) as f:
        current_readme = f.read()

    readme = _replace_between_tags(
        current_readme,
        _create_completed_text(),
        '<!-- start completed section -->',
        '<!-- end completed section -->'
    )

    readme = _update_stars(readme)

    with open(readme_file, 'w') as f:
        f.write(readme)


def _replace_between_tags(readme: str, content: str, start: str, end: str) -> str:
    content = '\n'.join([start, content, end])

    return re.sub(
        pattern=rf'{start}.*?{end}',
        repl=content,
        string=readme,
        flags=re.DOTALL,
    )


def _update_stars(readme: str) -> str:
    star_count = _count_stars()

    return re.sub(
        pattern=r'&message=\d+',
        repl=f'&message={star_count}',
        string=readme,
        flags=re.DOTALL,
    )


def _count_stars() -> int:
    found = _find_completed_days()
    return sum([val for days in found.values() for parts in days.values() for val in parts.values()])


def _create_completed_text() -> str:
    found = _find_completed_days()

    text = ['## Completed']
    for year, days in found.items():
        text.append(f'### {year}')

        for day, parts in days.items():
            part_one = '⭐️' if parts['part_one'] else '–'
            part_two = '⭐️' if parts['part_two'] else '–'
            text.append(f'- day {day:02}: part one {part_one}, part two {part_two}')

    text.append('')
    return '\n'.join(text)


def _find_completed_days() -> Dict[int, Dict[int, Dict[str, bool]]]:
    """
    Loops through all the year directories, all the day files
    and checks if the file contains functions 'part_one' and 'part_two'

    Returns the results as a Dict
    """
    items: Dict[int, Dict[int, Dict[str, bool]]] = {}

    for year in _get_years():
        clean_year = _clean_year(year)
        items[clean_year] = {}

        for day in _get_days(year):
            clean_day = _clean_day(day)
            items[clean_year][clean_day] = {}
            funcs = _get_functions_from_day(day)

            items[clean_year][clean_day]['part_one'] = 'part_one' in funcs
            items[clean_year][clean_day]['part_two'] = 'part_two' in funcs

    return items


def _get_years() -> List[str]:
    """
    Retrieves all directories in the ROOT_DIR that start with 'year_'
    """
    return [os.path.join(ROOT_DIR, val) for val in os.listdir(ROOT_DIR) if val.startswith('year_')]


def _get_days(year: str) -> List[str]:
    """
    Retrieves all files in the ROOT_DIR/year_{year} directory that start with 'day_'
    """
    return [os.path.join(year, val) for val in os.listdir(year) if val.startswith('day_')]


def _get_functions_from_day(day: str):
    """
    Uses ast to retrieve all top level functions in the provided day file
    """
    with open(day, 'rt') as f:
        parsed = ast.parse(f.read(), filename=day)

    return [func.name for func in parsed.body if isinstance(func, ast.FunctionDef)]


def _clean_year(year: str) -> int:
    segments = year.split(os.sep)
    year_segment = segments[-1]
    return int(year_segment[len('year_'):])


def _clean_day(day: str) -> int:
    segments = day.split(os.sep)
    day_segment = segments[-1].replace('.py', '')
    return int(day_segment[len('year_'):])
