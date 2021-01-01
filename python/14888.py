import sys

num = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))
max_num = 0
min_num = 1000000001
tmp = num_list[0]

operator = {0:lambda x, y: x + y, 1:lambda x, y: x - y, 2:lambda x, y: x * y, 3:lambda x, y: x / y}

def operation(count):
    global max_num, min_num, tmp
    if count == num - 1:
        max_num = max(max_num, tmp)
        min_num = min(min_num, tmp)
        return
    else:
        for i in range(4):
            if not op[i]:
                continue
            else:
                op[i] -= 1
                tmp = operator[i](tmp, num_list[count + 1])
                operation(count + 1)
                op[i] += 1
                if i % 2 == 0:
                    tmp = operator[i+1](tmp, num_list[count + 1])
                else:
                    tmp = operator[i-1](tmp, num_list[count + 1])

operation(0)
print(int(max_num))
print(int(min_num))
