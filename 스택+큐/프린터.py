from collections import deque


def solution(priorities, location):
    dq = deque()
    for idx, priority in enumerate(priorities):
        dq.append((priority, idx))

    cnt = 0
    while dq:
        priority = dq.popleft()
        if dq and priority[0] < max(dq)[0]:
            dq.append(priority)
        else:
            cnt += 1
            if priority[1] == location:
                return cnt


print(solution([2, 1, 3, 2], 2))
