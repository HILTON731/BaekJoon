# case 1

import sys

time = 0

for i in sys.stdin.readline().upper().strip("\n"):
    tmp = ord(i) - ord('A')
    
    if tmp >= 22 and tmp < 26:
        time += 10
    elif tmp >= 19:
        time += 9
    elif tmp >= 15:
        time += 8
    elif tmp >= 12:
        time += 7
    elif tmp >= 9:
        time += 6
    elif tmp >= 6:
        time += 5
    elif tmp >= 3:
        time += 4
    elif tmp >= 0:
        time += 3
    else:
        time += 11

print(time)

# case 2

words = sys.stdin.readline().lower()
s = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']

time = 0
for i in words:
    for j in s:
        if i in j:
            time += s.index(j) + 3
print(time)