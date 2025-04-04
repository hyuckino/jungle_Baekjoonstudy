import heapq
def dijkstra_maze(n,maze):
    distances = [[float('inf')]*n for _ in range(n)]
    distances[0][0]=0
    
    q=[]
    heapq.heappush(q,(0,0,0))
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    
    while q:
        current_distance,x,y = heapq.heappop(q)
        
        if x == n-1 and y == n-1:
            return current_distance
        
        for dx,dy in directions:
            nx,ny = x+dx, y+dy
            
            if 0<=nx<n and 0<=ny<n:
                next_distance=current_distance + (0 if maze[nx][ny]==1 else 1)
                if next_distance<distances[nx][ny]:
                    distances[nx][ny] = next_distance
                    heapq.heappush(q,(next_distance,nx,ny))
    return distances[n-1][n-1] 
n=int(input())
maze=[list(map(int,input())) for _ in range(n)]
print(dijkstra_maze(n, maze))  