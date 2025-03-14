n=int(input())
def pn_check(n):
    if n==1:
        return 0
    if n==2:
        return 1
    if n%2==0:
        return 0
    if n==3:
        return 1
    if n%3==0:
        return 0
    for i in range(5,n):
        if n%i==0:
            return 0
    else:
        return 1
l=list(map(int,input().split()))
a=0
for i in l:
    a=a+pn_check(i)
print(a)
    
    