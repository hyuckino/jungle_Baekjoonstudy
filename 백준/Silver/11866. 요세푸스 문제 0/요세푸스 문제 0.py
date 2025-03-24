from collections import deque

def find_last_card(N,K):
    result=[]
    queue = deque(range(1, N+1))
    
    while len(queue)>0:
        for i in range(K-1):
            queue.append(queue.popleft())
        result.append(queue.popleft())
    return result


N,K=map(int,input().split())
result=find_last_card(N,K)
print("<" + ", ".join(map(str, result)) + ">")