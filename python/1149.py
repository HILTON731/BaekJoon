import sys

num = int(sys.stdin.readline())
house = list()
house_sort = list()
for i in range(num):
    house.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, num):
    house[i][0] += min(house[i-1][1:])
    house[i][1] += min(house[i-1][0], house[i-1][2])
    house[i][2] += min(house[i-1][:2])

print(min(house[num-1]))

# Need to think another way of dynamic programming.
# At first, Couldn't realize using input data as computation.
# Must find out recurrence relation. This is key point of solve dp problems.