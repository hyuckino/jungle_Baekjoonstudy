n, m = map(int, input().split())
li = [int(input()) for _ in range(m)]
li.sort()

# 사용할 후보 리스트 결정
if n < m:
    li = li[-n:]

max_value = 0
result = 0
k = len(li)

for index in range(k):
    tmp = (k - index) * li[index]
    if tmp > max_value:
        max_value = tmp
        result = li[index]

print(result, max_value)