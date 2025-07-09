from collections import deque
import sys

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, x, y = map(int, input().split())  # x, y는 1씩 빼줘야 함
direction = [[-1,0],[1,0],[0,-1],[0,1]]

def check(target):
    dq = deque()
    # 초기 바이러스 좌표를 바이러스 번호 기준으로 정렬하여 dq에 넣기
    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                dq.append((arr[i][j], i, j))
    dq = deque(sorted(dq))
    
    time = 0
    while dq:
        if time == target:
            return arr[x-1][y-1]
        # 현재 레벨에 있는 모든 상태를 처리
        for _ in range(len(dq)):
            t, i, j = dq.popleft()
            for dx, dy in direction:
                ni, nj = i + dx, j + dy
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
                    arr[ni][nj] = t
                    dq.append((t, ni, nj))
        time += 1
    return arr[x-1][y-1]

print(check(S))
    
    
    