import sys

weight = int(sys.stdin.readline())

# case 1
count = weight // 5
left = weight % 5

while True:
    if left % 3 == 0:
        count += left // 3
        break
    left += 5
    count -= 1
    if count < 0:
        count = -1
        break

# case 2
count = 0
while True:
    if weight % 5 == 0:
        count += weight // 5
        print(count)
        break
    weight -= 3
    count += 1
    if weight < 0:
        print(-1)
        break

print(count)