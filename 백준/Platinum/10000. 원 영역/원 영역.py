import sys

class StackItem:
    def __init__(self, pos, state):
        self.pos = pos
        self.state = state

N = int(sys.stdin.readline().strip())
vec = []

for _ in range(N):
    x, r = map(int, sys.stdin.readline().split())
    vec.append((x - r, -1))
    vec.append((x + r, 1))

vec.sort(key=lambda p: (p[0], -p[1]))

st = []
ans = 0
last = 0

for i in range(len(vec)):
    if not st:
        st.append(StackItem(vec[i][0], 0))
        last = vec[i][0]
    elif vec[i][1] == -1:
        if vec[i][0] == last:
            tmp = st.pop()
            if tmp.state != -1:
                tmp.state = 1
            st.append(tmp)
            st.append(StackItem(vec[i][0], 0))
        else:
            tmp = st.pop()
            tmp.state = -1
            st.append(tmp)
            st.append(StackItem(vec[i][0], 0))
            last = vec[i][0]
    elif vec[i][1] == 1:
        tmp = st.pop()
        if tmp.state == 1 and last == vec[i][0]:
            ans += 2
        else:
            ans += 1
        last = vec[i][0]

print(ans + 1)