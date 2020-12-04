import sys
sys.stdin = open('swea_5249_최소신장트리_solution.txt')


def MST_prim():
    key = [987654321] * (V + 1)
    visited = [False] * (V + 1)

    key[0] = 0

    for _ in range(V):
        min_idx = -1
        min_value = 987654321

        # 최소값을 가진 인덱스를 찾는다.
        for i in range(V + 1):
            if not visited[i] and key[i] < min_value:
                min_idx = i
                min_value = key[i]

        visited[min_idx] = True

        # 갱신이 가능하다면 갱신한다.
        for i in range(V + 1):
            if not visited[i] and key[i] > adj[min_idx][i]:
                key[i] = adj[min_idx][i]

    return sum(key)


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[987654321] * (V + 1) for _ in range(V + 1)]

    for i in range(E):
        A, B, W = map(int, input().split())
        adj[A][B] = adj[B][A] = W

    ans = MST_prim()

    print('#{} {}'.format(tc, ans))


