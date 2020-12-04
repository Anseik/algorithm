import sys
sys.stdin = open('swea_5249_최소신장트리.txt')


# mst에 포함되지 않고 갈수 있는 노드의 가중치 중 가장 작은 것을 찾아서 선택
# 그 정점이 선택되므로서 인접한 정점을 mst에 연결하는데 필요한 가중치를 최소값으로 갱신한다.
# 모든 정점이 연결될때까지 위 과정을 반복
def prim(start):
    # 초기화
    INF = 0xffffffff
    weight = [INF] * (V + 1)
    weight[start] = 0
    mst = [0] * (V + 1)
    result = 0

    for _ in range(V + 1): # 모든 정점이 선택될때까지 반복
        # mst에 포함되지 않고 갈수 있는 노드의 가중치 중 가장 작은 것을 찾아서 선택
        min_w = INF
        min_idx = 0
        for i in range(V + 1):
            if not mst[i] and weight[i] < min_w:
                min_w = weight[i]
                min_idx = i

        mst[min_idx] = 1
        result += min_w

        # 그 정점이 선택되므로서 인접한 정점을 mst에 연결하는데 필요한 가중치를 최소값으로 갱신한다.
        for j in range(V + 1):
            if not mst[j] and G[min_idx][j] and weight[j] > G[min_idx][j]:
                weight[j] = G[min_idx][j]
                st[j] = min_idx

    return result

T = int(input())
for tc in range(1, T + 1):
    # V : 마지막노드 번호 / E : 간선의 개수
    V, E = map(int, input().split())
    G = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        n1, n2, w = map(int, input().split())
        G[n1][n2] = w
        G[n2][n1] = w
    # print(V, E)
    # print(G)
    st = [0] * (V + 1)
    result = prim(0)
    # print(st)
    print('#{} {}'.format(tc, result))

