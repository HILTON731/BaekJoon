import sys

N, M = map(int, sys.stdin.readline().split())
tmp = list()

def dfs(count):
    if count == M:
        print(*tmp)
        return None

    for i in range(N):
        tmp.append(i+1)
        dfs(count+1)

        tmp.pop()

dfs(0)

from itertools import product

for i in product(range(1,N+1),repeat = M):
    for j in i:
        print(j,end=' ')
    print()