import sys


num = int(sys.stdin.readline())
for _ in range(num):
    
    tmp = list()
    count = 0
    string = sys.stdin.readline().strip("\n")
    
    for i in string:
        if tmp.count(i) == 0 or tmp[-1] == i:
            tmp.append(i)
        else:
            count = -1
            break
    num += count

print(num)