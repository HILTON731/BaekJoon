import sys

start, end = map(int, sys.stdin.readline().split())

tmp = list(True if i > 1 else False for i in range(end + 1) )

for i in range(2, int(end ** 0.5) + 1):
    for j in range(2*i, end + 1, i):
        tmp[j] = False

for i in range(start, end + 1):
    if tmp[i]:
        print(i)

# Sieve of Eratosthenes
# arange numbers and rid of it if numbers could divide by least prime number
# repeating until sqrt(max number) then only prime number left
# print numbers that in boundary