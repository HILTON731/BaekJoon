import sys
input = sys.stdin.readline


tmpA = input().strip().upper()
tmpB = input().strip().upper()
check = [[0] * (len(tmpA)+1) for _ in range(len(tmpB)+1)]

for i in range(1, len(tmpA)+1):
    for j in range(1, len(tmpB)+1):
        check[i][j] = max(check[i-1][j], check[i][j-1], check[i-1][j-1] + (tmpA[i-1] == tmpB[j-1]))
print(check[-1][-1])
        
# reference: https://twinw.tistory.com/126, https://reakwon.tistory.com/67
# 2 dimensional memory means compare of string bound of index each side
# 