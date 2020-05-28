# num = int(input())

# num_list = []

# for i in range(num):
#     num_list.append(int(input()))

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
            
v = [int(input()) for i in range(int(input()))]

def merge(left, right) :
    v=list()
    i=0;j=0
    while(i<len(left) and j<len(right)) :
        if left[i]<=right[j] :
            v.append(left[i])
            i+=1
        else :
            v.append(right[j])
            j+=1
    if i==len(left) : v = v + right[j:len(right)]
    if j == len(right): v = v + left[i:len(left)]
    return v
 
def merge_sort(v) :
    if len(v) <= 1 : return v
    m = len(v)//2
    left = merge_sort(v[0:m])
    right = merge_sort(v[m:len(v)])
    return merge(left, right)

m = merge_sort(v)
print(*m, sep="\n")