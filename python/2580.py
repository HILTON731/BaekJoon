import sys

puzzle = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
tmp = list()

for i in range(9):
    for j in range(9):
        if puzzle[i][j] == 0:
            tmp.append((i,j))
# First just hard coding. Too much time spent that occur time running out problem.
# Second changed way of backtracking. Not checking all case of number just checking once and give a list of promising numbers.
# With those steps. Works well.

def promising(count, x, y):
    dx = (x // 3) * 3
    dy = (y // 3) * 3
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        if puzzle[x][i] in num:
            num.remove(puzzle[x][i])
        if puzzle[i][y] in num:
            num.remove(puzzle[i][y])
    for i in range(dx, dx + 3):
        for j in range(dy, dy + 3):
            if puzzle[i][j] in num:
                num.remove(puzzle[i][j])
    return num

def sudoku(count):
    if count == len(tmp):
        for i in puzzle:
            print(*i)
        sys.exit(0)
    else:
        x, y = tmp[count]
        num = promising(count, x, y)
        for i in num:
            puzzle[x][y] = i
            sudoku(count+1)
            puzzle[x][y] = 0
sudoku(0)