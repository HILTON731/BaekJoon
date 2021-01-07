import sys
input = lambda: sys.stdin.readline().strip()
num = int(input())
glasses = list(int(input()) for _ in range(num))
dp = list()


if num < 3:
    print(sum(glasses))
else:
    dp.append(glasses[0])
    dp.append(dp[0] + glasses[1])
    dp.append(max(dp[1], dp[0]+glasses[2],glasses[1] + glasses[2]))

    for i in range(3,num):
        dp.append(max(dp[i-1], dp[i-3] + glasses[i-1] + glasses[i], dp[i-2] + glasses[i]))

    print(dp[-1])

# same pattern with # 2579 except last value select is not essential.