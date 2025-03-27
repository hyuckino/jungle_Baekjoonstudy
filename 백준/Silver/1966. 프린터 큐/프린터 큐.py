from collections import deque
num = int(input())

for _ in range(num):
    a,b = map(int,input().split())
    que = list(map(int, input().split()))
    ind = list(i for i in range(len(que)))
    cnt = 0
    while b in ind:
        while max(que) != que[0]:
            que.append(que.pop(0))
            ind.append(ind.pop(0))
        que.pop(0)
        ind.pop(0)
        cnt += 1
    print(cnt)