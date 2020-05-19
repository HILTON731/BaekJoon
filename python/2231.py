# My answer
div_sum = int(input())

list_num = []

for i in range(div_sum):
    value = i
    num = i
    while num >= 1:
        value += num % 10
        num = int(num / 10)
    if value == div_sum:
        print(i)
        break
if i == div_sum - 1:
    print(0)

# Other answer
n = int(input())
ans = 1000001
for i in range(1, n):
    k = i
    for j in list(str(i)):
        k += int(j)
    if k == n:
        ans = min(ans, i)

if ans == 1000001:
    print(0)
else:
    print(ans)