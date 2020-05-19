# first
people_num = int(input())
time_sort = list(map(int, input().split()))

time_sort.sort()

temp = 0

for i in range(people_num):
    sum = 0
    for j in range(i + 1):
        sum = sum + time_sort[j]
    temp = temp + sum

print(temp)

# second
people_num = int(input())
time_sort = list(map(int, input().split()))
time_sort.sort()
sum_val = time_sort[0]

for i in range(1,people_num):
    sum_val += sum(time_sort[:i+1])

print(sum_val)

# third
people_num = int(input())
time_sort = list(map(int, input().split()))
time_sort.sort()
sum_val = 0
for i in range(people_num):
    sum_val += sum(time_sort[:i+1])

print(sum_val)