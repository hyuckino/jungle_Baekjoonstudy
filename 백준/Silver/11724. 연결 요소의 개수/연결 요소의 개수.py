import sys
sys.setrecursionlimit(100000)

def dfs(start,visited):
    visited.add(start)
    for neighbor in graph[start]:
        if not neighbor in visited:
            dfs(neighbor,visited)
    return 1
    
V,E = map(int,sys.stdin.readline().split())
#그래프 생성
graph={}
for i in range(1,V+1):
    graph[i]=[]

#간선 생성
def list_ap(st,end):
    graph[st].append(end)
    graph[end].append(st)

for _ in range(E):
    st,end=map(int,sys.stdin.readline().split())
    list_ap(st,end)
    
visited = set()
cnt = 0
for i in range(1, V + 1):
    if i not in visited:
        cnt += dfs(i, visited)
print(cnt)