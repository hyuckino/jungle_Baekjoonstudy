def generate_permutations(arr, selected, depth, result):
    if depth == n:  # 6개를 선택하면 종료
        result.append(selected[:])  # 깊은 복사해서 저장
        return

    for i in range(len(arr)):
        new_arr = arr[:i] + arr[i+1:]  # 현재 원소 제거한 새로운 리스트
        selected.append(arr[i])  # 선택한 원소 추가
        generate_permutations(new_arr, selected, depth + 1, result)  # 재귀 호출
        selected.pop()  # 백트래킹 (이전 상태로 복귀)

n = int(input())
array = list(map(int, input().split()))
m = []

generate_permutations(array, [], 0, m)
final=[]
for per in m:                   
    result=0
    for i in range(len(per)-1):
        result+=abs(per[i]-per[i+1])
    final.append(result)
print(max(final))