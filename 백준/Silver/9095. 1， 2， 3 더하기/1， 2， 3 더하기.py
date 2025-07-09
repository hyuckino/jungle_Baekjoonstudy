k=int(input())
for i in range(k):
    n=int(input())
    def count(n):
        if n==1:
            return 1
        if n==2:
            return 2
        if n==3:
            return 4
        else:
            return count(n-1)+count(n-2)+count(n-3)
    print(count(n))