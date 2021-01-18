from itertools import combinations

a = [0,3,3,0,7,2,0,2,2,0]

def solution(a):
    if len(a) == 1:
        return 0

    answer = 0
    for i in range(len(a), 0, -2):
        for sub in combinations(a, i):
            # print(sub)

            for j in range(0, len(sub) - 2, 2):
                set1 = set([sub[j], sub[j + 1]])
                set2 = set([sub[j + 2], sub[j + 3]])
                if set1 & set2:
                    continue
                else:
                    break
            else:
                answer = len(sub)
                return answer


# 결과 출력
answer = solution(a)
print(answer)