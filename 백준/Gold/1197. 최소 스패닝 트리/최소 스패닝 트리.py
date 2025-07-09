input = __import__('sys').stdin.readline
V,E = map(int,input().split())
#그래프 생성
graph={}
for i in range(1,V+1):
    graph[i]=[]

#간선 생성
def list_ap(st,end,di):
    graph[st].append((end,di))
    graph[end].append((st,di))

for _ in range(E):
    st,end,di=map(int,input().split())
    list_ap(st,end,di)
    
import heapq as hq
heap=[]
visited=set()

def prim(start):
    sum=0
    for com in graph[start]:
        if not com[0] in visited:
            hq.heappush(heap,(com[1],com))
    visited.add(start)
    while heap:
        pop=hq.heappop(heap)
        if pop[1][0] not in visited:
            sum += pop[0]  # 방문하지 않은 정점일 때만 비용 추가
            visited.add(pop[1][0])
            for com in graph[pop[1][0]]:
                if not com[0] in visited:
                    hq.heappush(heap,(com[1],com))      
    return sum

print(prim(1))