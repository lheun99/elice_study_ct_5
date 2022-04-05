def solution(participants, completion):
    participants.sort()
    completion.sort()
    print(participants, completion)
    for a, b in zip(participants, completion):
        print(a, b)
        if a != b:
            return a
    return participants[-1]


print(">",
      solution(["marina", "josipa", "nikola", "vinko", "filipa"],
               ["josipa", "filipa", "marina", "nikola"]))
print(">",
      solution(["marina", "josipa", "nikola", "vinko", "maha"],
               ["josipa", "vinko", "marina", "nikola"]))
