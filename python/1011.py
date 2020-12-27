import sys

# case 1: with some rules --> use repeat rules
for _ in range(int(sys.stdin.readline())):
    start, end = map(int, sys.stdin.readline().split())
    dist = end - start
    count = 0 # 이동 횟수
    move = 1 # count 별 이동 가능 거리
    movesum = 0 # 이동 거리 합
    while movesum < dist:
        count += 1
        movesum += move
        if count % 2 == 0: # move가 두번씩 반복되어 나타나는 특성에 의해
            move += 1
    print(count)

# case 2: with square method --> use math problems                
for _ in range(int(sys.stdin.readline())):
    start, end = map(int, sys.stdin.readline().split())
    dist = end - start
    squarenum = int(dist ** 0.5) # Get closest square number with distance
    if squarenum ** 2 == dist:
        print(2 * squarenum - 1) # if distance is square number
    elif dist <= squarenum ** 2 + squarenum:
        print(squarenum * 2) # distance is between square number and square number + 1
    else:
        print(2 * squarenum + 1) # distance over square number + 1

# 1 (1) 1
# 2 (2) 1 --> 1
# 3 (3) 1 --> 1 --> 1
# 4 (3) 1 --> 2 --> 1
# 5 (4) 1 --> 2 --> 1 --> 1
# 6 (4) 1 --> 2 --> 2 --> 1
# 7 (5) 1 --> 2 --> 2 --> 1 --> 1
# 8 (5) 1 --> 2 --> 2 --> 2 --> 1
# 9 (5) 1 --> 2 --> 3 --> 2 --> 1
# 10 (6) 1 --> 2 --> 3 --> 2 --> 1 --> 1
# 11 (6) 1 --> 2 --> 3 --> 2 --> 2 --> 1
# 12 (6) 1 --> 2 --> 3 --> 3 --> 2 --> 1
# 13 (7) 1 --> 2 --> 3 --> 3 --> 2 --> 1 --> 1
# 14 (7) 1 --> 2 --> 3 --> 3 --> 2 --> 2 --> 1
# 15 (7) 1 --> 2 --> 3 --> 3 --> 3 --> 2 --> 1
# 16 (7) 1 --> 2 --> 3 --> 4 --> 3 --> 2 --> 1