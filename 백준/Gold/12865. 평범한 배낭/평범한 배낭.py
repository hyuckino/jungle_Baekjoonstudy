import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, K = map(int, input().split())
arr = [tuple(map(int, input().split())) for _ in range(N)]

# 메모이제이션: (idx, 남은 무게) → 최대 가치
dp = [[-1] * (K + 1) for _ in range(N + 1)]

def knapsack(i, w):
    if i == N:
        return 0
    if dp[i][w] != -1:
        return dp[i][w]
    
    # i번째 아이템을 안 고르는 경우
    result = knapsack(i + 1, w)
    
    # 고를 수 있으면 고르는 경우도 고려
    if w + arr[i][0] <= K:
        result = max(result, knapsack(i + 1, w + arr[i][0]) + arr[i][1])
    
    dp[i][w] = result
    return result

print(knapsack(0, 0))