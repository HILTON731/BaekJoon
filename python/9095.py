count = int(input())

# num = list(map(int, input().split()))
num = list()
for i in range(count):
    num.append(int(input()))
result = list()
def calculate(lst):
    temp = []
    for n in lst:
        if n > 0:
            temp.append(n - 1)
        if n > 1:
            temp.append(n - 2)
        if n > 2:
            temp.append(n - 3)
        elif n == 0:
            temp.append(n)
    return temp


for n in num:
    temp = [n]
    while True:
        temp = calculate(temp)
        if sum(temp) == 0:
            result.append(len(temp))
            break
for t in result:
    print(t)       