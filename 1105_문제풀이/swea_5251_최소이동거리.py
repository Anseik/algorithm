import sys
sys.stdin = open('swea_5251_최소이동거리.txt')


def dijkstra(s):
    U = {s}

    while len(U) < (N + 1):
        # 확정되지 않은 것중에 가중치가 최소인 노드를 찾고
        min_w = INF
        min_idx = 0
        for i in range(N + 1):
            if i not in U and min_w > weight[i]:
                min_w = weight[i]
                min_idx = i
        U.add(min_idx)

        # 그 노드를 확정했을때 인접 노드의 가중치를 갱신한다.
        for j in range(N + 1):
            if j not in U and G[min_idx][j] != INF:
                tmp = min_w + G[min_idx][j]
                if weight[j] > tmp:
                    weight[j] = tmp


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    INF = 0xfffffff
    G = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in range(E):
        s, e, w = map(int, input().split())
        G[s][e] = w

    # print(G)
    weight = G[0][:] # 가중치 초기화
    dijkstra(0)
    result = weight[N]
    print('#{} {}'.format(tc, result))
