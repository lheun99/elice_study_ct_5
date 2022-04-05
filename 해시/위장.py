import collections


def solution(clothes):
    typeList = []
    for cloth, _type in clothes:
        typeList += [_type]
    count = collections.Counter(typeList)
    print(count)
    answer = 1
    for cnt in count.values():
        answer *= cnt+1

    return answer-1


print(solution([["yellowhat", "headgear"], [
      "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))

# 경우의 수
# cnt + 1 -> 각 타입 안입는 경우 추가
# 마지막 -1 -> 모든 타입에서 안입는 경우 빼주는
