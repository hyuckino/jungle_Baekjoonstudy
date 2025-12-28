N=int(input())
E=int(input())
D= {i: [] for i in range(1, N + 1)}
for i in range(E):
    li=list(map(int,input().split()))
    if 1 in li[1:]:
        for j in li[1:]:
            D[j].append(i)
    else:
        result = set().union(*(D[k] for k in li[1:]))
        for i in li[1:]:
            D[i] = list(result)

for k,v in D.items():
    if len(v)==len(D[1]):
        print(k)