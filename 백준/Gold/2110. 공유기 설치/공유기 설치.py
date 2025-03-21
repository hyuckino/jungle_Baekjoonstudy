N, C = map(int, input().split())  # N: 집의 개수, C: 공유기 개수
l = [int(input()) for _ in range(N)]  # 집들의 좌표 리스트
l.sort()  # 집들의 좌표를 정렬

def solv(left, right):
    dist = 0
    while left <= right:
        mid = (left + right) // 2  # mid는 공유기 간 최소 거리
        count = 1  # 첫 번째 집에 공유기 설치
        last_position = l[0]  # 첫 번째 집에 설치했으므로 마지막 위치는 첫 번째 집
        
        # 공유기를 설치할 수 있는지 확인하는 그리디 방식
        for i in range(1, N):
            if l[i] - last_position >= mid:
                count += 1  # 공유기 설치
                last_position = l[i]  # 마지막 설치된 집의 위치를 업데이트
            if count >= C:  # C개 이상의 공유기를 설치하면 종료
                break
        
        if count >= C:  # C개 이상의 공유기를 설치할 수 있으면 거리 늘려보기
            dist = mid
            left = mid + 1
        else:  # C개 이상의 공유기를 설치할 수 없으면 거리를 줄여야 함
            right = mid - 1
            
    return dist

# 이분 탐색 범위: 1 ~ (마지막 집 좌표 - 첫 번째 집 좌표)
print(solv(1, l[-1] - l[0]))
