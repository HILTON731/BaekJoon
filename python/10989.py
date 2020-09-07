import sys

num = int(sys.stdin.readline())
result = [0]*10001
for i in range(num):
    n = int(sys.stdin.readline())
    result[n] += 1

for i in range(len(result)):
    if result[i] != 0:
        for j in range(result[i]):
            sys.stdout.write("{}\n".format(i))
