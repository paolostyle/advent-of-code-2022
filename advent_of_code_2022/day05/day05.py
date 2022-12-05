import re

STACK_WIDTH = 3
CRATE_GAP = 1
MARKS_GAP = STACK_WIDTH + CRATE_GAP
INSTRUCTION_REGEX = re.compile(r"move (\d+) from (\d+) to (\d+)")


def parse_input(input: str):
    lines = input.splitlines()
    stack_line_width = len(lines[0])
    stacks_count = (stack_line_width - STACK_WIDTH) // MARKS_GAP + 1

    stacks: dict[int, list] = {index: [] for index in range(1, stacks_count + 1)}
    instructions_line_start = -1

    for index, line in enumerate(lines):
        # numbering row
        if line.startswith(" 1"):
            # +2 for numbering row and empty line afterwards
            instructions_line_start = index + 2
            break

        for stack in range(stacks_count):
            crate_mark = line[1 + stack * MARKS_GAP]
            if crate_mark.isalpha():
                stacks[stack + 1].append(crate_mark)

    instructions = []
    for instruction in lines[instructions_line_start:]:
        matched_instruction = INSTRUCTION_REGEX.search(instruction)

        if matched_instruction:
            instructions.append([int(match) for match in matched_instruction.groups()])

    return stacks, instructions


def get_top_crates(stacks: dict[int, list], idx: int) -> str:
    end_string = ""

    for stack in stacks.values():
        end_string += stack[idx]

    return end_string


def part_1(input: str) -> str:
    stacks, instructions = parse_input(input)

    for s in stacks.values():
        s.reverse()

    for instruction in instructions:
        to_move, from_stack, to_stack = instruction

        for _ in range(to_move):
            item = stacks[from_stack].pop()
            stacks[to_stack].append(item)

    return get_top_crates(stacks, -1)


def part_2(input: str) -> str:
    stacks, instructions = parse_input(input)

    for instruction in instructions:
        to_move, from_stack, to_stack = instruction

        crates = stacks[from_stack][:to_move]
        stacks[from_stack] = stacks[from_stack][to_move:]
        stacks[to_stack] = crates + stacks[to_stack]

    return get_top_crates(stacks, 0)
