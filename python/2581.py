import sys

start = int(sys.stdin.readline())
end = int(sys.stdin.readline())

minimum = end + 1
tmp = 0

for i in range(start, end + 1):
    prime = True
    if i == 1: continue
    for j in range(2, i):
        if i % j == 0:
            prime = False
            break
    if prime:
        tmp += i
        minimum = i if i < minimum else minimum

if tmp == 0: print(-1)
else:
    print(tmp)
    print(minimum)