import sys
sys.stdin = open('swea_5201_컨테이너운반_solution.txt')

T = int(input())
for tc in range(1, T + 1):
    # N : 컨테이너 수 / M : 트럭 수
    N, M = map(int, input().split())
    # 화물 무게
    W = list(map(int, input().split()))
    # 적재용량
    T = list(map(int, input().split()))

    W.sort(reverse=True)
    T.sort(reverse=True)

    i = j = ans = 0
    while i < N and j < M:
        if W[i] <= T[j]:
            ans += W[i]
            i, j = i + 1, j + 1
        else: # i번 화물을 실을 수 없으므로 다음 화물로 넘어간다.
            i += 1

    print('#{} {}'.format(tc, ans))