import sys

count = int(sys.stdin.readline())

tmp = list(map(int, sys.stdin.readline().split()))

if count == len(tmp):
    for i in tmp:
        correct = True
        if i == 1:
            count -= 1
            continue
        for t in range(2, i):
            if i % t == 0:
                count -= 1
                break
    print(count)