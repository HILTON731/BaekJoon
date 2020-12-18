num = int(input())
tmp = list()
for _ in range(num):
    x, y = map(int, input().split())
    tmp.append(x+y)

for i in tmp:
    print(i)