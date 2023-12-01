import os
from concurrent.futures import ProcessPoolExecutor
from typing import Any

from rich.table import Table

from adventofcode import config
from adventofcode.config import ROOT_DIR
from adventofcode.scripts.generate_readme import _replace_between_tags
from adventofcode.util.console import console
from adventofcode.util.input_helpers import get_input_for_day
from adventofcode.util.module_helpers import (
    clean_day,
    clean_year,
    get_full_day_paths,
    get_full_module_from_day_file,
    get_full_year_paths,
    year_dir_from_path,
)

Benchmarks = dict[int, dict[int, dict[str, float]]]


def generate_benchmarks() -> None:
    benchmarks = get_benchmarks()
    write_benchmarks_to_readme(benchmarks)


def get_benchmarks() -> Benchmarks:
    """
    Runs all tests and retrieves the benchmarks
    """
    benchmarks = _retrieve_benchmarks()
    # benchmarks = _retrieve_benchmarks_mp()
    print(get_averages(benchmarks))  # noqa
    return benchmarks


def get_averages(benchmarks: Benchmarks) -> tuple[float, float]:
    part_one_solutions = []
    part_two_solutions = []

    for days in benchmarks.values():
        for solutions in days.values():
            for solution, benchmark in solutions.items():
                if solution.startswith("part one"):
                    part_one_solutions.append(benchmark)
                elif solution.startswith("part two"):
                    part_two_solutions.append(benchmark)

    return sum(part_one_solutions) / len(part_one_solutions), sum(
        part_two_solutions
    ) / len(part_two_solutions)


def create_benchmark_text(benchmarks: Benchmarks) -> str:
    text = ["## Benchmarks 🚀"]

    for year, days in benchmarks.items():
        year_text = [
            f"### {year}",
            f"<details><summary>Benchmarks for {year}</summary>",
            "<p>",
            "",
            "|  day  | part  | duration |",
            "| :---: | :---: | -------: |",
        ]

        for day, parts in days.items():
            for part, duration in parts.items():
                year_text.append(f"| {day:02} | {part} | {duration:.2f} ms |")

        year_text += [
            "",
            "</p>",
            "</details>",
            "",
        ]
        text += year_text

    return "\n".join(text)


def generate_rich_tables(benchmarks: Benchmarks) -> list[tuple[int, Table]]:
    tables: list[tuple[int, Table]] = []

    for year, days in benchmarks.items():
        console.print(f"[bold]{year}")

        table = Table()
        table.add_column("Day", justify="left")
        table.add_column("Part", justify="center")
        table.add_column("Solution", justify="right")

        for day, parts in days.items():
            for part, duration in parts.items():
                table.add_row(f"{day:02}", f"{part}", f"{duration:.2f} ms")

        tables.append((year, table))

    return tables


def write_benchmarks_to_readme(benchmarks: Benchmarks):
    console.log("writing benchmarks to readme")
    console.print_json(data=benchmarks)
    benchmark_text = create_benchmark_text(benchmarks)
    path = os.path.join(ROOT_DIR, "../../README.md")
    readme_file = os.path.abspath(path)

    with open(readme_file) as f:
        current_readme = f.read()

    readme = _replace_between_tags(
        current_readme,
        benchmark_text,
        "<!-- start benchmark section -->",
        "<!-- end benchmark section -->",
    )

    with open(readme_file, "w") as f:
        f.write(readme)

    console.log("generating benchmarks table")
    tables = generate_rich_tables(benchmarks)

    console.print("[bold]Benchmarks 🚀")
    for year, table in tables:
        console.print(year)
        console.print(table)


def _retrieve_benchmarks_for_day_mp(
    day_file: str, year: int
) -> dict[int, dict[str, float]]:
    config.RUNNING_BENCHMARKS = True
    day = clean_day(day_file)
    benchmarks: dict[int, dict[str, float]] = {day: {}}

    module_name = get_full_module_from_day_file(day_file)
    module = __import__(module_name, fromlist=["object"])

    try:
        _run_day_mp(module, year, day, benchmarks)
    except FileNotFoundError:
        console.print(f"[blue]{year} day {day:02}: [red]input file not found")

    return benchmarks


def _retrieve_benchmarks_mp() -> Benchmarks:
    config.RUNNING_BENCHMARKS = True
    benchmarks: Benchmarks = {}

    for year_path in get_full_year_paths():
        year_dir = year_dir_from_path(year_path)
        year = clean_year(year_dir)
        benchmarks[year] = {}

        days = get_full_day_paths(year_path)
        results = []

        with ProcessPoolExecutor(max_workers=8) as executor:
            for day in days:
                result = executor.submit(_retrieve_benchmarks_for_day_mp, day, year)
                results.append(result)

        for result in results:
            benchmarks[year].update(result.result())

    return benchmarks


def _retrieve_benchmarks() -> Benchmarks:
    config.RUNNING_BENCHMARKS = True
    benchmarks: Benchmarks = {}

    for year_path in get_full_year_paths():
        year_dir = year_dir_from_path(year_path)
        year = clean_year(year_dir)
        benchmarks[year] = {}

        for day_file in get_full_day_paths(year_path):
            day = clean_day(day_file)
            benchmarks[year][day] = {}

            module_name = get_full_module_from_day_file(day_file)
            module = __import__(module_name, fromlist=["object"])

            try:
                _run_day(module, year, day, benchmarks)
            except FileNotFoundError:
                console.print(f"[blue]{year} day {day:02}: [red]input file not found")

    config.RUNNING_BENCHMARKS = False
    console.log("finished running benchmarks")
    return benchmarks


def _get_extra_solutions_in_module(module: str) -> list[str]:
    def _eval_functions(f: str) -> bool:
        return f not in ["part_one", "part_two"] and (
            f.startswith("part_one") or f.startswith("part_two")
        )

    functions = dir(module)
    return [f for f in functions if _eval_functions(f)]


def _run_day(module: Any, year: int, day: int, benchmarks: Benchmarks):
    """
    Runs all solutions in the given day
    """
    data = get_input_for_day(year, day)
    console.log(f"retrieved input for {year} {day:02}")

    try:
        benchmarks[year][day]["part one"] = module.part_one(data)
    except AttributeError:
        pass

    console.log(f"ran {year} {day:02} part one")

    try:
        benchmarks[year][day]["part two"] = module.part_two(data)
    except AttributeError:
        pass

    console.log(f"ran {year} {day:02} part two")

    for solution in _get_extra_solutions_in_module(module):
        readable_name = solution.replace("_", " ")
        try:
            benchmarks[year][day][readable_name] = getattr(module, solution)(data)
        except AttributeError:
            pass

        console.log(f"ran {year} {day:02} {readable_name}")


def _run_day_mp(
    module: Any, year: int, day: int, benchmarks: dict[int, dict[str, float]]
):
    """
    Runs all solutions in the given day
    """
    data = get_input_for_day(year, day)
    console.log(f"retrieved input for {year} {day:02}")

    try:
        benchmarks[day]["part one"] = module.part_one(data)
    except AttributeError:
        pass

    try:
        benchmarks[day]["part two"] = module.part_two(data)
    except AttributeError:
        pass

    for solution in _get_extra_solutions_in_module(module):
        readable_name = solution.replace("_", " ")
        try:
            benchmarks[day][readable_name] = getattr(module, solution)(data)
        except AttributeError:
            pass


if __name__ == "__main__":
    generate_benchmarks()
