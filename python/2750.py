num = int(input())

num_list = []

for i in range(num):
    num_list.append(int(input()))

for i in range(num-1):
    first = i
    for j in range(i,num):
        if num_list[j] < num_list[first]:
            first = j    
    if i != first:
        temp = num_list[first]
        num_list[first] = num_list[i]
        num_list[i] = temp
for i in range(num):
    print(num_list[i])
            