def spiral_order(matrix):
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, -1

    sing = 1

    res = []

    while rows > 0 and cols > 0:

        for _ in range(cols):
            col += sing
            res.append(matrix[row][col])
        rows -= 1

        for _ in range(rows):
            row += sing
            res.append(matrix[row][col])
        cols -= 1

        sing *= -1

    return res


def rotate_image(matrix):
    n = len(matrix)

    for r in range(n // 2):
        for c in range(r, n - r - 1):

            matrix[r][c], matrix[c][n - 1 - r] = matrix[c][n - 1 - r], matrix[r][c]

            matrix[r][c], matrix[n - 1 - r][n - 1 - c] = matrix[n - 1 - r][n - 1 - c], matrix[r][c]

            matrix[r][c], matrix[n-1 - c][r] = matrix[n - 1 - c][r], matrix[r][c]

    return matrix


def find_exist_column(grid:list[list[int]]) -> list[int]:
    m = len(grid)
    n = len(grid[0])
    res = [-1] * n

    for i in range(n):
        c = i
        r = 0

        while r < m:
            sign = grid[r][c]
            if sign == -1:
                if c - 1 >= 0 and grid[r][c - 1] == sign:
                    r +=1
                    c -=1
                else:
                    break
            else:
                if c + 1 < n and grid[r][c + 1] == sign:
                    r +=1
                    c +=1
                else:
                    break
        if r == m:
            res[i] = c
    return res