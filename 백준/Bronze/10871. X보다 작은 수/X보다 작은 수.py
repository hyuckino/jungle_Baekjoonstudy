a,b=map(int,input().split())
s=list(map(int,input().split()))
for i in range(a):
    if int(s[i])<b:
        print(s[i],end=' ')