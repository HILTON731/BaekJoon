import sys

num, avg = map(int, sys.stdin.readline().split())
print(num * (avg - 1) + 1)