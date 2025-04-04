N,K=map(int,input().split())
value=[]
for _ in range(N):
    value.append(int(input()))
value.sort(reverse=True)
result=0
remain=0
for i in value:
    if i<=K:
        result+=K//i
        remain=K%i
        K=remain
    if K==0:
        break
print(result)