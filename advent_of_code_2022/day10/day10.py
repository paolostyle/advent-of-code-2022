class CPU:
    def __init__(self, program: str):
        self.register = 1
        self.cycle = 1
        self.history: list[int] = []
        self.run_program(program)

    def run_program(self, program: str):
        for instruction in program.splitlines():
            match instruction.split(" "):
                case ["noop"]:
                    self.tick()
                case ["addx", value]:
                    self.addx(int(value))
        return self

    def addx(self, value: int):
        self.tick()
        self.tick()
        self.register += value

    def tick(self):
        self.cycle += 1
        self.history.append(self.register)

    def display_screen(self) -> str:
        screen = ""
        for cycle, register in enumerate(self.history):
            if cycle % 40 == 0:
                screen += "\n"
            if cycle % 40 in range(register - 1, register + 2):
                screen += "#"
            else:
                screen += "."
        return screen

    def signal_strength(self) -> int:
        return sum(
            [
                cycle * self.history[cycle - 1]
                for cycle in range(20, len(self.history), 40)
            ]
        )


def part_1(input: str) -> int:
    return CPU(input).signal_strength()


def part_2(input: str) -> str:
    return CPU(input).display_screen()
