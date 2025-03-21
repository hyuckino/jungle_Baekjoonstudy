N, M = map(int, input().split())
trees = list(map(int, input().split()))


def solve(left, right):
    best = 0
    while left <= right:
        
        mid = (right + left)//2
    
        remains = sum(tree-mid for tree in trees if tree > mid)
    
        if remains < M:
            right = mid-1
        else :
            best = mid
            left = mid+1
            
    return best


print(solve(0, max(trees)))