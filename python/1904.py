# case 1
import sys
from itertools import product

count = 0
binary = ''

length = int(sys.stdin.readline())

for i in list(product(['0','1'],repeat=length)):
    tmp = ''.join(i)
    # print(tmp, tmp.count('0'))
    if tmp.count('0') % 2 == 0 and '00' in tmp or '0' not in tmp:
        count+=1
        print(tmp)

print(count%15746)

# case 2
import sys

tmp = [0] * 1000001

length = int(sys.stdin.readline())
tmp[1], tmp[2] = 1, 2
for i in range(3, length+1):
    tmp[i] = (tmp[i-1] + tmp[i-2])%15746

print(tmp[length])