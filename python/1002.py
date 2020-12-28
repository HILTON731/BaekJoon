import sys
import math

for _ in range(int(sys.stdin.readline())):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    R = [r1, r2, distance]
    maxr = max(R)
    R.remove(maxr)
    sumr = sum(R)
    print(-1 if r1 == r2 and distance == 0 else 1 if (distance == r1+r2 or maxr==sumr) else 0 if (maxr > sumr) else 2)