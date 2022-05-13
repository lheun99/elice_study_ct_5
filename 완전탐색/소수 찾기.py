# 중복 없는 순열
from itertools import permutations as pm
#import math


def solution(numbers):
    # 숫자 목록 만들기
    # 순열로 가능한 숫자 만듦 [('1',), ('7',), ('1', '7'), ('7', '1')]
    tuple_list = []
    for length in range(1, len(numbers)+1):
        tuple_list += list(pm(numbers, length))

    # 순열 내용 하나의 내용으로 합쳐서 리스트로 ['1', '7', '17', '71']
    number_list = []
    for number in tuple_list:
        num = int("".join(number))
        if(num != 1 and num != 0):
            number_list.append(num)

    # 소수인지 확인
    answer = number_list.copy()
    for number in number_list:
        for num in range(2, number):
            if number % num == 0:
                answer.remove(number)
                break

    # 또 다른 소수 체크 방법 >> range(2, int(math.sqrt(number)) + 1)
    # 약수의 성질 : https://freedeveloper.tistory.com/391
    # for number in number_list:
    #     for num in range(2, int(math.sqrt(number)) + 1):
    #         if number % num == 0:
    #             answer.remove(number)
    #             break

    # (0이 존재하는 경우 중복 발생) 중복 제거

    answer = set(answer)
    return len(answer)


print(solution("101"))
