input = __import__('sys').stdin.readline
M, N, L = map(int,input().split())
hunters = list(map(int, input().split()))
animals = []
hunters.sort()

for _ in range(N):
  a, b = map(int, input().split())
  animals.append((a, b))

def find_hunter(x):
  start = 0
  end = M-1
  result = 0

  while start + 1 < end:
    mid = (start+end) // 2


    if x > hunters[mid] :
      start = mid
    else:
      end = mid
      
  if abs(hunters[start] - x) < abs(hunters[end] - x):
    result = start
  else: result = end
  return result

cnt = 0
for x, y in animals:
  if 0 <= y <= L:
    find_idx = find_hunter(x)

    if L >= y+abs(hunters[find_idx]-x):
      cnt += 1

print(cnt)