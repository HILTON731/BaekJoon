# first
num = int(input())
number_list = list(map(int, input().split()))
number_list.sort()
print(number_list[0], number_list[-1])

# second
num = int(input())
num_list = list(map(int, input().split()))
print("{} {}".format(min(num_list), max(num_list)))