import sys
# case 1: running out of time in "python 3". Must use "PyPy3"
num = int(sys.stdin.readline())
col = [0] * num
count = 0

def promising(row):
    for i in range(row):
        if col[i] == col[row] or abs(i - row) == abs(col[i] - col[row]):
            return False
    return True

def n_queens(row):
    global count
    if row == num:
        count += 1
        return None
    else:
        for i in range(num):
            col[row] = i
            if promising(row):
                n_queens(row+1)

n_queens(0)
print(count)

# case 2: https://rebas.kr/761 look out the link

col, ldiag, rdiag = [False] * num, [0] * (2 * num - 1), [0] * (2 * num - 1)
count = 0
def solve(i):
    global count
    if i == num:
        count += 1
        return None
    for j in range(num):
        if not(col[j] or ldiag[i + j] or rdiag[i - j + num - 1]):
            col[j] = ldiag[i + j] = rdiag[i - j + num - 1] = True
            solve(i + 1)
            col[j] = ldiag[i + j] = rdiag[i - j + num - 1] = False
            
solve(0)
print(count)