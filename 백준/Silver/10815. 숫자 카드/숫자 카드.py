input = __import__('sys').stdin.readline
def check(num,k):
    return num>=k
N=int(input())
arr=list(map(int,input().split()))
arr.sort()

result=[] 
M=int(input())
M_arr=list(map(int,input().split()))
for i in range(M):
    lo=0 #가장 왼쪽 인덱스
    hi=N-1 #가장 마지막
    k=M_arr[i] #찾는 수

    #가장 왼쪽만 따로
    if k==arr[0]:
        result.append(True)
        continue
    if k<arr[0]:
        result.append(False)
        continue
         
    while lo+1<hi:
        mid=(lo+hi)//2
        if check(arr[mid],k):
            hi=mid
        else:
            lo=mid
    result.append(arr[hi]==k)

int_list = [1 if x else 0 for x in result]

# 공백으로 구분된 문자열로 출력
print(" ".join(map(str, int_list)))