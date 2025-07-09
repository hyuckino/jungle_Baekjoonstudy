n=int(input())
memo={0:0,1:1}
def pibo(n):
    if n in memo:
        return memo[n]
    memo[n]= pibo(n-1) + pibo(n-2)
    return memo[n]
print(pibo(n))