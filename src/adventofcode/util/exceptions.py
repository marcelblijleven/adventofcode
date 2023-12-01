class SolutionNotFoundError(Exception):
    def __init__(self, year: int, day: int, part: int):
        message = f"solution not found for {year} day {day:02} part {part}"
        super().__init__(message)
