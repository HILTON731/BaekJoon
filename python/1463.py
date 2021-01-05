import sys

num = int(sys.stdin.readline())
dp = [num]
count = 0

def operation(num_list):
    tmp = list()
    for i in num_list:
        tmp.append(i-1)
        if not i % 3:
            tmp.append(i / 3)
        if not i % 2:
            tmp.append(i / 2)
    return tmp

while True:
    if 1 in dp:
        print(count)
        break
    dp = operation(dp)
    count += 1

# many ways of using memories.
# in this case you can't know that which operation is best.
# so must operate all cases.
# this is another way of making function in dynamic programming problems.
# could use every case of operation in memory and check is there a result.
# in this case memory role in storage of operations so it works.