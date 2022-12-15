import re


SENSOR_REGEX = re.compile(
    r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
)


class Coord:
    def __init__(self, x: int | str, y: int | str) -> None:
        self.x = int(x)
        self.y = int(y)

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)


def part_1(input: str) -> int:
    all_covered_points: set[int] = set()
    beacons_in_row: set[Coord] = set()
    row_y = 2000000
    for line in input.splitlines():
        sensor_x, sensor_y, beacon_x, beacon_y = SENSOR_REGEX.search(line).groups()
        sensor = Coord(sensor_x, sensor_y)
        beacon = Coord(beacon_x, beacon_y)
        distance_to_beacon = sensor.distance(beacon)
        distance_to_row = abs(sensor.y - row_y)
        covered_points = range(
            sensor.x - (distance_to_beacon - distance_to_row),
            sensor.x + (distance_to_beacon - distance_to_row) + 1,
        )
        all_covered_points.update(covered_points)

        if beacon.y == row_y:
            beacons_in_row.add(beacon)

    return len(all_covered_points) - len(beacons_in_row)


def part_2(input: str) -> int:
    pass
