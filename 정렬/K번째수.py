# [1, 5, 2, 6, 3, 7, 4][2, 5, 3]
# [5, 2, 6, 3]
# [2, 3, 5, 6] -> 5

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
command = commands[0]


def solution(array, commands):
    answer = []
    for command in commands:
        start = command[0]-1
        end = command[1]
        idx = command[2]-1
        start, end, idx = command
        arr = array[start:end]

        arr.sort()
        answer.append(arr[idx])
    return answer
