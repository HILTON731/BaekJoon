import sys

tmp = list()

def isin(item):
    for i in tmp:
        if i == item:
            return True
    return False

for i in range(10):
    temp = int(sys.stdin.readline()) % 42
    if not isin(temp):
        tmp.append(temp)

print(len(tmp))