from heapq import heappop, heappush
input = __import__('sys').stdin.readline
def dijkstra(graph, start, end=None):
    n = len(graph)
    
    heap = [(0,start)]
    seen = set()
    d = [float('inf')] * n
    d[start] = 0
    
    while heap:
        _, curr = heappop(heap)
        if curr in seen:
            continue
        seen.add(curr)
        for child, w in graph[curr]:
            if d[curr] + w < d[child]:
                d[child] = d[curr] + w
                heappush(heap, (d[child], child))
                
    if end!=None:
        return d[end]
    return 0
# graph 생성
graph={}
N=int(input())
for i in range(N):
    graph[i]=[]
M=int(input())
for _ in range(M):
    a,b,c=map(int,input().split())
    graph[a-1].append((b-1,c))
    
start,end=map(int,input().split())

tmp=dijkstra(graph, start-1,end-1)
print(tmp)