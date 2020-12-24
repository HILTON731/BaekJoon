import sys

word = sys.stdin.readline().strip("\n").lower()
tmp = ' '
tmp_num = 0

for i in list(set(word)):
    if word.count(tmp) < word.count(i):
        tmp = i
        tmp_num = word.count(i)
    elif word.count(tmp) == word.count(i):
        tmp_num = -1

if tmp_num == -1:
    print('?')
else:
    print(chr(ord(tmp)-32))

# lower(): Make input string lower.