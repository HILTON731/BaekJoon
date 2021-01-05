import sys

step_size = int(sys.stdin.readline())
step = list(int(sys.stdin.readline()) for _ in range(step_size))
dp = list()

if step_size > 2:
    dp.append(step[0]) # first value selected
    dp.append(dp[0] + step[1]) # second value selected sequentially
    dp.append(max(dp[0] + step[2], step[1] + step[2])) # compare with jump or not when third value select

    for i in range(3, step_size):
        dp.append(max(dp[i-3] + step[i-1] + step[i], dp[i-2] + step[i]))
        # dp[i-3] + step[i-1] + step[i]: value select after previous one selected
        # dp[i-2] + step[i]: value select after jump
    print(dp[-1])
else:
    print(sum(step))
# I couldn't think reccurence relation at all.
# need to practice more.