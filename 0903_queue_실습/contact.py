import sys
sys.stdin = open('contact.txt')

def bfs(v):
    Q = []
    Q.append(v)
    visited[v] = 1
    latest_contact = 0 # 가장 나중에 연락을 받는 경우
    latest_person = 0 # 가장 나중에 연락을 받는 사람 중 번호가 가장 큰 사람
    while Q:
        cv = Q.pop(0)
        for w in adj[cv]:
            if not visited[w]:
                Q.append(w)
                visited[w] = visited[cv] + 1

                if visited[w] > latest_contact: # 더 늦게 연락을 받은 경우
                    latest_contact = visited[w]
                    latest_person = w
                elif visited[w] == latest_contact: # 같이 연락을 받은 경우 번호가 큰 사람
                    if w > latest_person:
                        latest_person = w

    return latest_person

T = 10
V = 100
for tc in range(1, T+1):
    # N: 입력받는 데이터의 길이 / S: 시작점
    N, S = map(int, input().split())
    # 비상연락망
    contact_net = list(map(int, input().split()))
    # print(N, S)
    # print(contact_net)

    # 인접리스트(유향 그래프)
    adj = [[] for _ in range(V+1)]
    for i in range(N // 2):
        f, t = contact_net[2 * i], contact_net[2 * i + 1]
        adj[f].append(t)
    # print(adj)

    # 방문표시 및 거리
    visited = [0] * (V + 1)

    # 함수실행
    result = bfs(S)

    # 출력
    print("#{} {}".format(tc, result))