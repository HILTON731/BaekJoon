import sys

num = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
asc = [0] * num
dsc = [0] * num
tmp = [0] * num

for i in range(num):
    for j in range(i):
        if num_list[i] > num_list[j] and asc[i] < asc[j]:
            asc[i] = asc[j]
    
    asc[i] += 1

for i in range(num-1,0,-1):
    for j in range(num-1, i, -1):
        if num_list[i] > num_list[j] and dsc[i] < dsc[j]:
            dsc[i] = dsc[j]
    dsc[i] += 1
if num == 1:
    print(1)
else:
    print(max(list(map(lambda x: sum(x) - 1,list(zip(asc,dsc))))))