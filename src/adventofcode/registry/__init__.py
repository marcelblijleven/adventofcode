import os.path
from importlib import import_module

from adventofcode.config import ROOT_DIR
from adventofcode.util.helpers import solution_timer

registry = {}


def autodetect():
    """Automatically detects all solutions in the project"""
    days = sorted(ROOT_DIR.rglob('year_*/day_*.py'))

    for day in days:
        import_module(f'adventofcode.{day.parent.name}.{os.path.splitext(day.name)[0]}')
