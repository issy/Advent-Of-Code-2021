from functools import reduce
from collections import Counter
from typing import Callable


NUM_OF_BITS = 12


def get_input(day: int) -> list[str]:
    with open(f"../../inputs/day-{day}.txt", "r") as fp:
        return fp.read().split()


def bitwise_xor(a: int, b: int) -> int:
    return a ^ b


def get_power_rating(values: list[int], predicate: Callable[[int, int], bool]) -> int:
    threshold = len(values) // 2
    return reduce(int.__xor__, [
        (
            predicate(sum(
                bool(line & (True << i))
                for line in values
            ), threshold)
        ) << i
        for i in range(NUM_OF_BITS)
    ])


def get_rating(values: list[str], select_least_common: bool, default_to: str) -> int:
    values = values.copy()
    for i in range(len(values[0])):
        if len(values) == 1:
            break

        counter = Counter(s[i] for s in values)
        selection: str
        if counter["0"] == counter["1"]:
            selection = default_to
        else:
            selection, _ = counter.most_common()[-1 if select_least_common else 0]
        values = [s for s in values if s[i] == selection]

    return int(values[0], 2)


def part_one(day_input: list[str]) -> int:
    day_input = [int(line, 2) for line in day_input]
    gamma = get_power_rating(day_input, int.__gt__)
    epsilon = get_power_rating(day_input, int.__lt__)
    return gamma * epsilon


def part_two(day_input: list[str]) -> int:
    oxy = get_rating(day_input, False, "1")
    co2 = get_rating(day_input, True, "0")
    return oxy * co2


def main():
    day_input = get_input(3)
    result_one = part_one(day_input)
    print(result_one)
    result_two = part_two(day_input)
    print(result_two)


if __name__ == "__main__":
    main()
