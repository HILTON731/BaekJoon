import sys

hour, minute = map(int, sys.stdin.readline().split())

if minute - 45 < 0:
    hour -= 1
    if hour < 0:
        hour += 24
    minute += 15
else:
    minute -= 45

print(hour, minute)