'''
6 11
0 1 3
0 2 5
1 2 2
1 3 6
2 1 1
2 3 4
2 4 6
3 4 2
3 5 3
4 0 3
4 5 6
'''

# start : 시작정점 / adj : 그래프 / weight : 시작정점으로부터 각 노드까지의 최소 비용을 저장할 배열
def dijkstra(start, adj, weight):
    U = {start} # 정점을 방문할때마다 정점을 추가

    # 모든 정점을 방문할 때까지 반복
    while len(U) < V: # U에 모든 정점이 추가되면 while문 종료
        # 1. 현재 방문하지 않은 정점 중, 최소 비용으로 방문할 수 있는 정점 방문
        min_w = INF
        min_idx = -1
        for i in range(V):
            if i not in U and weight[i] < min_w:
                min_w = weight[i]
                min_idx = i
        U.add(min_idx)

        # 2. 그 정점으로부터 갈 수 있는 방문하지 않은 모든 정점의 비용을 확인해서 최소 비용으로 갱신
        for j in range(V):
            if j not in U:
                tmp = min_w + adj[min_idx][j]  # 좀 전에 방문한 정점을 통하여 j노드로 가는 비용
                # tmp가 기존에 j로 가는 비용보다 작으면 갱신
                if weight[j] > tmp:
                    weight[j] = tmp

    return weight # 시작점으로부터 각 정점까지 최소비용이 저장된 배열 반환


V, E = map(int, input().split())
INF = float('inf')
adj = [[INF] * V for _ in range(V)]
for i in range(E):
    s, e, w = map(int, input().split())
    adj[s][e] = w

# 시작지점(start)으로부터 각 노드로 가는데 필요한 최소 비용을 저장하는 배열
start = 0
weight = adj[start][:] # 초기 가중치는 인접행렬에서 시작지점 행과 같다.
result = dijkstra(start, adj, weight)
print(result)
