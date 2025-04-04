from collections import deque
import sys
input=sys.stdin.readline
#입력값
n=int(input())
m=int(input())

indegree=[0]*(n+1) 
dp=[[0]*(n+1) for _ in range(n+1)] # dp 테이블 생성
#그래프 생성
graph=[[] for _ in range(n+1)]
for _ in range(m):
    b,a,s=map(int,input().split())
    graph[a].append((b,s))
    indegree[b]+=1
dq=deque([])
for i in range(1,n+1):
    if indegree[i]==0:
        dq.append(i)
while dq:
    now = dq.popleft()
    for next,next_need in graph[now]:
        if dp[now].count(0) == n+1:
            dp[next][now] += next_need
        else:
            for i in range(1,n+1):
                dp[next][i] += dp[now][i] * next_need
        indegree[next] -= 1
        if indegree[next] == 0:
            dq.append(next)

for x in enumerate(dp[n]):
    if x[1] > 0:
        print(*x)  