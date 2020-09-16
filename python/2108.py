import sys
from collections import Counter

num = [int(sys.stdin.readline()) for i in range(int(sys.stdin.readline()))]
length = len(num)

def avg(num):
    return round(sum(num)/length)

def mid(num):
    return sorted(num)[length//2]

def lot(num):
    temp = list()
    num_set = list(set(sorted(num)))
    num_dict = {i : num.count(i) for i in num_set}
    max_count = max(num_dict.values())
    for k, v in num_dict.items():
        if v == max_count:
            temp.append(k)
    temp.sort()
    print(temp)
    if len(temp) == 1:
        return temp[0]
    else:
        return temp[1]


def mode(x):
    mode_dict = Counter(x)
    modes = mode_dict.most_common()
    if len(x) > 1 : 
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else : 
            mod = modes[0][0]
    else : 
        mod = modes[0][0]
    
    return mod

def bound(num):
    return max(num) - min(num)

print(avg(num))
print(mid(num))
print(lot(num))
print(bound(num))