def all_subsets(lst):
    """
    주어진 리스트 lst의 모든 부분집합을 반환하는 함수 (라이브러리 없이 구현)
    """
    def backtrack(index, subset):
        if index == len(lst):
            result.append(subset[:])
            return
        
        # 원소를 포함하지 않는 경우
        backtrack(index + 1, subset)
        
        # 원소를 포함하는 경우
        subset.append(lst[index])
        backtrack(index + 1, subset)
        subset.pop()
    
    result = []
    backtrack(0, [])
    return result

n,k=map(int,input().split())
test_list = list(map(int,input().split()))
result = all_subsets(test_list)
count=0
if k==0:
    for i in range(len(result)):
        if sum(result[i])==k:
            count+=1
    print(count-1)
else:
    for i in range(len(result)):
        if sum(result[i])==k:
            count+=1
    print(count)