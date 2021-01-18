def solution(n, m):
    answer = []
    # 최대공약수
    x = n
    y = m
    while y:
        x, y = y, x % y
    answer.append(x)

    # 최소공배수
    answer.append(n * m // x)

    return answer

print(solution(3, 12))