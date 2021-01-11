import sys

n, w = map(int, sys.stdin.readline().split())
stuff = list(list(map(int, sys.stdin.readline().split()))for _ in range(n))
dp = [0] * (w + 1)

for i in range(n):
    for j in range(w, 1, -1):
        if stuff[i][0] <= j:
            dp[j] = max(dp[j], dp[j-stuff[i][0]] + stuff[i][1])

print(stuff[-1])