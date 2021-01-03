import sys

size = int(sys.stdin.readline())
num_list = list()
for _ in range(size):
    num_list.append(list(map(int,sys.stdin.readline().split())))
min_size = sys.maxsize
team_a = [i for i in range(1, size)]
team_b = [0]
print(team_a, team_b)

def potential():
    res = 0
    for i in team_a:
        for j in team_a:
            if i < j:
                res += (num_list[i][j] + num_list[j][i])
            else:
                break
    for i in team_b:
        for j in team_b:
            if i < j:
                res -= (num_list[i][j] + num_list[j][i])
            else:
                break
    print('potential', res)
    return res
            
def tracking(count):
    global min_size
    if count == size // 2 - 1:
        tmp = potential()
        min_size = min(min_size, tmp)
        print(min_size, team_a, team_b)
        return
    else:
        for i in team_a:
            if team_b[-1] < i:
                team_b.append(i)
                team_a.remove(i)
                
                tracking(count + 1)
                
                team_a.append(i)
                team_b.remove(i)

tracking(0)
print(min_size)