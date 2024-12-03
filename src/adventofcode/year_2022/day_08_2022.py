from adventofcode.registry.decorators import register_solution
from adventofcode.util.exceptions import SolutionNotFoundError
from adventofcode.util.input_helpers import get_input_for_day


def get_grid_size(input_data: list[str]) -> tuple[int, int]:
    """Get the horizontal and vertical for the provided data"""
    return len(input_data[0]), len(input_data)


def get_grid(input_data: list[str]) -> dict[tuple[int, int], int]:
    """Parse input to (x, y) grid"""
    grid: dict[tuple[int, int], int] = {}

    for y, row in enumerate(input_data):
        for x, value in enumerate(row):
            grid[(x, y)] = int(value)

    return grid


def is_visible(
    grid: dict[tuple[int, int], int], tree: tuple[int, int], grid_size: tuple[int, int]
) -> bool:
    """Check if the tree is visible from the outside"""
    x, y = tree
    horizontal, vertical = grid_size
    tree_size = grid[tree]

    # First check if the tree is on the outer edges
    if x == 0 or x == horizontal - 1:  # noqa: PLR1714
        return True
    if y == 0 or y == vertical - 1:  # noqa: PLR1714
        return True

    # Check horizontal
    # - Check all left
    if all([grid[check_x, y] < tree_size for check_x in range(0, x)]):  # noqa: C419
        return True

    # - Check all right
    if all([grid[check_x, y] < tree_size for check_x in range(x + 1, horizontal)]):  # noqa: C419
        return True

    # Check vertical
    # - Check all above
    if all([grid[x, check_y] < tree_size for check_y in range(0, y)]):  # noqa: C419
        return True

    # - Check all below
    if all([grid[x, check_y] < tree_size for check_y in range(y + 1, vertical)]):  # noqa: C419
        return True

    return False


def get_visible_trees(input_data: list[str]) -> int:
    """Get trees that are visible from the outside"""
    grid_size = get_grid_size(input_data)
    grid = get_grid(input_data)
    visible_trees = 0

    for y in range(grid_size[1]):
        for x in range(grid_size[0]):
            visible_trees += 1 if is_visible(grid, (x, y), grid_size) else 0

    return visible_trees


def get_scenic_score_for_tree(
    grid: dict[tuple[int, int], int], tree: tuple[int, int], grid_size: tuple[int, int]
) -> int:
    """
    Get scenic score for the provided tree
    Scenic score is the number of trees it can see in each direction, multiplied by each other
    """
    x, y = tree
    horizontal, vertical = grid_size
    tree_size = grid[tree]

    left, right, up, down = 0, 0, 0, 0

    # Get all trees to the left of X until we reach zero
    for _x in range(x - 1, -1, -1):
        left += 1
        if grid[_x, y] >= tree_size:
            break

    # Get all trees to the right of X until we reach max length
    for _x in range(x + 1, horizontal):
        right += 1
        if grid[_x, y] >= tree_size:
            break

    # Get all trees above Y until we reach zero
    for _y in range(y - 1, -1, -1):
        up += 1
        if grid[x, _y] >= tree_size:
            break

    # Get all trees below Y until we reach max length
    for _y in range(y + 1, vertical):
        down += 1
        if grid[x, _y] >= tree_size:
            break

    return left * right * up * down


def get_scenic_scores(input_data: list[str]) -> int:
    """Find the tree with the max scenic score"""
    grid_size = get_grid_size(input_data)
    grid = get_grid(input_data)
    max_scenic_score = 0

    for y in range(grid_size[1]):
        for x in range(grid_size[0]):
            max_scenic_score = max(
                max_scenic_score, get_scenic_score_for_tree(grid, (x, y), grid_size)
            )

    return max_scenic_score


@register_solution(2022, 8, 1)
def part_one(input_data: list[str]):
    answer = get_visible_trees(input_data)

    if not answer:
        raise SolutionNotFoundError(2022, 8, 1)

    return answer


@register_solution(2022, 8, 2)
def part_two(input_data: list[str]):
    answer = get_scenic_scores(input_data)

    if not answer:
        raise SolutionNotFoundError(2022, 8, 2)

    return answer


if __name__ == "__main__":
    data = get_input_for_day(2022, 8)
    part_one(data)
    part_two(data)
