import sys
sys.stdin = open('장훈이의 높은 선반.txt')

# 부분집합
def powerset(i):
    global a_tall

    if i == N:
        case_tall = 0
        for k in range(N):
            if s[k] == 1:
                case_tall += H[k]
        if B <= case_tall < a_tall:
            a_tall = case_tall

        return

    s[i] = 1
    powerset(i + 1)
    s[i] = 0
    powerset(i + 1)

T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))

    # 가능한 부분집합을 모두구해 점원의 키의 합과 B를 비교하여 B이상인 것중 가장 작은 것을 구한다.
    a_tall = 10000 * N
    s = [0] * N
    powerset(0)

    answer = a_tall - B

    print("#{} {}".format(tc, answer))