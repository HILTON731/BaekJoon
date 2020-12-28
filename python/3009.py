import sys

X = list()
Y = list()

for i in range(3):
    x, y = map(int, sys.stdin.readline().split())
    if X.count(x) == 0:
        X.append(x)
    else:
        X.remove(x)
    if Y.count(y) == 0:
        Y.append(y)
    else:
        Y.remove(y)

print("{} {}".format(X.pop(), Y.pop()))