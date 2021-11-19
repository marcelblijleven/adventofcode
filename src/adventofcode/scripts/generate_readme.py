import os
import re
from typing import Dict

from adventofcode.config import ROOT_DIR
from adventofcode.util.module_helpers import get_functions_from_day_file, get_full_day_paths, get_full_year_paths, clean_day, clean_year


YearDayType = Dict[int, Dict[int, Dict[str, bool]]]


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

    text = ['## Completed ⭐️']
    for year, days in found.items():
        text.append(f'### {year}')

        for day, parts in days.items():
            part_one = '⭐️' if parts['part_one'] else '–'
            part_two = '⭐️' if parts['part_two'] else '–'
            text.append(f'- day {day:02}: part one {part_one}, part two {part_two}')

    text.append('')
    return '\n'.join(text)


def _find_completed_days() -> YearDayType:
    """
    Loops through all the year directories, all the day files
    and checks if the file contains functions 'part_one' and 'part_two'

    Returns the results as a Dict
    """
    items: YearDayType = {}

    for year_path in get_full_year_paths():
        year = clean_year(year_path)
        items[year] = {}

        for day_file in get_full_day_paths(year_path):
            day = clean_day(day_file)
            items[year][day] = {}
            funcs = get_functions_from_day_file(day_file)

            items[year][day]['part_one'] = 'part_one' in funcs
            items[year][day]['part_two'] = 'part_two' in funcs

    return items
