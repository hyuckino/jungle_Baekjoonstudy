input = __import__('sys').stdin.readline
from heapq import heappush
from heapq import heappop
min_heap=[]
max_heap=[]
N=int(input())
value1=int(input())
print(value1)
value2=int(input())
if value1>=value2:
    print(value2)
    max_heap.append(-value2)
    min_heap.append(value1)
else:
    print(value1)
    max_heap.append(-value1)
    min_heap.append(value2)

for _ in range(2,N):
    k=int(input())
    if min_heap[0]<k:
        heappush(min_heap, k)
    else:
        heappush(max_heap, -k)
    if len(min_heap)-len(max_heap)==1:
        tmp=heappop(min_heap)
        heappush(max_heap, -tmp)
    if len(max_heap)-len(min_heap)==2:
        tmp=-heappop(max_heap)
        heappush(min_heap, tmp)
    print(-max_heap[0])