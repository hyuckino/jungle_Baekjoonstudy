N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]  # 2차원 리스트로 저장

count = 0

# 가로 방향 검사 ('-' 탐색)
for i in range(N):
    j = 0
    while j < M:
        if arr[i][j] == '-':  # 새로운 '-' 그룹 발견
            count += 1
            while j < M and arr[i][j] == '-':  # 같은 그룹의 '-'는 스킵
                j += 1
        else:
            j += 1  # 다음 문자로 이동

# 세로 방향 검사 ('|' 탐색)
for j in range(M):
    i = 0
    while i < N:
        if arr[i][j] == '|':  # 새로운 '|' 그룹 발견
            count += 1
            while i < N and arr[i][j] == '|':  # 같은 그룹의 '|'는 스킵
                i += 1
        else:
            i += 1  # 다음 문자로 이동

print(count)