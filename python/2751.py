# merge sort v.1
num = int(input())

num_list = []

for i in range(num):
    num_list.append(int(input()))

# def merge_sort(list):
#     if len(list) <= 1:
#         return list
#     mid = len(list) // 2
#     lList = list[:mid]
#     rList = list[mid:]
#     lList = merge_sort(lList)
#     rList = merge_sort(rList)
#     return merge(lList, rList)

# def merge(left, right):
#     result = []
#     while len(left) > 0 or len(right) > 0:
#         if len(left) > 0 and len(right) > 0:
#             if left[0] <= right[0]:
#                 result.append(left[0])
#                 left = left[1:]
#             else:
#                 result.append(right[0])
#                 right = right[1:]
#         elif len(left) > 0:
#             result.append(left[0])
#             left = left[1:]
#         elif len(right) > 0:
#             result.append(right[0])
#             right = right[1:]
#     return result

# # merge sort v.2            
# v = [int(input()) for i in range(int(input()))]

# def merge(left, right) :
#     v=list()
#     i=0;j=0
#     while(i<len(left) and j<len(right)) :
#         if left[i]<=right[j] :
#             v.append(left[i])
#             i+=1
#         else :
#             v.append(right[j])
#             j+=1
#     if i==len(left) : v = v + right[j:len(right)]
#     if j == len(right): v = v + left[i:len(left)]
#     return v
 
# def merge_sort(v) :
#     if len(v) <= 1 : return v
#     m = len(v)//2
#     left = merge_sort(v[0:m])
#     right = merge_sort(v[m:len(v)])
#     return merge(left, right)

# m = merge_sort(num_list)
# print(*m, sep="\n")

# # quick sort v.1

# q_list = [int(input()) for i in range(int(input()))]

# def quick_sort(qlist):
#     if len(qlist) <= 1:
#         return qlist
#     pivot = qlist[0]
#     lList = [num for num in qlist if pivot > num]
#     rList = [num for num in qlist if pivot < num]
#     List = [num for num in qlist if pivot == num]
#     return quick_sort(lList)+List+quick_sort(rList)
# print(quick_sort(q_list))

# # qucik sort v.2
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     lesser_arr, equal_arr, greater_arr = [], [], []
#     for num in arr:
#         if num < pivot:
#             lesser_arr.append(num)
#         elif num > pivot:
#             greater_arr.append(num)
#         else:
#             equal_arr.append(num)
#     return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

import sys

Num = int(sys.stdin.readline())
result = list()

for i in range(Num):
    result.append(int(sys.stdin.readline()))

for i in sorted(result):
    sys.stdout.write(str(i)+'\n')