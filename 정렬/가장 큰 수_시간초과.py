# 시간 초과
from itertools import permutations as pm


def solution(numbers):
    # join사용을 위해 str형태로 바꿔준다 + 정답도 str 형태
    numbers = list(map(str, numbers))
    # 가능한 정수 목록
    number_list = []
    for length in range(1, len(numbers)+1):
        number_list += map("".join, pm(numbers, length))

    # 내림차순 정렬
    number_list.sort(reverse=True)
    # 맨 앞에 큰 수
    answer = number_list[0]

    return answer


print(solution([3, 30, 34, 5, 9]))
