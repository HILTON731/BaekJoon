row, col = map(int, input().split())
temp = [list(map(int,input())) for _ in range(row)]
start_row = 0
start_col = 0
def chasing(row, col):
    step = temp[row][col]
    if temp[row][col + step] and temp[row][col + step] != 'H':
        right = chasing(row, col + step)
    if temp[row + step][col] and temp[row + step][col] != 'H':
        down = chasing(row + step, col)
    if temp[row - step][col] and temp[row - step][col] != 'H':
        up = chasing(row - step, col)
    if temp[row][col - step] and temp[row][col - step] != 'H':
        left = chasing(row, col - step)
    return max(right, down, up, left) + 1
print(chasing(start_row, start_col))