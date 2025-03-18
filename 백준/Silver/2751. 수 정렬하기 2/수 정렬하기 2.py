import sys
n = int(sys.stdin.readline())
a = [int(sys.stdin.readline().strip()) for i in range(n)] 
a.sort()
for i in a:
    print(i)
   