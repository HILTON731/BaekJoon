import sys

N, K = map(int, sys.stdin.readline().split())
stuff = list(list(map(int, sys.stdin.readline().split()))for _ in range(N))
stuff.sort(key=lambda k: (k[1]/k[0], k[1]), reverse=True)
tmp = [0, 0] * N

print(tmp)
for i in range(N):
    tmp[i] = max(tmp[i], tmp[i] + stuff[i][0])