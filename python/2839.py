import sys

weight = int(sys.stdin.readline())

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

print(count)