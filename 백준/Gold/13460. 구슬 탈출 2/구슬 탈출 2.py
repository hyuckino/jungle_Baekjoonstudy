from collections import deque

# 입력
N, M = map(int, input().split())
board = []
for i in range(N):
    row = list(input().rstrip())
    for j, ch in enumerate(row):
        if ch == 'R':
            Rx, Ry = i, j
            row[j] = '.'
        elif ch == 'B':
            Bx, By = i, j
            row[j] = '.'
    board.append(row)

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상,하,좌,우

def roll(x,y,dx,dy):
    steps = 0
    while True:
        nx, ny = x + dx, y + dy
        if board[nx][ny] == '#':
            return x, y, steps, False
        if board[nx][ny] == 'O':
            return nx, ny, steps + 1, True
        x, y = nx, ny
        steps += 1
        
def solve():
    q = deque()
    q.append((Rx, Ry, Bx, By, 0))
    visited = set()
    visited.add((Rx, Ry, Bx, By))
    
    while q:
        rx, ry, bx, by, depth = q.popleft()
        if depth >= 10:
            continue
        
        for dx,dy in directions:
            nrx, nry, rdist, r_hole = roll(rx, ry, dx, dy)
            nbx, nby, bdist, b_hole = roll(bx, by, dx, dy)
            
            if b_hole:
                continue
            
            if r_hole:
                return depth + 1
            
            if nrx == nbx and nry == nby:
                if rdist > bdist:
                    nrx -= dx
                    nry -= dy
                else:
                    nbx -= dx
                    nby -= dy
                    
            state = (nrx, nry, nbx, nby)
            if state not in visited:
                visited.add(state)
                q.append((nrx, nry, nbx, nby, depth + 1))
    
    return -1
                    
            
print(solve())    