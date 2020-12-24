import sys

s = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for tmp in sys.stdin:
        
    tmp = tmp.strip("\n")
    remove = 0

    for letter in s:
        remove += tmp.count(letter)
        
    print(len(tmp) - remove)