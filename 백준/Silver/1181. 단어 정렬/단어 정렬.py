n=int(input())
l=[]
for i in range(n):
    l.append(input())
l=set(l)
l=list(l)
l.sort(key=lambda x: (len(x), x.lower()))
for i in l:
    print(i)