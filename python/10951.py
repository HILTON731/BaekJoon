# Case 1: Get input until EOF(End Of File). In python use try/except to wait until EOF.
while True:
    try:
        x, y = map(int, input().split())
        if x == 0 and y == 0:
            break
        print(x + y)
    except:
        break

# Case 2: use sys.stdin. sys.stdin if press 'ctrl + z' then your code acknowledge that point is EOF.
import sys
for line in sys.stdin:
    x, y = map(int, line.split())
    print(x + y)