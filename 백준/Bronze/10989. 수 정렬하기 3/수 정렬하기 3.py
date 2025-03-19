import sys
N=int(sys.stdin.readline())
l=[0]*10000
for i in range(N):
    l[int(sys.stdin.readline())-1]+=1
for i in range(10000):
    if l[i]!=0:
        for qq in range(l[i]):
            print(i+1)