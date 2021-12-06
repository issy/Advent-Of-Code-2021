from __future__ import annotations

from collections import Counter
from typing import Mapping
from itertools import groupby


class Fish:
    timer: int
    value: int

    def __init__(self, timer_start_value: int, value: int = 1):
        self.timer = timer_start_value
        self.value = value

    def tick(self) -> bool:
        if self.timer == 0:
            maybe_fish = True
            self.timer = 7
        else:
            maybe_fish = False

        self.timer -= 1
        return maybe_fish

    def get_timer_value(self) -> int:
        return self.timer


class FishSimulator:
    fish: list[Fish]

    def __init__(self, start_fish: Mapping[int, int]):
        self.fish = [Fish(start, value) for start, value in start_fish.items()]

    def simulate(self, days: int) -> int:
        for _ in range(days):
            self.fish.append(Fish(8, sum(
                fish.value
                for fish in
                self.fish
                if fish.tick()
            )))
            self.fish = [
                Fish(*[key, sum(f.value for f in result)])
                for key, result in
                groupby(
                    sorted(self.fish, key=Fish.get_timer_value),
                    key=Fish.get_timer_value
                )
            ]

        return sum([fish.value for fish in self.fish])


def get_input(day: int) -> FishSimulator:
    with open(f"../../inputs/day-{day}.txt", "r") as fp:
        return FishSimulator(Counter([int(i) for i in fp.read().split(",")]))


def part_one(day_input: FishSimulator) -> int:
    return day_input.simulate(80)


def part_two(day_input: FishSimulator) -> int:
    return day_input.simulate(256 - 80)


def main():
    day_input = get_input(6)
    result_one = part_one(day_input)
    print(result_one)
    result_two = part_two(day_input)
    print(result_two)


if __name__ == "__main__":
    main()
