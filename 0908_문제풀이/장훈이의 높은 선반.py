import sys
sys.stdin = open('장훈이의 높은 선반.txt')

# 조합문제
def comb(s, i, c, t):
    global t_tall
    if c == t:
        # 해당 경우의수의 키의 합
        case_tall = 0
        for k in range(N):
            if s[k] == 1:
                case_tall += H[k]
        if B <= case_tall < t_tall:
            t_tall = case_tall

        return

    if i == N:
        return

    s[i] = 1
    comb(s, i + 1, c + 1, t)
    s[i] = 0
    comb(s, i + 1, c, t)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    # print(N, B)
    # print(H)

    # N명부터 1명까지 가능한 조합을 모두구해 점원의 키의 합과 B를 비교하여 B이상인 것중 가장 작은 것을 구한다.
    a_tall = 10000 * N
    for t in range(N, 0, -1):
        s = [0] * N

        # t명일때의 최적해
        t_tall = 10000 * N
        comb(s, 0, 0, t)

        # 1 ~ N명의 최적해
        if t_tall < a_tall:
            a_tall = t_tall

    answer = a_tall - B

    print("#{} {}".format(tc, answer))