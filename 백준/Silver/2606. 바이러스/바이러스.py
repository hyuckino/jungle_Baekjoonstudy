graph={}
N=int(input())
for i in range(1,N+1):
    graph[i]=[]
M=int(input())
for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
#====================================== 그래프

def dfs(start,visited,result):
    visited[start]=True
    result.append(start)   
    for i in graph[start]:
        if not visited[i]:
            dfs(i,visited,result)
    return result
visited=[False]*(N+1)
print(len(dfs(1,visited,[]))-1)