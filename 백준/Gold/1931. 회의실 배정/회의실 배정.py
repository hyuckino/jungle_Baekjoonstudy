N=int(input())
intervals=[]
for _ in range(N):
    a,b=map(int,input().split())
    intervals.append((a,b))
intervals.sort(key=lambda x: (x[1], x[0]))
last_end = -1
count = 0
for s, e in intervals:
    if s >= last_end:
        count += 1
        last_end = e
print(count)