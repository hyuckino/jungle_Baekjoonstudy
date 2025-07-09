solve=input()
tmp=solve.split('-')
result=sum(map(int,tmp[0].split('+')))
for i in tmp[1:]:
    result-=sum(map(int,i.split('+')))
print(result)