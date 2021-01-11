import sys

time = sum([int(sys.stdin.readline()) for _ in range(4)])
print("{}\n{}".format(time//60, time%60))