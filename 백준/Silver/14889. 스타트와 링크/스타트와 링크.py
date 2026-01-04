from itertools import combinations,permutations
N = int(input())
board = []
for _ in range(N):
    temp = list(map(int,input().split()))
    board.append(temp) # 가로세로 조회방향에 따라 속도 차이가 생기지 않나?
data = tuple(range(1, N + 1))
flag = 1

result = list(combinations(data,int(len(data)/2)))
sol = []
for i in result:
    start = list(permutations(i,2))
    start_sum, link_sum = 0, 0
    for j in start:
        start_sum += board[j[0]-1][j[1]-1]
    link = list(permutations([x for x in data if x not in i],2))
    for k in link:
        link_sum += board[k[0]-1][k[1]-1]
    diff = abs(start_sum-link_sum)
    if diff==0:
        print(0)
        flag = 0
        break
    else:
        sol.append(diff)
if sol and flag:  
    print(min(sol))