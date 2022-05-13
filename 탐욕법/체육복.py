# 체육복
# n = int(input())  # 5
# lost = list(map(int, input().split()))  # 1 3
# reserve = list(map(int, input().split()))  # 2 3

def solution(n, lost, reserve):
    lost.sort()
    reserve.sort()

    # lost 내용의 변경을 막기 위해 copy한 거 사용
    lostCopy = lost.copy()
    # lost에 존재하면서
    for i in lost:
        # reserve에서도 존재하면
        if i in reserve:
            # 빌려주지 못하지만 + 참석은 할 수 있음
            # lostCopy + reserve에서 제거
            lostCopy.remove(i)
            reserve.remove(i)

    # lostCopy2 : 최종적으로 체육복 빌리지 못한 사람만 남을 것
    # lost+reserve인 사람 제거한 lostCopy을 복사
    lostCopy2 = lostCopy.copy()

    # 체육복 빌려야 하는 사람들 (lostCopy)
    for i in lostCopy:
        # reserve에 앞 번호 존재
        if i-1 in reserve:
            # 체육복 빌렸으므로 lostCopy2에서 제거
            lostCopy2.remove(i)
            # i-1번은 이제 못빌려주므로 reserve에서 제거
            reserve.remove(i-1)
        # reserve에 뒷 번호 존재
        elif i+1 in reserve:
            # 체육복 빌렸으므로 lostCopy2에서 제거
            lostCopy2.remove(i)
            # i+1번은 이제 못빌려주므로 reserve에서 제거
            reserve.remove(i+1)
    # 최종적으로 수업에 참여할 수 있는 학생 수
    # = 전체 학생 수 - 체육복을 못 빌린 학생 수
    answer = n - len(lostCopy2)
    return answer
