N = int(input())
li = list(map(int, input().split()))
li.sort()

index1 = 0  # 왼쪽 포인터
index2 = N - 1  # 오른쪽 포인터
min_sum = float('inf')  # 최소 절댓값 저장
best1, best2 = 0, 0  # 최적의 두 값 저장

while index1 < index2:  # 올바른 종료 조건
    sum_val = li[index1] + li[index2]

    # 최소 합 갱신
    if abs(sum_val) < abs(min_sum):
        min_sum = abs(sum_val)
        best1, best2 = li[index1], li[index2]

    # sum이 음수면 index1 증가 (더 큰 값 필요)
    if sum_val < 0:
        index1 += 1
    # sum이 양수면 index2 감소 (더 작은 값 필요)
    else:
        index2 -= 1

print(best1, best2)