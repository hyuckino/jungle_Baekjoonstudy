import sys

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n  # 방문 체크 배열
min_cost = float('inf')

def tsp(start, now, cost, depth):
    global min_cost
    
    if cost >= min_cost:  # 가지치기 (현재 비용이 이미 최소 비용보다 크면 중단)
        return
    
    if depth == n - 1:  # 모든 도시를 방문한 경우
        if arr[now][start] != 0:  # 시작점으로 돌아갈 수 있을 때만 계산
            min_cost = min(min_cost, cost + arr[now][start])
        return

    for i in range(n):
        if not visited[i] and arr[now][i] != 0:  # 방문하지 않았고 갈 수 있는 경로라면
            visited[i] = True
            tsp(start, i, cost + arr[now][i], depth + 1)
            visited[i] = False

# 모든 도시에서 시작해 보기
for i in range(n):
    visited[i] = True
    tsp(i, i, 0, 0)
    visited[i] = False

print(min_cost)