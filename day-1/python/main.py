from collections import deque
from typing import Iterator, Iterable


def get_input(day: int) -> tuple[int]:
    with open(f"../../inputs/day-{day}.txt", "r") as fp:
        return tuple(int(line) for line in fp.readlines())


def sliding_window(sequence: Iterable, size: int) -> Iterator[deque]:
    iterator = iter(sequence)
    window = deque((next(iterator, None) for _ in range(size)), maxlen=size)
    yield window
    for item in iterator:
        window.append(item)
        yield window


def part_one(day_input: Iterable[int]) -> int:
    return len([
        True
        for prev, current in
        sliding_window(day_input, 2)
        if prev < current
    ])


def part_two(day_input: Iterable[int]) -> int:
    return len([
        True
        for prev, current in
        sliding_window(map(sum, sliding_window(day_input, 3)), 2)
        if prev < current
    ])


def main():
    day_input = get_input(1)
    result_one = part_one(day_input)
    print(result_one)
    result_two = part_two(day_input)
    print(result_two)


if __name__ == "__main__":
    main()
