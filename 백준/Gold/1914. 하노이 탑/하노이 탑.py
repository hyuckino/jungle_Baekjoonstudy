#목표지점 (n)
def f(n):
    if n==1:
        return 1
    else:
        return(2*f(n-1)+1)
N=int(input())
if N>20:
    print(f(N))
else:
    print(f(N))
    def f(a,b,n):
        if n==1:
            print(a,b)
        else:
            f(a,6-a-b,n-1),f(a,b,1),f(6-a-b,b,n-1)
    f(1,3,N)