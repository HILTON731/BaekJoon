import sys

tmp = list(-1 for _ in range(26))

word = sys.stdin.readline().strip("\n")

for i in word:
    tmp[ord(i) - ord('a')] = word.index(i)

for i in tmp:
    print(i, end=' ')

# ord(): Casting char to int(ASCII)