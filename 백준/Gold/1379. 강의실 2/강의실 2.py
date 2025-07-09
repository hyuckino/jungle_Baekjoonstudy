import sys
import heapq

input = sys.stdin.readline
n = int(input())
arr = []

for _ in range(n):
    a, b, c = map(int, input().split())
    arr.append((b, c, a))  # (시작, 끝, 고유번호)

arr.sort()  # 시작 시간 기준

# 줄 정보: (현재 줄의 끝나는 시간, 줄 번호)
heap = []  # 우선순위 큐
next_line = 1  # 다음 줄 번호
order = dict()  # 고유번호: 줄번호 저장용

for start, end, idx in arr:
    # 가장 빨리 끝나는 줄을 꺼내서 확인
    if heap and heap[0][0] <= start:
        finish_time, line_no = heapq.heappop(heap)
        heapq.heappush(heap, (end, line_no))
        order[idx] = line_no
    else:
        # 새로운 줄을 할당
        heapq.heappush(heap, (end, next_line))
        order[idx] = next_line
        next_line += 1

# 출력
print(len(set(order.values())))
for key in sorted(order):
    print(order[key])

    
    