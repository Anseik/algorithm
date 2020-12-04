import sys
sys.stdin = open('pro_괄호 변환.txt')

def correct(p):
    # 괄호검사
    stack = []
    for i in range(len(p)):
        if p[i] == "(":
            stack.append(p[i])
        elif p[i] == ")":
            if len(stack) == 0:
                return False
            else:
                tmp = stack.pop()
                if not tmp == "(" and p[i] == ")":
                    return False

    if len(stack) != 0:
        return False
    return True


def slice(p):
    # u, v분리
    if len(p) == 0:
        return ""
    bracket = {
        "(": 0,
        ")": 0
    }
    for i in range(len(p)):
        if p[i] == "(":
            bracket["("] += 1
        elif p[i] == ")":
            bracket[")"] += 1

        if bracket["("] == bracket[")"]:
            u, v = p[:i + 1], p[i + 1:]
            break

    return u, v


def solution(p):
    answer = ''

    if correct(p): # 올바른 괄호 문자열이면
        answer += p
        return answer

    u, v = slice(p)

    if correct(u):
        answer += u
        answer += solution(v)

    else:
        answer += "("
        answer += solution(v)
        answer += ")"
        tmp = ""
        for i in range(len(u[1:-1])):
            if u[1:-1][i] == "(":
                tmp += ")"
            elif u[1:-1][i] == ")":
                tmp += "("
        answer += tmp

    return answer


T = 3
for tc in range(1, T+1):
    p = input()
    result = solution(p)
    print(result)
