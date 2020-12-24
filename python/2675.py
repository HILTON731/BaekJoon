import sys

for _ in range(int(sys.stdin.readline().strip("\n"))):
    tmp, string = sys.stdin.readline().split()

    for i in string:
        for _ in range(int(tmp)):
            sys.stdout.write(i)
    sys.stdout.write("\n")
