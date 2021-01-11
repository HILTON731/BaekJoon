import sys

print((lambda x: (x[0] * x[1]) + (x[2] * x[3]))(list(map(int, sys.stdin.readline().split()))))