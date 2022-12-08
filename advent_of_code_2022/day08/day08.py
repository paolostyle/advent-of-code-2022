def analyze_trees(input: str):
    lines = input.splitlines()
    rows_n = len(lines)
    cols_n = len(lines[0])

    visible_trees = [[True] + [False] * (cols_n - 2) + [True] for _ in range(rows_n)]
    visible_trees[0] = [True] * cols_n
    visible_trees[-1] = [True] * cols_n

    max_left = {}
    max_top = {}

    for row_idx, row in list(enumerate(lines))[1:-1]:
        max_left[row_idx] = row[0]
        for col_idx, tree in list(enumerate(row))[1:-1]:
            if row_idx == 1:
                max_top[col_idx] = lines[0][col_idx]

            if tree > max_left[row_idx]:
                visible_trees[row_idx][col_idx] = True
                max_left[row_idx] = tree

            if tree > max_top[col_idx]:
                visible_trees[row_idx][col_idx] = True
                max_top[col_idx] = tree

    max_right = {}
    max_bottom = {}

    for row_idx, row in reversed(list(enumerate(lines))[1:-1]):
        max_right[row_idx] = row[-1]
        for col_idx, tree in reversed(list(enumerate(row))[1:-1]):
            if row_idx == rows_n - 2:
                max_bottom[col_idx] = lines[-1][col_idx]

            if tree > max_right[row_idx]:
                visible_trees[row_idx][col_idx] = True
                max_right[row_idx] = tree

            if tree > max_bottom[col_idx]:
                visible_trees[row_idx][col_idx] = True
                max_bottom[col_idx] = tree

    return visible_trees


def part_1(input: str) -> int:
    visible_trees = analyze_trees(input)
    return sum([sum(row) for row in visible_trees])


def part_2(input: str) -> int:
    pass
