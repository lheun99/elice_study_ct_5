from functools import cmp_to_key


def numberCompare(x, y):
    num1 = x + y
    num2 = y + x

    if num1 > num2:
        print(1)
        return 1
    elif num1 < num2:
        print(-1)
        return -1
    else:
        print(0)
        return 0


def solution(numbers):
    numbers = list(map(str, numbers))
    n = sorted(numbers, key=cmp_to_key(numberCompare), reverse=True)
    print(n)
    answer = str(int(''.join(n)))
    return answer


print(solution([0, 0, 0]))
