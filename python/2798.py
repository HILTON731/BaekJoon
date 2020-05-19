from itertools import combinations

cards, num = map(int, input().split())

card_num = list(map(int, input().split()))

every_cases = []

for cases in combinations(card_num, 3):
    sum_of_cases = sum(cases)
    every_cases.append(sum_of_cases)

every_cases.sort(reverse=True)

for i in every_cases:
    if i > num:
        continue
    else:
        break
print(i)
