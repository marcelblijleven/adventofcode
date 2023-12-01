from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day

Position = tuple[int, int]
Paper = dict[Position, int]
Instruction = tuple[str, int]


def fold_position_along_y(position: Position, fold_y: int) -> Position:
    x, y = position
    y = fold_y * 2 - y
    return x, y


def fold_position_along_x(position: Position, fold_x: int) -> Position:
    x, y = position
    x = fold_x * 2 - x
    return x, y


def parse_input(input_data: list[str]) -> tuple[Paper, list[Instruction]]:
    text_input = "\n".join(input_data)

    position_input, instruction_input = text_input.split("\n\n")
    paper: Paper = {}

    for line in position_input.split("\n"):
        x, y = map(int, line.split(","))
        paper[(x, y)] = 1

    instructions: list[Instruction] = []

    for instruction in instruction_input.split("\n"):
        parts = instruction.split(" ")
        axis, position = parts[-1].split("=")
        instructions.append((axis, int(position)))

    return paper, instructions


def run_instructions(paper: Paper, instructions: list[Instruction]) -> Paper:
    for instruction in instructions:
        paper = fold_paper(paper, instruction)

    return paper


def _fold_paper_along_x(paper: Paper, fold_position) -> Paper:
    folded_paper: Paper = {}

    for position in paper.keys():
        if position[0] == fold_position:
            # Position is at fold so gets removed
            continue
        elif position[0] < fold_position:
            folded_paper[position] = 1
        else:
            new_position = fold_position_along_x(position, fold_position)
            folded_paper[new_position] = 1

    return folded_paper


def _fold_paper_along_y(paper: Paper, fold_position) -> Paper:
    folded_paper: Paper = {}

    for position in paper.keys():
        if position[1] == fold_position:
            # Position is at fold so gets removed
            continue
        elif position[1] < fold_position:
            folded_paper[position] = 1
        else:
            new_position = fold_position_along_y(position, fold_position)
            folded_paper[new_position] = 1

    return folded_paper


def fold_paper(paper: Paper, fold_instruction: Instruction) -> Paper:
    axis, fold_position = fold_instruction

    if axis == "x":
        paper = _fold_paper_along_x(paper, fold_position)
    elif axis == "y":
        paper = _fold_paper_along_y(paper, fold_position)
    else:
        raise ValueError(f"invalid instruction received: {fold_instruction}")

    return paper


def _paper_to_str(paper: Paper) -> str:
    max_x = max(key[0] for key in paper.keys())
    max_y = max(key[1] for key in paper.keys())
    lines: list[str] = []

    for y in range(max_y + 1):
        line = ""
        for x in range(max_x + 1):
            if (x, y) in paper:
                line += "█"
            else:
                line += " "
        lines.append(line)

    return "\n".join(lines)


def print_paper(paper: Paper) -> None:
    print(_paper_to_str(paper))  # noqa


def count_visible_dots(paper: Paper) -> int:
    return len(paper.values())


@register_solution(2021, 13, 1)
def part_one(input_data: list[str]):
    paper, instructions = parse_input(input_data)
    paper = run_instructions(paper, instructions[:1])
    answer = count_visible_dots(paper)

    if not answer:
        raise SolutionNotFoundError(2021, 13, 1)

    return answer


@register_solution(2021, 13, 2)
def part_two(input_data: list[str]):
    paper, instructions = parse_input(input_data)
    paper = run_instructions(paper, instructions)
    answer = "\n" + _paper_to_str(paper)

    if not answer:
        raise SolutionNotFoundError(2021, 13, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2021, 13)
    part_one(data)
    part_two(data)
