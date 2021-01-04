import sys

num = int(sys.stdin.readline())
house = list()
house_sort = list()
for i in range(num):
    house.append(list(map(int, sys.stdin.readline().split())))

    house_sort.append(sorted(house[i]))

print(house, house_sort)

