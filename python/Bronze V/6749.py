import sys

print((lambda x: 2*x[1] - x[0])([int(sys.stdin.readline()) for _ in range(2)]))