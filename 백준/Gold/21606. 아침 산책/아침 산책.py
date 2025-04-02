
n=int(input())
info=[0]+list(map(int,input()))
graph={}
for i in range(1,n+1):
    graph[i]=[]
for _ in range(n-1):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)   
    
result=0
for i in range(1,n+1):
    if not info[i]==0:
        for j in graph[i]:
            if info[j]!=0:
                result+=1
                
clusters=[]
visited=[False]*(n+1)
def dfs(node, cluster):
    visited[node] = True
    cluster.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor] and info[neighbor] == 0:
            dfs(neighbor, cluster)

for i in range(1, n+1):
    if info[i] == 0 and not visited[i]:
        cluster = []
        dfs(i, cluster)
        clusters.append(cluster)
for arr in clusters:
    tmp=0
    for i in arr:
        for j in graph[i]:
            if info[j]!=0:
                tmp+=1
    result+=tmp*(tmp-1)
print(result)