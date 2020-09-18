import sys
temp = list(map(int, sys.stdin.readline().rstrip()))
temp.sort(reverse=True)
print("".join(map(str,temp)))