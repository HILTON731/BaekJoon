import sys

tmp = list(int(sys.stdin.readline()) for _ in range(2))

print(sum(tmp))
print(tmp[0] - tmp[1])
print(tmp[0] * tmp[1])