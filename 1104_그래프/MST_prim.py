# 그래프 입력받기
'''
7 11
0 5 60
0 1 32
0 2 31
0 6 51
1 2 21
2 6 25
2 4 46
3 5 18
3 4 34
4 6 51
4 5 40
'''


# 최소 신장트리의 가중치의 합 구하기
def prim(adj, start):
    # 정점을 mst에 연결하기 위한 최소 가중치
    # 처음에는 어떤것도 연결되어 있지 않기때문에 적절히 큰 값으로 초기화한다.
    INF = 0xfffffff
    weight = [INF] * V

    # 각 정점이 mst에 포함되었는지 표시하는 배열
    # 각 정점이 mst에 포함되지 않았으면 0, 포함되었으면 1
    mst = [0] * V

    weight[start] = 0

    # 가중치의 합을 구하기 위한 변수
    result = 0

    # mst에 모든 정점이 선택될 때까지 반복
    # 정점의 개수만큼 반복문을 돌면서 정점을 선택
    for _ in range(V):
        min_w = INF
        min_v = 0
        # 현재 갈 수 있는 경로 중 가장 가중치가 작은 경로를 선택
        for i in range(V):
            # 정점이 mst에 포함되지 않으면서, 가중치가 가장 작아야 함
            if mst[i] == 0 and weight[i] < min_w:
                min_w = weight[i]
                min_v = i

        mst[min_v] = 1
        result += min_w # 선택되었으니 가중치 더하기

        # 새로 선택한 정점으로부터 갈 수 있는 경로를 살펴보고
        # 노드를 선택하기 위한 정점의 가중치가 작아지면 갱신
        for j in range(V):
            if adj[min_v][j] > 0 and not mst[j] and adj[min_v][j] < weight[j]:
                weight[j] = adj[min_v][j]
                st[j] = min_v

    return result


V, E = map(int, input().split())
adj = [[0] * V for _ in range(V)]
for i in range(E):
    s, e, w = map(int, input().split())
    adj[s][e] = w
    adj[e][s] = w

st = [0] * V # 출발 정점
result = prim(adj, 0)
print(result)
print(st)