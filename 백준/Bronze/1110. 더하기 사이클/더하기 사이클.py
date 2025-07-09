N = input()
if len(N) == 1:  # 한 자리 수일 경우 '0'을 붙여 두 자리로 만듦
    N = '0' + N

first = N  # 초기 값 저장
cycle = 0

while True:
    k = str(int(N[0]) + int(N[1]))  # 각 자리 숫자의 합을 문자열로 변환
    N = N[1] + k[-1]  # 새로운 숫자 생성 (두 번째 자리 + 합의 마지막 자리)
    cycle += 1

    if N == first:  # 원래 숫자로 돌아오면 종료
        break

print(cycle)