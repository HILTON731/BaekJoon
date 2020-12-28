import sys

num = int(sys.stdin.readline())

temp = list()
def hanoi(disk, start = 1, tmp = 2, end = 3):
    if disk == 1:
        temp.append([start, end])
        return
    hanoi(disk - 1, start, end, tmp)
    temp.append([start, end])
    hanoi(disk - 1, tmp, start, end)

hanoi(num)
print(len(temp))
for i in temp:
    print(i[0], i[1])