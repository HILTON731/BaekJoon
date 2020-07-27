while True:
    col, row = map(int, input().split())
    if row * col == 0:
        break
    temp = [list(map(int,input().split())) for _ in range(row)]
    step = [0, -1, 1]
    count = 0
    def island(ro, co):
        for s in step:
            for sc in step:
                if ro+s >= row or ro+s < 0 or co+sc >= col or co+sc < 0:
                    continue
                elif temp[ro+s][co+sc] == 1:
                    temp[ro+s][co+sc] = 2
                    island(ro+s, co+sc)

    for r in range(row):
        for c in range(col):
            if temp[r][c] == 1:
                island(r, c)
                count += 1
    print(count)