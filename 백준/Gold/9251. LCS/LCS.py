val1 = input()
val2 = input()
len1 = len(val1)
len2 = len(val2)
arr = [[0] * (len1 + 1) for _ in range(len2 + 1)]

for y in range(len2):
    for x in range(len1):
        if val1[x] == val2[y]:
            arr[y+1][x+1] = arr[y][x] + 1
        else:
            arr[y+1][x+1] = max(arr[y][x+1], arr[y+1][x])

print(arr[len2][len1])