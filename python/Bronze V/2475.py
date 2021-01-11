import sys

print(sum(list(map(lambda x : int(x) ** 2, sys.stdin.readline().split()))) % 10)