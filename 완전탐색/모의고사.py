def solution(answers):
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    one_len = len(one)
    two_len = len(two)
    three_len = len(three)

    answers_len = len(answers)
    correct = [0, 0, 0]
    for i in range(answers_len):
        if one[i % one_len] == answers[i]:
            correct[0] += 1

        if two[i % two_len] == answers[i]:
            correct[1] += 1

        if three[i % three_len] == answers[i]:
            correct[2] += 1

    answer = []
    for i, person in enumerate(correct):
        best = max(correct)
        if best == person:
            answer.append(i+1)
            # print(answer)

    return answer


print(solution([1, 3, 2, 4, 2]))