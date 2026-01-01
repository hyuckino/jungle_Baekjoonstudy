#just수학 백준 13458
#뺄샘일때 음수가 되는 조건을 항상 유의하자 i-B음수 조건
import math
N = int(input())
A = list(map(int,input().split()))
B, C = map(int,input().split())
Temp = []
for i in A:
    if i-B>0:
        calc = math.ceil((i-B)/C)
        Temp.append(calc)
    else:
        Temp.append(0)   #음수 조건 분기처리 
print(N+sum(Temp))
