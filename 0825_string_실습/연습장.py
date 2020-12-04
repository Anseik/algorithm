arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = arr[-1:-4:-1]

print(a)


def solution(participant, completion):
    for _ in range(len(participant)):
        person = participant.pop
        if person in completion:
            completion.remove(person)
        else:
            answer = person

    return answer