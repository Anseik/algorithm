'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

# 정점, 간선
N, E = map(int, input().split())
# 간선들
temp = list(map(int, input().split()))
# 인접행렬
G = [[0] * (N + 1) for _ in range(N + 1)]
visited = [0] * (N + 1)
# 간선들을 인접행렬에 저장
for i in range(E):
    s, e = temp[2 * i], temp[2 * i + 1]
    G[s][e] = 1
    G[e][s] = 1

# stack을 이용한 dfs
def dfs(v):
    result = list()
    stack = list()
    stack.append(v)
    result.append(v)
    while stack:
        current = stack[-1] # 가장 마지막에 있는 요소
        visited[current] = 1
        # 현재 노드에서 갈 수 있는 모든 노드 검사
        for i in range(1, N+1):
            if G[current][i] == 1 and visited[i] == 0:
                stack.append(i) # 다음방문추가
                result.append(i) # 경로추가
                break
        else: # break에 걸리지 않음 : 현재노드에서 갈 수 있는 노드가 없음
            stack.pop()

    print(result)

dfs(1)


