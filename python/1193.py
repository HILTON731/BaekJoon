import sys

# case 1: time out
# num = int(sys.stdin.readline())

# tmp = [1,1]
# count = 1

# while True:
#     for _ in range(count):
#         tmp[count % 2] += 1
#         if tmp[(count + 1) % 2] != 1:
#             tmp[(count + 1) % 2] -= 1
#         num -= 1
#         if num == 1:
#             print("{}/{}".format(tmp[0],tmp[1]))
#             break
#     count += 1
#     if num == 1:
#         break

# case 2:
num = int(sys.stdin.readline().strip("\n"))
count = 0

while num > 0:
    num -= count
    count += 1

num = count + num - 1
result = str(num)+'/'+str(count - num)
if count % 2 == 0:
    result = str(count - num) + '/' + str(num)

print(result)

# 1/1 --> 1/2 --> 2/1 --> 3/1 --> 2/2 --> 1/3 --> 1/4 --> 2/3 --> 3/2 --> 4/1 --> 5/1
# start --> ri --> le --> le --> ri --> ri --> ri --> le --> le --> le --> le