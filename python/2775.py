import sys

for _ in range(int(sys.stdin.readline())):
    k = int(sys.stdin.readline().strip('\n')) # floor
    n = int(sys.stdin.readline().strip('\n')) # address

    tmp = [[i for i in range(1, n+1)] for _ in range(2)]

    for i in range(k+1):
        for j in range(n):
            tmp[(i+1)%2][j] = sum(tmp[i%2][:(j+1)])

    print(tmp[k%2][n-1])

# Use dynamic programming with space complexity O(1)