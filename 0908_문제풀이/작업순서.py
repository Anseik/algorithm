import sys
sys.stdin = open('작업순서.txt')

def dfs(v):
    global remain
    visit[v] = 1
    remain -= 1
    result.append(v)
    for w in range(1, V + 1):
        if w in G[v] and not visit[w]:
            for j in range(1, V + 1):
                if not visit[j] and w not in G[j]:
                    continue
                elif not visit[j] and w in G[j]:
                    break
            else:
                dfs(w)


T = 10
for tc in range(1, T+1):
    V, E = map(int, input().split())
    rel = list(map(int, input().split()))
    # print(V, E)
    # print(rel)

    # 인접리스트
    G = [[] for _ in range(V + 1)]
    for i in range(0, len(rel), 2):
        s, e = rel[i], rel[i + 1]
        G[s].append(e)
    # print(G)

    # 방문체크
    visit = [0] * (V + 1)

    # 인접리스트에 해당 번호가 없어야 선행작업이 모두 끝난것이다(즉 현재 작업을 할 수 있는 상태이다.)
    # 방문 안한 정점 중에서 나한테 올 수 있는 정점이 있으면 선행작업이 끝나지 않은 것이다.
    result = []
    remain = V
    while remain:
        for v in range(1, V + 1):
            for row in G:
                if v not in row:
                    continue
                else:
                    break
            else:
                if not visit[v]:
                    dfs(v)

    # print(result)
    # print(len(result))

    print("#{}".format(tc), end=" ")
    for num in result:
        print(num, end=" ")
    print()
