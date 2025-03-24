#막대기
import sys
n=int(input())
stack=[]
l=[]
for i in range(n):
    tmp=int(input())
    stack.append(tmp)
for i in reversed(stack):
    if len(l)==0:
        l.append(i)
    else:
        if l[-1]<i:
            l.append(i)
    
print(len(l))