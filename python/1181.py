import sys

tmp = list()

for _ in range(int(sys.stdin.readline())):
    tmp.append(sys.stdin.readline().strip('\n'))
tmp = list(set(tmp))
tmp.sort(key=lambda x:(len(x), x))

for i in tmp:
    print(i)