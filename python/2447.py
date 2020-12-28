# case 1: fill with '*' and remove blank
# def star(i):
#     global arr
#     idx = [i for i in range(n) if(i // 3 ** cna) % 3 == 1]
#     for i in idx:
#         for j in idx:
#             arr[i][j] = " "
# n = int(input())
# v = n
# cnt = 0
# while v != 1:
#     v /= 3
#     cnt += 1

# arr = [["*"] * n for _ in range(n)]
# for cna in range(cnt):
#     star(cna)

# print('\n'.join([''.join([str(i) for i in row]) for row in arr]))

# case 2: drawing with bottom-to-top
# import sys

# num = int(input())

# def stars(i, j):
#     while i!=0:
#         if i % 3 == 1 and j % 3 == 1:
#             sys.stdout.write(' ')
#             return None
#         i = i // 3
#         j = j // 3
#     sys.stdout.write('*')

# for i in range(num):
#     for j in range(num):
#         stars(i, j)
#     sys.stdout.write('\n')

# my solution
# def draw_star(n) :
#     global Map
    
#     if n == 3 :
#         Map[0][:3] = Map[2][:3] = [1]*3
#         Map[1][:3] = [1, 0, 1]
#         return

#     a = n//3
#     draw_star(n//3)
#     for i in range(3) :
#         for j in range(3) :
#             if i == 1 and j == 1 :
#                 continue
#             for k in range(a) :
#                 Map[a*i+k][a*j:a*(j+1)] = Map[k][:a] # 핵심 아이디어
#             for q in Map:
#                 print(q)
#             print()

# N = int(input())      

# # 메인 데이터 선언
# Map = [[0 for i in range(N)] for i in range(N)]

# draw_star(N)

# for i in Map :
#     for j in i :
#         if j :
#             print('*', end = '')
#         else :
#             print(' ', end = '')
#     print()

import sys

num = int(sys.stdin.readline())

Map = [[' ' for _ in range(num)] for _ in range(num)]

def star(num):
    global Map
    if num == 3:
        for i in range(3):
            for j in range(3):
                if i == j == 1:
                    continue
                Map[i][j] = '*'
        return None
    count = num // 3
    star(count)
    for i in range(3):
        for j in range(3):
            for k in range(count):
                if i == j == 1:
                    continue
                Map[count * i + k][count * j: count * (j + 1)] = Map[k][:count]
    return None

star(num)

for i in Map:
    for j in i:
        print(j, end='')
    print()