import sys
import numpy as np

N, M = map(int, sys.stdin.readline().split())

num_list = list(range(1, N + 1))
check_list = [False] * N
arr = list()

def dfs(count):

    if(count == M):
        print(arr)
        return
    
    for i in range(N):
        if(check_list[i]):
            continue

        check_list[i] = True
        arr.append(num_list[i])

        dfs(count + 1)
        arr.pop()

        # print(arr)
        # print(check_list)

        check_list[i] = False

dfs(0)
