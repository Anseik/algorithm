# DFS
# 후행작업 먼저 stack에 넣고 후행작업이 없으면 자기 자신을 stack에 넣는다.

import sys
sys.stdin = open('작업순서.txt')

def dfs(v):
    visited[v] = 1
    for i in range(1, V + 1):
        if adj[v][i] == 1 and not visited[i]:
            dfs(i)
    # for문이 끝나면 후행작업을 모두 마친 상태
    stack.append(v)


T = 10
for tc in range(1,T + 1):
    V, E = map(int, input().split())
    edges = list(map(int, input().split()))

    # 인접행렬(후행 작업 노드)
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    prev_arr = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        f, t = edges[2 * i], edges[2 * i + 1]
        adj[f][t] = 1
        prev_arr[t][f] = 1

    stack = list() # 후행 작업을 먼저 push할 stack
    visited = [0] * (V + 1) # 노드 방문여부 체크

    # 선행작업이 없는 위치에서 깊이 우선탐색 실행
    for i in range(1, V + 1):
        if prev_arr[i].count(1) == 0: # 선행작업 없음
            dfs(i)

    print("#{}".format(tc), *stack[::-1])