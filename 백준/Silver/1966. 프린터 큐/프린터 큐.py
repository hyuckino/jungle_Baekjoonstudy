input = __import__('sys').stdin.readline
num=int(input())
for _ in range(num):
    length,target=map(int,input().split())
    li=list(map(int,input().split()))
    indexed_li = list(enumerate(li))
    cnt=0
    result=(-1,-1)
    while result[0] != target:
        while max(indexed_li, key=lambda x: x[1]) != indexed_li[0]:
            tmp=indexed_li.pop(0)
            indexed_li.append(tmp)
        result=indexed_li.pop(0)
        cnt+=1
    print(cnt)
