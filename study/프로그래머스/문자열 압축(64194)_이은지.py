def solution(s):
    answer = len(s)


    for alpha in range(1, len(s)):
        c = ""
        p = s[0:alpha]
        cnt = 1


        for j in range(alpha, len(s), alpha):

            if p == s[j:j + alpha]:
                cnt += 1


            else:
                c += str(cnt) + p if cnt >= 2 else p

                p = s[j:j + alpha]
                cnt = 1

        c += str(cnt) + p if cnt >=2 else p
        answer = min(answer, len(c))
    return answer