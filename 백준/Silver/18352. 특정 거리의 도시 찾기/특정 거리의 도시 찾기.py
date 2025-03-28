input = __import__('sys').stdin.readline
from collections import deque
#초기 값 input
N,M,K,X=map(int,input().split())
edges=[]
for _ in range(M):
    edges.append(tuple(map(int,input().split())))


#그래프 정의
def create_graph(edges, directed=True):
  graph = {}
  for u, v in edges:
    if u not in graph:
      graph[u] = []
    if v not in graph:
      graph[v] = []
    graph[u].append(v)
    #무방향인경우, 양방향으로 값 저장
    if not directed:
      graph[v].append(u)
  return graph


graph=create_graph(edges)

# 정점 클래스 정의
class vtx:
    def __init__(self):
        self.visit = False   # 방문 여부
        self.dist = 1000000  # 무한대로 초기화 (거리를 나타내기 위한 값)
        self.pi = None       # 부모 정점 (직전 원소)

def bfs(graph, vertices, start):
    """
    graph: 인접 리스트 형태의 그래프 {정점: [인접 정점, ...]}
    vertices: 정점 이름을 key로 하고 vtx 클래스 인스턴스를 값으로 가지는 딕셔너리
    start: 시작 정점 이름
    """
    queue = deque([start])
    
    # 시작 정점 초기화
    vertices[start].visit = True
    vertices[start].dist = 0

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if not vertices[neighbor].visit:  # 아직 방문하지 않은 인접 정점이면
                vertices[neighbor].visit = True
                vertices[neighbor].dist = vertices[current].dist + 1
                vertices[neighbor].pi = current
                queue.append(neighbor)


# 모든 정점에 대해 vtx 인스턴스를 생성
vertices = {node: vtx() for node in range(1,N+1)}

# 시작점 'A'에서 BFS 실행
bfs(graph, vertices, X)

# 결과 출력: 각 정점의 최단 거리와 부모 정점
result=[]
for node in vertices:
    if vertices[node].dist==K:
        result.append(node)

if result:
    for i in result:
        print(i)
else:
    print(-1)