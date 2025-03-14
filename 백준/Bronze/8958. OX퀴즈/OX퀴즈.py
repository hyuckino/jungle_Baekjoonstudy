k=int(input())
for i in range(k):
    n=0
    str1=input()
    u=1
    for i in range(len(str1)):
        if str1[i]=='O':
            if i==0:
                n+=1
            elif str1[i-1]=='O':
                u+=1
                n+=u
            else:
                n+=1
                u=1
    print(n)