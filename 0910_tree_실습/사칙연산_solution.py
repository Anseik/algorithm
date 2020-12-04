import sys
sys.stdin = open('사칙연산.txt')


T = 10
for tc in range(1, T + 1):
    N = int(input())
    T = [0] + [input().split() for _ in range(N)] # 루트가 1번이므로 앞에 [0]추가
    # print(T)

    for i in range(1, N + 1):
        if len(T[i]) == 4:          # 연산자
            T[i][2] = int(T[i][2])
            T[i][3] = int(T[i][3])
        else:                       # 피연산자
            T[i][1] = int(T[i][1])
    # print(T)

    def calc(v):
        if len(T[v]) == 2:  # 피연산자 = 단말노드
            return T[v][1]
        else:               # 연산자
            l = calc(T[v][2])
            r = calc(T[v][3])

            if T[v][1] == '+': return l + r
            elif T[v][1] == '-': return l - r
            elif T[v][1] == '*': return l * r
            elif T[v][1] == '/': return l / r

    print(int(calc(1)))

