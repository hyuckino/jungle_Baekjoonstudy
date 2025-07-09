n=int(input())
result=n//5
if n==1 or n==3:
    print(-1)
elif n%5==0:
    print(result)
elif n%5==1:
    print(result+2)
elif n%5==2:
    print(result+1)
elif n%5==3:
    print(result+3)
elif n%5==4:
    print(result+2)