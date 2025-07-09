input = __import__('sys').stdin.readline
arr = input().strip()
bomb = input().strip()
bomb_len = len(bomb)

result=[]
for ch in arr:
    result.append(ch)
    if len(result)>=bomb_len and result[-bomb_len:]==list(bomb):
        del result[-bomb_len:]
if result:
    print(''.join(result))
else:
    print('FRULA')