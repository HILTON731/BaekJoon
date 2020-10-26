import sys

num = int(sys.stdin.readline())

def fib(n):
    temp = [0, 1]
    if n < 2:
        return n
    for i in range(2, n + 1):
        temp.append(temp[i-1] + temp[i-2])
    return temp[n]

print(fib(num))