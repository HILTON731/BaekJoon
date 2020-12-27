import sys

A, B, V = map(int, sys.stdin.readline().split())

count = (V - A) // (A - B) + 1

if (V - A) % (A - B) != 0:
    count += 1

print(count)