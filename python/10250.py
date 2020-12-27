import sys

case = int(sys.stdin.readline())

for _ in range(case):
    floor, room, guest = map(int, sys.stdin.readline().strip('\n').split())
    tmp = guest % floor * 100 + guest // floor + 1
    if guest % floor == 0:
        tmp = floor * 100 + guest // floor
    print(tmp)

# Caution with other condition.
# if guest % floor == 0: condition is for top floor condition.