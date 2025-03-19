n = int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))
m = []
for i in range(n):
    arr[i].append(i)
def find(arr,select,depth,result):
    if depth==n:
        sum=0
        for i in range(len(select)-1):
            if select[i][select[i+1][-1]]!=0:
                sum+=select[i][select[i+1][-1]]
            else:
                return None
        if select[-1][select[0][-1]]!=0:
            sum+=select[-1][select[0][-1]]
        else:
            return None
        result.append(sum)
        return
    for i in range(len(arr)):
        new_arr=arr[:i]+arr[i+1:]
        select.append(arr[i])
        find(new_arr,select,depth+1,result)
        select.pop()

        

find(arr, [], 0, m)
print(min(m))