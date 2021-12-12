from __future__ import annotations

from typing import NamedTuple


class Coords2D(NamedTuple):
    depth: int = 0
    distance: int = 0

    def update(self, depth: int, distance: int) -> Coords2D:
        return self.__class__(self.depth + depth, self.distance + distance)

    def follow_instruction(self, instruction: str) -> Coords2D:
        direction, amount = instruction.split()
        distance, depth = [0, 0]
        if direction == "forward":
            distance += int(amount)
        elif direction == "down":
            depth += int(amount)
        elif direction == "up":
            depth -= int(amount)
        else:
            raise ValueError(f"unrecognized instruction {direction}")
        return self.update(distance=distance, depth=depth)


class Coords3D(NamedTuple):
    depth: int = 0
    distance: int = 0
    aim: int = 0

    def update(self, depth: int, distance: int, aim: int) -> Coords3D:
        return self.__class__(
            depth=self.depth + depth,
            distance=self.distance + distance,
            aim=self.aim + aim,
        )

    def follow_instruction(self, instruction: str) -> Coords3D:
        direction, amount = instruction.split()
        distance, depth, aim = [0, 0, 0]
        val = int(amount)
        if direction == "forward":
            distance += val
            depth += self.aim * val
        elif direction == "down":
            aim += val
        elif direction == "up":
            aim -= val
        else:
            raise ValueError(f"unrecognized instruction {direction}")
        return self.update(distance=distance, depth=depth, aim=aim)


def main():
    with open("input") as f:
        instructions = [x.strip() for x in f.readlines()]

    current_pos = Coords2D()
    for instruction in instructions:
        current_pos = current_pos.follow_instruction(instruction)
    print(f"final position: {current_pos.depth=}, {current_pos.distance=}")

    current_pos = Coords3D()
    for instruction in instructions:
        current_pos = current_pos.follow_instruction(instruction)
    print(
        f"final position: {current_pos.depth=}, {current_pos.distance=}, answer = {current_pos.depth*current_pos.distance}"
    )


if __name__ == "__main__":
    main()
