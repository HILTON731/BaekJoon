num = int(input())

def square(n):
    lst = list()
    for i in range(n+1):
        if i < 3:
            lst.append(i)
        else:
            lst.append(lst[i-1]+lst[i-2])
    print(lst[n] % 10007)

square(num)