import sys

# num = int(sys.stdin.readline())
# tmp = list(map(int, sys.stdin.readline().split()))
# count = [0] * num

# for i in range(num):
#     for j in range(i):
#         if tmp[i] > tmp[j] and count[i] < count[j]:
#             count[i] = count[j]
#     count[i] += 1
# print(max(count))

num = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
check = [0] * num

for i in range(num):
    for j in range(i):
        if num_list[i] > num_list[j] and check[i] < check[j]:
            check[i] = check[j]
    check[i] += 1

print(max(check))