import sys

tmp = list()

for _ in range(int(sys.stdin.readline())):
    x, y = sys.stdin.readline().strip('\n').split()
    tmp.append((int(x), y))
tmp.sort(key=lambda x: x[0])

for i in tmp:
    print(i[0], i[1])