def solution(s):
    answer = 0
    # 가장 긴 펠린드롬 찾기
    for i in range(len(s)):
        for j in range(i, len(s)):
            tmp = s[i:j+1]
            if tmp == tmp[::-1]:
                answer = max(answer, len(tmp))

    return answer


s = 'abacde	'
print(solution(s))