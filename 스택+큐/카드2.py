from collections import deque
n = int(input())
lst = [i+1 for i in range(n)]
dq = deque(lst)

while len(dq) > 1:
    fst = dq.popleft()
    snd = dq.popleft()
    dq.append(snd)

print(dq.pop())
