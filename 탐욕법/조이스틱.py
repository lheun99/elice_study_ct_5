def solution(name):
    result = 0
    shift = len(name) - 1

    for idx, a in enumerate(name):
        #up, down
        up = ord(a) - ord('A')
        down = 26 - up
        result += min(up, down)

        #left (left_right), right (right_left)
        # A : -> , <- 비교
        if a == 'A':
            a_idx = idx
            while a_idx < len(name) and name[a_idx] == 'A':
                a_idx += 1

            if idx == 0:
                left_right = 0
            else:
                left_right = idx - 1

            right_left = len(name) - a_idx
            shift = min(shift, left_right + right_left +
                        min(left_right, right_left))

    result += shift
    return result


print(solution("BABABABABBA"))
print(solution("JAN"))
print(solution("AAA"))
print(solution("BBBB"))
