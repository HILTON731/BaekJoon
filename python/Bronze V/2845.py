import sys

L, P = map(int, sys.stdin.readline().split())
print(*list(map(lambda x: int(x) - (L * P), sys.stdin.readline().split())))
