p = int(input())

size_p = []

for i in range(p):
    size = tuple(map(int, input().split()))
    size_p.append(size)

for i in size_p:
    rank = 1
    for j in size_p:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = " ")