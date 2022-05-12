# h-index 자체가 이해 안됨,,

# h-index 산출 방법
# 1. 해당 연구자의 발표 논문을 피인용횟수가 많은 순으로 정렬합니다.
#   피인용횟수가 높은 순으로 번호를 부여합니다.
# [3, 0, 6, 1, 5] -> 0:6 1:5 2:3 3:1 4:0

# 2. 논문의 번호(No)와 피인용횟수를 비교하여
#   피인용횟수가 논문의 번호(No)와 같거나
#   citations[idx] = idx
#   큰 번호(No)가
#   citations[idx] < idx
#   연구자의 h-index가 됩니다.

# 전체 논문중 많이 인용된 순으로 정렬한 후,
# 피인용수가 논문수와 같아지거나
# citations[idx] = idx
# 피인용수가 논문수보다 작아지기 시작하는 숫자가
# citations[idx] < idx
# 바로 나의 h가 됩니다.

def solution(citations):
    citations.sort(reverse=True)
    for idx, citation in enumerate(citations):
        # idx번째의 인용 수 h : h번 이상 인용된 논문은 idx편
        # 0 : 6 : 1 (6)
        # 1 : 5 : 2 (5, 6)
        # 2 : 3 : 3 (3, 5, 6)
        # 3 : 1 : 4 (1, 3, 5, 6)
        # 4 : 0 : 5 (0, 1, 3, 5, 6)
        # ? citation : 인용수
        # ? idx : 논문 수
        # ? 피인용수 <= 논문수
        if citation <= idx:
            print(idx)
            return idx

    return len(citations)

# def solution(citations):
#     citations.sort(reverse=True)  # 인용 횟수가 높은 것부터 내림차순 정렬
#     # i번째 원소가 h라면, h번 이상 인용된 논문은 i+1편
#     # enumerate에 start=1을 주어 1부터 인덱스를 세게 하자
#     answer = max(map(min, enumerate(citations, start=1)))

#     return answer


# def solution(citations):
#     citations = sorted(citations) 0 1 3 5 6
#     l = len(citations) 5
#     for i in range(l):
#         if citations[i] >= l-i:
#             return l-i
#     return 0

# h번 이상 인용된 논문이 h편 이상 : h의 최대
# 0 : 0:0 >= 5-0
# 1 : 1:1 >= 5-1
# 2 : 2:3 >= 5-2 -> 3

print(solution([3, 0, 6, 1, 5]))
