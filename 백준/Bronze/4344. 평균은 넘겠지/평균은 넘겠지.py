c=int(input())
for i in range(c):
    l=list(map(int,input().split()))
    m=sum(l[1:])/l[0]
    k=0
    for i in l[1:]:
        if i>m:
            k=k+1
    print(f"{k / l[0]*100:.3f}%")
    
    