T=int(input())
for i in range(T):
  a,b=map(str,input().split())
  a=int(a)
  k=len(b)
  c=''
  for i in range(k):
    c=c+b[i]*a
  print(c)
    