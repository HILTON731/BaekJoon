import sys

N, M = map(int, sys.stdin.readline().split())
tmp = list()
def dfs(count):
    if count == M:
        print(*tmp)
        return None
    for i in range(1, N + 1):
        if len(tmp) == 0 or tmp[-1] <= i:
            tmp.append(i)
            dfs(count+1)
            tmp.pop()

dfs(0)

from itertools import combinations_with_replacement

for i in combinations_with_replacement(range(1,N+1),M):
    for j in i:
        print(j,end=' ')
    print()