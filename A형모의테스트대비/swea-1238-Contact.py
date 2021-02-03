import sys
sys.stdin = open('swea-1238-Contact.txt')

def bfs(v):
    Q = list()
    # 노드번호, 거리
    Q.append((v, 0))
    visit[v] = 1
    max_dist = 0
    result = 0
    while Q:
        cv, dist = Q.pop(0)
        for w in adj[cv]:
            if not visit[w]:
                Q.append((w, dist + 1))
                visit[w] = 1
                # 더 늦게 연락을 받았으면 번호에 관계 없이 갱신
                if max_dist < (dist + 1):
                    max_dist = dist + 1
                    result = w
                # 같이 연락을 받았을때는 번호가 크면 갱신
                elif max_dist == (dist + 1):
                    if result < w:
                        result = w

    return result

T = 10
N = 100
for tc in range(1, T + 1):
    # L : 입력받는 데이터 길이, S : 시작점
    L, S = map(int, input().split())
    # print(N, S)

    # 인접 리스트 생성
    adj = [[] for _ in range(N + 1)]
    edge = list(map(int, input().split()))
    for i in range(L // 2):
        s, e = edge[2 * i], edge[2 * i + 1]
        adj[s].append(e)
    # print(adj)

    # 방문체크
    visit = [0] * (N + 1)

    # 당번부터 시작해 bfs 실행
    result = bfs(S)

    # 결과출력
    print('#{} {}'.format(tc, result))
