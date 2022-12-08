def part_1(input: str) -> int:
    lines = input.splitlines()
    rows_n = len(lines)
    cols_n = len(lines[0])

    visible_trees = [[True] + [False] * (cols_n - 2) + [True] for _ in range(rows_n)]
    visible_trees[0] = [True] * cols_n
    visible_trees[-1] = [True] * cols_n

    max_left = {i: row[0] for i, row in enumerate(lines)}
    max_top = {i: tree for i, tree in enumerate(lines[0])}
    max_right = {i: row[-1] for i, row in enumerate(lines)}
    max_bottom = {i: tree for i, tree in enumerate(lines[-1])}

    for row in range(1, rows_n - 2):
        for col in range(1, cols_n - 2):
            tree = lines[row][col]

            if tree > max_left[row]:
                visible_trees[row][col] = True
                max_left[row] = tree

            if tree > max_top[col]:
                visible_trees[row][col] = True
                max_top[col] = tree

    for row in range(rows_n - 2, 1, -1):
        for col in range(cols_n - 2, 1, -1):
            tree = lines[row][col]

            if tree > max_right[row]:
                visible_trees[row][col] = True
                max_right[row] = tree

            if tree > max_bottom[col]:
                visible_trees[row][col] = True
                max_bottom[col] = tree

    return sum([sum(row) for row in visible_trees])


def part_2(input: str) -> int:
    lines = input.splitlines()
    rows_n = len(lines)
    cols_n = len(lines[0])

    max_score = 0

    for row_idx, row in list(enumerate(lines))[1:-1]:
        for col_idx, tree in list(enumerate(row))[1:-1]:
            up, down, left, right = 0, 0, 0, 0
            i = 1

            while up == 0 or left == 0 or down == 0 or right == 0:
                if up == 0:
                    if row_idx - i >= 0:
                        if lines[row_idx - i][col_idx] >= tree:
                            up = i
                    else:
                        up = row_idx

                if down == 0:
                    if row_idx + i < rows_n:
                        if lines[row_idx + i][col_idx] >= tree:
                            down = i
                    else:
                        down = rows_n - row_idx - 1

                if left == 0:
                    if col_idx - i >= 0:
                        if lines[row_idx][col_idx - i] >= tree:
                            left = i
                    else:
                        left = col_idx

                if right == 0:
                    if col_idx + i < cols_n:
                        if lines[row_idx][col_idx + i] >= tree:
                            right = i
                    else:
                        right = cols_n - col_idx - 1

                i += 1

            score = up * down * left * right
            max_score = max(score, max_score)

    return max_score
