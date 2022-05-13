def solution(number, k):
    answer = []
    kForAnswer = k
    # 4 1 7 7 2 5 2 8 4 1
    for num in number:
        # answer에 내용이 존재해야 비교 가능 + k만큼만 제거
        # + number중 하나인 num이 answer에 마지막 수보다 크면
        while len(answer) > 0 and k > 0 and num > answer[-1]:
            # print(f"{num} > {answer[-1]}")
            # 마지막 수 제거하고
            answer.pop()  # 1 2 2
            # print(answer)
            # k-1해준다
            k -= 1

        # 계속 비교를 위해 answer에는 num을 계속 추가
        answer.append(num)
        # print(answer)

    answer = "".join(answer)
    # answer.append때문에 길이는 len(number)이므로
    # 제거한 k만큼의 개수를 뺀 수만큼 출력해줘야
    answer = answer[:len(number)-kForAnswer]
    # print(kForAnswer)
    return answer


print(solution("4177252841", 4))
