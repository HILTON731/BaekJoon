# Case 1: Compare max value every loop.
import sys

index = 0
temp = 0
for i in range(9):
    
    val = int(sys.stdin.readline())
    
    if temp < val:
        temp = val
        index = i + 1
print(temp)
print(index)

# Case 2: put every value in array. sort it and find max value and index by array function.
tmp = list()

for _ in range(9):
    tmp.append(int(sys.stdin.readline()))

print(max(tmp))
print(tmp.index(max(tmp)) + 1)