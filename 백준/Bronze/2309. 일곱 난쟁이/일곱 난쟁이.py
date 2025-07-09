l=[]
for i in range(9):
    k=int(input())
    l.append(k)
found=False
for a1 in l:
    a=l[:]
    a.remove(a1)
    for b1 in a:
        b=a[:]
        b.remove(b1)
        if sum(b)==100:
            b.sort()
            for i in b:
                print(i)
            found=True
            break
        
    if found:
        break