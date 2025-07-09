from bisect import bisect_left
n=int(input())
arr=list(map(int,input().split()))
index=[1]
x=[arr[0]]

for i in range(1,len(arr)):
    if arr[i]> x[-1]:
        x.append(arr[i])
        index.append(index[-1]+1)
    else:# 더 작을 경우 들어갈 위치 이분 탐색으로 찾기
        idx = bisect_left(x, arr[i]) # 현재 값이 x 배열의 몇 번째 인덱스에 들어갈 수 있는지를 찾아서
        x[idx] = arr[i]   
        
print(index[-1])     