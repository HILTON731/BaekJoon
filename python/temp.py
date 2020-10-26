def bin2(n, k):
    # temp = [[0 for i in range(k + 1)] for i in range(n + 1)]
    # temp = [[0] * (k + 1)] * 2
    temp = [[0 for i in range(k + 1)] for i in range(2)]
    count = 0
    for i in range(n+1):
        col = min(i,k)
        for j in range(col + 1):
            floor = i%2
            # print('floor',floor)
            if(j == 0 or j == i):
                temp[floor][j] = 1
            else:
                temp[floor][j] = temp[1-floor][j-1] + temp[1-floor][j]
            count += 1
    return temp[n%2][k]
print(bin2(5, 3))
