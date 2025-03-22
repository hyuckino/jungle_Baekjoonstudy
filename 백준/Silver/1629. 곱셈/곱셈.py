import sys

A, B, C = map(int, sys.stdin.readline().split())

# 메모이제이션을 위한 딕셔너리
dp = {}

def recur_multi(A, B):
    if B == 0:
        return 1
    if B in dp:  # 이미 계산된 값이면 반환
        return dp[B]
    
    half = recur_multi(A, B // 2) % C
    if B % 2 == 0:
        dp[B] = (half * half) % C
    else:
        dp[B] = (half * half * A) % C
    
    return dp[B]

print(recur_multi(A, B))