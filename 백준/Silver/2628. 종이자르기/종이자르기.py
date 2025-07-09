#종이자르기
#처음에 주어지는 가로 세로 길이 -1 이 점선의 개수
# 가로 길이 a 분할 지점 점선 번호0(2,4)10 사이에 가장 큰 거 8 가장 큰 세로
# 만약 (0,1,3,9,10)이런 튜플형 있으면 간격 가장 큰거 구해주는 함수?
def max_d(l):
    index=0
    distance=[]#간격격
    while True:
        d=l[index+1]-l[index]
        distance.append(d)
        if index==len(l)-2:
            break
        index+=1
    return max(distance)
a,b=map(int,input().split())
n=int(input())
width=[0,b]
height=[0,a]
for i in range(n):
    c,d=map(int,input().split())
    if c==0:
        width.append(d)
    else:
        height.append(d)
width.sort()
height.sort() # sort를 안하면 간격이 (0,10,3,2) 10이 되는경우 발생생
print(max_d(width)*max_d(height))