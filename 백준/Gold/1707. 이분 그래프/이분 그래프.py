import sys

sys.setrecursionlimit(20000)
input = sys.stdin.readline


def dfs(start, group):
    global error
    
    if error:
        return
    
    visited[start] = group   
    for neighbor in graph[start]:
        if not visited[neighbor]:  # 아직 방문하지 않은 노
            dfs(neighbor,-group)
        elif visited[neighbor] == visited[start]:
            error=True# 같은 색으로 방문했으면, 이분 그래프가 아님
            return 
        
K=int(input())
for _ in range(K):
    V,E = map(int,input().split())
    graph={}
    for i in range(1,V+1):
        graph[i]=[]
    for _ in range(E):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
                      

        
    visited=[False]*(V+1)
    error=False
    
    for i in range(1, V + 1):
            if not visited[i]:  # 만약 아직 방문하지 않았다면
                dfs(i,1)  # dfs를 돈다.
                if error:  # 만약 에러가 참이라면
                    break  # 탈출

    if error:
        print('NO')
    else:
        print('YES')

#### 1, 2 방향 그래프일 때 예외처리 고민 1 돌고 2->1 방향만 있을때 2 다시 돌아서 1
##됨 근데 1 값 이미 1 그래서 false인데 이거 예외 처리