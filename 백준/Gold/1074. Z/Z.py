n,r,c=map(int,input().split())
def f(n,r,c):
    if n==1:
        if r==0:
            if c==0:
                return 0
            else:
                return 1
        else:
            if c==0:
                return 2
            else:
                return 3
    else:
        if r<2**(n-1) and c>=2**(n-1):
            c=c-2**(n-1)
            return f(n-1,r,c)+4**(n-1)
        elif r>=2**(n-1) and c<2**(n-1):
            r=r-2**(n-1)
            return f(n-1,r,c)+2*4**(n-1)
        elif r>=2**(n-1) and c>=2**(n-1):
            r=r-2**(n-1)
            c=c-2**(n-1)
            return f(n-1,r,c)+3*4**(n-1)
        else:
            return f(n-1,r,c)
k=f(n,r,c)
print(k)