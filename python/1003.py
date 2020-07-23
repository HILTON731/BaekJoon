num = int(input())
count = list()
for i in range(num):
    count.append(int(input()))
result = list()
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fst = fib(n - 1)
        sec = fib(n - 2)
        if fst < 2:
            temp.append(fst)
        if sec < 2:
            temp.append(sec)
        return fst + sec
for n in count:
    temp = list()
    fib(n)
    result.append([temp.count(0), temp.count(1)])

print(result)