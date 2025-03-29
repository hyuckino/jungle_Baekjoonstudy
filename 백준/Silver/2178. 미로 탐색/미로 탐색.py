input = __import__('sys').stdin.readline
from collections import deque
N,M = map(int,input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph={}
for i in range(N):
    for j in range(M):
        graph[(i,j)]=[]

arr = []     
for _ in range(N):
    arr.append(list(map(int,input().strip())))
    

#상하좌우 체크후 추가
def check(arr,i,j):
    for direction in range(4):
        nx, ny = i + dx[direction], j +dy[direction]
        if 0 <= nx < N and 0 <= ny < M:
            if arr[nx][ny] == 1:    
                graph[(i,j)].append((nx,ny))
#그래프 만들기        
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            check(arr,i,j)
            
#출력
def bfs(start, target):
    # 방문 여부와 거리를 저장할 딕셔너리 (이미 방문한 노드: 거리)
    dist = {start: 1}
    
    # BFS를 위한 큐 초기화
    queue = deque([start])
    
    while queue:
        current = queue.popleft()
        # 목표 노드에 도달하면 거리를 반환
        if current == target:
            return dist[current]
        # 인접 노드 순회
        for neighbor in graph[current]:
            if neighbor not in dist:  # 아직 방문하지 않았다면
                dist[neighbor] = dist[current] + 1
                queue.append(neighbor)

# 예를 들어 시작점 (0,0)에서 도착점 (N-1, M-1)까지의 최소 거리 계산
start = (0, 0)
target = (N-1, M-1)
result = bfs(start, target)
print(result)