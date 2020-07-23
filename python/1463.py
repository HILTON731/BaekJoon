# X = int(input())
# count = 0
# result = [X]
# def calculation(x):
#     lst = []
#     for i in x:
#         lst.append(i-1)
#         if i%3 ==0:
#             lst.append(i/3)
#         if i%2 ==0:
#             lst.append(i/2)
#     lst = set(lst)
#     lst = list(lst)
#     return lst
# while True:
#     if X == 1:
#         break
#     temp = result
#     result = []
#     result = calculation(temp)
#     count += 1
#     if min(result) == 1:
#         break
# print(count)

n = int(input())
result = [n]
count = 0
def counter(numbers):
    lst = list()
    for num in numbers:
        lst.append(num-1)
        if num % 3 == 0:
            lst.append(num/3)
        if num % 2 == 0:
            lst.append(num/2)
    lst = set(lst)
    lst = list(lst)
    return lst

while True:
    if min(result) == 1:
        print(count)
        break
    result = counter(result)
    count += 1
