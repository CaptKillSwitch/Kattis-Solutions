from collections import deque


def flood_fill(r, c, val, matrix: [[]], t, _row, _col):
    stack = deque()
    stack.appendleft((r, c))
    while len(stack) > 0:
        r, c = stack.popleft()
        matrix[r][c] = t
        if r + 1 < _row and type(matrix_input[r + 1][c]) == int and matrix[r + 1][c] == val:
            stack.appendleft((r + 1, c))
        if c + 1 < _col and type(matrix_input[r][c + 1]) == int and matrix[r][c + 1] == val:
            stack.appendleft((r, c + 1))
        if r - 1 >= 0 and type(matrix_input[r - 1][c]) == int and matrix[r - 1][c] == val:
            stack.appendleft((r - 1, c))
        if c - 1 >= 0 and type(matrix_input[r][c-1]) == int and matrix[r][c - 1] == val:
            stack.appendleft((r, c - 1))


if __name__ == '__main__':
    decimal_graphs = []
    binary_graphs = []
    row, col = [int(x) for x in input().split(" ")]
    matrix_input = [[int(x) for x in input()] for _ in range(row)]
    graphs = []
    mark = 0
    for i in range(row):
        for j in range(col):
            if type(matrix_input[i][j]) == int:
                linked_points = []
                value = matrix_input[i][j]
                if value == 0:
                    flood_fill(i, j, matrix_input[i][j], matrix_input, (mark, 0), row, col)
                else:
                    flood_fill(i, j, matrix_input[i][j], matrix_input, (mark, 1), row, col)
                mark += 1
    for _ in range(int(input())):
        r1, c1, r2, c2 = [int(x) - 1 for x in input().split(" ")]
        graph1, point1_type = matrix_input[r1][c1]
        graph2, point2_type = matrix_input[r2][c2]
        if graph1 == graph2 and point1_type == point2_type:
            if point1_type == 0:
                print("binary")
            else:
                print("decimal")
        else:
            print("neither")
