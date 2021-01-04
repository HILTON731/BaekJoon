import sys

# def w(a, b, c):
#     if a == b == c == -1:
#         sys.exit(0)
#     elif a <= 0 or b <= 0 or c <= 0:
#         return 1
#     elif a > 20 or b > 20 or c > 20:
#         return w(20, 20, 20)
#     else:
#         for i in range(1, a + 1):
#             for j in range(1, b + 1):
#                 for k in range(1, c + 1):
#                     if i < j and j < k:
#                         tmp[i][j][k] = tmp[i][j][k-1] + tmp[i][j-1][k-1] - tmp[i][j-1][k]
#                     else:
#                         tmp[i][j][k] = tmp[i-1][j][k] + tmp[i-1][j-1][k] + tmp[i-1][j][k-1] - tmp[i-1][j-1][k-1]

#         return tmp[a][b][c]

def w(a, b, c):
    if a == b == c == -1:
        sys.exit(0)
    elif a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif tmp[a][b][c]:
        return tmp[a][b][c]
    elif a < b < c:
        tmp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return tmp[a][b][c]
    else:
        tmp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return tmp[a][b][c]


tmp = [[[0] * 21 for _ in range(21)] for __ in range(21)]
for i in range(21):
    for j in range(21):
        tmp[0][i][j] = tmp[i][0][j] = tmp[i][j][0] = 1

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    tmp = w(a, b, c)
    print("w({}, {}, {}) = {}".format(a, b, c, tmp))
