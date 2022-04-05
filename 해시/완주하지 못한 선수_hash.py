def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
        """
        dic = {
            marina의 해시값 : marina,
            josipa의 해시값 : josipa,
            nikola의 해시값 : nikola,
            vinko의 해시값 : vinko,
            filipa의 해시값 : filipaㄴ,
        }
        temp = (모든 사람의 해시값의 합)
        """

    for com in completion:
        temp -= hash(com)
        """
        temp에서 
        "josipa", "filipa", "marina", "nikola"의 해시값을 빼주면 
        남는 값 = vinko의 해시값
        """
    answer = dic[temp]
    """
    dic에서 vinko의 해시값을 통해 :vinko를 찾는다
    """
    return answer


print(solution(["marina", "josipa", "nikola", "vinko",
      "filipa"], ["josipa", "filipa", "marina", "nikola"]))
