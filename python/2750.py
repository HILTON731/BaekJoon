num = int(input())

num_list = []

for i in range(num):
    num_list.append(int(input()))

# Selection sort
def selection_sort():
    for i in range(num-1):
        first = i
        for j in range(i,num):
            if num_list[j] < num_list[first]:
                first = j    
        num_list[i], num_list[first] = num_list[first], num_list[i]
            
# Insertion sort
def insert_sort():
    for i in range(1, len(num_list)):
        j = i - 1
        key = num_list[i]
        while num_list[j] > key and j >= 0:
            num_list[j+1] = num_list[j]
            j = j - 1
        num_list[j+1] = key

def bubble_sort():
    length = len(num_list)-1
    for i in range(length):
        for j in range(length-i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

for i in range(num):
    print(num_list[i])