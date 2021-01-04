import sys

size = int(sys.stdin.readline())
triangle = list(list(map(int, sys.stdin.readline().split())) for _ in range(size))

for i in range(1, size):
    for j in range(i+1):
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
        elif j == i:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j-1:j+1])
print(max(triangle[size-1]))

# Need to organize reccurence relation.