def solution(info, query):
    answer = []
    # info를 list로 변환
    for i in range(len(info)):
        info[i] = info[i].split()
    # print(info)

    # query를 list로 변환
    for j in range(len(query)):
        query[j] = query[j].split()
        for i in range(3):
            query[j].remove('and')
    # print(query)

    for m in range(len(query)):
        cnt = 0
        for n in range(len(info)):
            for k in range(5):
                if query[m][k] != '-' and 0 <= k < 4:
                    if info[n][k] != query[m][k]:
                        break
                elif k == 4:
                    if int(info[n][k]) < int(query[m][k]):
                        break
            else:
                cnt += 1

        answer.append(cnt)

    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

result = solution(info, query)
print(result)