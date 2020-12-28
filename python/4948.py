import sys
num = 2 * 123456 + 1
tmp = list(True if i > 1 else False for i in range(num) )
for i in range(2, int(num ** 0.5) + 1):
        for j in range(2*i, num, i):
            tmp[j] = False

while True:
    start = int(sys.stdin.readline())
    end = 2 * start
    if start == 0: break
    count = tmp[start + 1:end + 1].count(True)
    print(count)