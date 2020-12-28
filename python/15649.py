import sys


# case 1
N, M = map(int, sys.stdin.readline().split())

check = [False] * N
tmp = list()

def dfs(count):
    if count == M:
        print(*tmp)
        return None

    for i in range(N):
        if check[i]:
            continue
        check[i] = True
        tmp.append(i+1)
        dfs(count+1)

        tmp.pop()
        check[i] = False

dfs(0)

# case 2
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())

tmp = [i for i in range(1,N+1)]

for per in permutations(tmp, M):
    for i in per:
        print(i, end=' ')
    print()

# case 3

N, M = map(int, sys.stdin.readline().split())
check = [False] * N
tmp = list()

def dfs1(count):
    if count == M:
        print(*tmp)
        return None
    for i in range(N):
        if check[i]:
            continue
        check[i] = True
        tmp.append(i+1)
        dfs(count+1)
        check[i] = False
        tmp.pop()

dfs1(0)