from __future__ import annotations

from typing import NamedTuple


class Coords(NamedTuple):
    depth: int = 0
    distance: int = 0

    def update(self, depth: int, distance: int) -> Coords:
        return self.__class__(self.depth + depth, self.distance + distance)

    def follow_instruction(self, instruction: str) -> Coords:
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
        return self.update(depth, distance)


def main():
    with open("input") as f:
        instructions = [x.strip() for x in f.readlines()]

    current_pos = Coords()

    for instruction in instructions:
        current_pos = current_pos.follow_instruction(instruction)

    print(f"final position: {current_pos.depth=}, {current_pos.distance=}")


if __name__ == "__main__":
    main()
