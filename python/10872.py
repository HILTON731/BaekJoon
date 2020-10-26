import sys

def fac(n):
    return n * fac(n-1) if n > 1 else 1

print(fac(int(sys.stdin.readline())))