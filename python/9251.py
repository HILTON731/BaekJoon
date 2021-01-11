import sys
input = sys.stdin.readline


tmpA = list(input().strip().upper())
tmpB = list(input().strip().upper())
check = [[0] * (len(tmpB)+1) for _ in range(len(tmpA)+1)]

if len(tmpA) * len(tmpB) == 0:
    print(0)
else:
    for i in range(1, len(tmpA)+1):
        for j in range(1, len(tmpB)+1):
            check[i][j] = max(check[i-1][j], check[i][j-1], check[i-1][j-1] + (tmpA[i-1] == tmpB[j-1]))
    print(check[len(tmpA)][len(tmpB)])
        
# reference: https://twinw.tistory.com/126, https://reakwon.tistory.com/67
# 2 dimensional memory means compare of string bound of index each side