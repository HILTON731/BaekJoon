import sys

while True:
    try:
        dest = int(sys.stdin.readline()) - 1
        count = 0

        while True:
            dest -= 6 * count
            if dest <= 0:
                print(count + 1)
                break
            count += 1
    except:
        break