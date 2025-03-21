N=int(input())
arr=set(map(int,input().split()))
M=int(input())
arr2=list(map(int,input().split()))
for i in arr2:
    print(1) if i in arr else print(0)  