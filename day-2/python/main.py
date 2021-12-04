from dataclasses import dataclass


@dataclass
class Coordinates:
    x: int
    y: int


@dataclass
class AimCoordinates:
    x: int
    y: int
    aim: int


def parse_instruction(line: str) -> tuple[str, int]:
    instruction, step = line.split()
    return instruction, int(step)


def get_input(day: int) -> list[tuple[str, int]]:
    with open(f"../../inputs/day-{day}.txt", "r") as fp:
        return [
            parse_instruction(line)
            for line in
            fp.read().split("\n")
        ]


def part_one(day_input: list[str]) -> int:
    coordinates = Coordinates(0, 0)
    for instruction, step in day_input:
        match instruction:
            case "forward":
                coordinates.x += step
            case "down":
                coordinates.y += step
            case "up":
                coordinates.y -= step

    return coordinates.x * coordinates.y


def part_two(day_input: list[str]) -> int:
    coordinates = AimCoordinates(0, 0, 0)
    for instruction, step in day_input:
        match instruction:
            case "down":
                coordinates.aim += step
            case "up":
                coordinates.aim -= step
            case "forward":
                coordinates.x += step
                coordinates.y += coordinates.aim * step

    return coordinates.x * coordinates.y


def main():
    day_input = get_input(2)
    result_one = part_one(day_input)
    print(result_one)
    result_two = part_two(day_input)
    print(result_two)


if __name__ == "__main__":
    main()
