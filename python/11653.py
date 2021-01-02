import sys

num = int(sys.stdin.readline())
# Case 1:
def prime(num):
    for i in range(2,num + 1):
        if num % i == 0:
            print(i)
            prime(num // i)
            break

prime(num)

# Case 2:
i = 2
while num!=1:
    if num % i == 0:
        num /= i
        print(i)
    else: i += 1
