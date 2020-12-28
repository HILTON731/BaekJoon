import sys

def isprime(num):
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

for _ in range(int(sys.stdin.readline())):
    tmp = int(sys.stdin.readline())
    
    for i in range(tmp//2, tmp + 1):
        if isprime(i) and isprime(tmp - i):
            print(tmp - i, i)
            break