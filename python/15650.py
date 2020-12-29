import sys

# case 1: hard coding of combinations with using stack
# First I didn't realize how to make combination without using library from itertools.
# So searching for google and there's a solution.
# In combination recongnize that first picked number never selected after finish operations.
# You just turn other selected numbers False without first selected one.
N, M = map(int, sys.stdin.readline().split())

check = list(False for _ in range(N))
tmp = list()

def dfs(count):
    if count == M:
        print(*tmp)
        return None
    for i in range(N):
        if check[i]:
            continue
        tmp.append(i+1)
        check[i] = True
        dfs(count+1)
        tmp.pop()

        # Return except first selected value.
        for j in range(i+1,N):
            check[j] = False

dfs(0)

# Case 2: Just using library function from itertools.
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

for i in combinations(range(1,N+1),M):
    for j in i:
        print(j, end=' ')
    print()