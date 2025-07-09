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
    i=5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return 0
        i += 6
    return 1
itr=int(input())
for i in range(itr):
    n=int(input())
    k=n/2
    while True:
        if pn_check(k)==1 and pn_check(n-k)==1:
            print(int(k),int(n-k))
            break
        k-=1

#다른 버전도 있음