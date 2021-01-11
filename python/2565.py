import sys

num = int(sys.stdin.readline())
check = [0] * num
line = list(list(map(int, sys.stdin.readline().split())) for _ in range(num))
line.sort(key=lambda x: x[0])
line = list(zip(*line))[1]

for i in range(num):
    for j in range(i):
        if line[i] > line[j] and check[i] < check[j]:
            check[i] = check[j]
    check[i] += 1

print(num - max(check))