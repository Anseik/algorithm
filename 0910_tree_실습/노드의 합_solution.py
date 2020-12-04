import sys
sys.stdin = open('노드의 합.txt')

T = int(input())
for tc in range(1, T + 1):
    # N : 노드의개수, M : 리프의 개수, L: 값을 출력할 노드 번호
    N, M, L = map(int, input().split())
    T = [0] * (N + 1)
    for _ in range(M):
        num, val = map(int, input().split())
        T[num] = val

    # 재귀를 이용한 방법
    def dfs(v):
        if v > N: return 0
        l = dfs(v * 2)
        r = dfs(v * 2 + 1)
        T[v] += l + r

        return T[v]

    dfs(1)
    print(T[L])

    # 반복문으로 배열을 채우는 방법
    # for i in range(N - M, 0, -1): # 배열의 인덱스이자, 노드 번호
    #     T[i] = T[i * 2]
    #     if i * 2 + 1 <= N:
    #         T[i] += T[i * 2 + 1]
    #
    # print(T[L])

