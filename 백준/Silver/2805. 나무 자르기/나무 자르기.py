N,M=map(int,input().split())
trees=list(map(int,(input().split())))
trees.sort()
lo=0
hi=trees[-1]
def check(mid):
    remains = sum(tree-mid for tree in trees if tree > mid)
    return remains>=M   
while lo+1<hi:
    mid=(lo+hi)//2
    if check(mid):
        lo=mid
    else:
        hi=mid
print(lo)