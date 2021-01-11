import sys

chess = list(map(int, sys.stdin.readline().split()))
tmp = [1, 1, 2, 2, 2, 8]
for i in range(len(chess)):
    tmp[i] -= chess[i]
print(*tmp)