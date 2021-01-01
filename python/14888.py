import sys

num = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
op = list(map(int, sys.stdin.readline().split()))
max_num = -sys.maxsize - 1
min_num = sys.maxsize
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
                tmp_loc = operator[i](tmp, num_list[count + 1])
                tmp = int(tmp_loc)
                operation(count + 1)
                op[i] += 1
                if i % 2 == 0:
                    tmp = operator[i+1](tmp_loc, num_list[count + 1])
                else:
                    tmp = operator[i-1](tmp_loc, num_list[count + 1])

operation(0)
print(max_num)
print(min_num)

# print((((int((1 - 2) / 3) + 4) + 5) * 6))
# print(((int(((1 + 2) + 3) / 4) - 5) * 6))