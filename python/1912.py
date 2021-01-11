import sys

# My answer: timeout occur

size = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
tmp = [0] * size

maxnum = - sys.maxsize

for i in range(size):
    for j in range(size-i):
        tmp[j] += num_list[i+j]
        if tmp[j] > maxnum:
            maxnum = tmp[j]
print(maxnum)

# Correct

size = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
tmp = [num_list[0]]
for i in range(size-1):
    tmp.append(max(tmp[i] + num_list[i+1], num_list[i+1]))
print(max(tmp))

# get numbers by list in num_list and make new list.
# put num_list first argument in tmp for compare.
# compare with tmp[i] + num_list[i+1] and num_list[i+1] and put tmp a bigger one.
# print biggest number in tmp.