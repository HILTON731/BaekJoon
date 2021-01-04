import sys

tmp = [1] * 3 + [0] * 98

for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())

    for i in range(3, num+1):
            tmp[i] = tmp[i-2] + tmp[i-3]
    print(tmp[num - 1])