import math


def mean(target_list: list[int], floor: bool = True) -> int:
    """
    Gets the mean value of the list, rounded down if floor is True, else rounded up
    """
    if floor:
        return mean_floor(target_list)

    return mean_ceil(target_list)


def mean_floor(target_list: list[int]) -> int:
    """
    Gets the rounded down mean of the list
    """
    return sum(target_list) // len(target_list)


def mean_ceil(target_list: list[int]) -> int:
    """
    Gets the rounded up mean of the list
    """
    return math.ceil(sum(target_list) / len(target_list))


def gaussian_sum(number: int) -> int:
    """
    Gets the sum of all numbers up to the provided number.
    E.g. gaussian_sum(5) == sum([1, 2, 3, 4, 5])
    :param number:
    :return:
    """
    return number * (1 + number) // 2
