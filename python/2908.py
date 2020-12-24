import sys

print(max(map(int, sys.stdin.readline()[::-1].split())))

# [<start of index>:<end of index>:<step size>]
# if step size is -1 it read reverse order