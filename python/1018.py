N, M = map(int, input().split())

count = []
board = [list(input()) for _ in range(N)]

for i in range(N-7):
    for j in range(M-7):
        # print("({},{})\n".format(i,j))
        temp_odd = [0,0]
        temp_even = [0,0]
        for k in range(i,i+8):
            # print(board[k][j:j+8])
            if k%2==0:
                temp_odd[0] += board[k][j:j+8:2].count('B') # 홀수줄의 홀수번째 B의 개수
                temp_even[0] += board[k][j+1:j+8:2].count('B') # 홀수줄의 짝수번째 B의 개수
            else:
                temp_odd[1] += board[k][j:j+8:2].count('B') # 짝수줄의 홀수번째 B의 개수
                temp_even[1] += board[k][j+1:j+8:2].count('B') # 짝수줄의 짝수번째 B의 개수

        odd_W = 16 + temp_odd[0] - temp_even[0] # 홀수번째 줄에서 W부터 시작
        odd_B = 16 + temp_even[0] - temp_odd[0] # 홀수번재 줄에서 B부터 시작
        even_W = 16 + temp_odd[1] - temp_even[1] # 짝수번째 줄에서 W부터 시작
        even_B = 16 + temp_even[1] - temp_odd[1] # 짝수번째 줄에서 B부터 시작
        # print("odd_W: {}, odd_B: {}, even_W: {}, even_B: {}\n".format(odd_W,odd_B,even_W,even_B))
        count.append(min(odd_W + even_B,odd_B + even_W))       
        # print(count)
print(min(count))

