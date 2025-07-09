import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    tmp=[]
    n=int(input())
    for _ in range(n):
        a,b=map(int,input().split())
        tmp.append((a,b))
    tmp.sort()
    max=tmp[0][1]
    count=1
    for ele in tmp[1:]:
        if ele[1]<max:
            max=ele[1]
            count+=1
    print(count)