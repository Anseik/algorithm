import sys
sys.stdin = open('swea_5248_그룹나누기_solution.txt')


def bfs(st):
    queue = [st]
    team[st] = True

    while len(queue) > 0:
        curr = queue.pop(0)

        for w in range(1, V + 1):
            if not team[w] and adj[curr][w]:
                team[w] = True
                queue.append(w)


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    team = [False] * (V + 1)
    edge = list(map(int, input().split()))
    adj = [[0] * (V + 1) for _ in range(V + 1)]

    # for i in range(0, len(edge), 2):
    #     A = edge[i]
    #     B = edge[i + 1]
    #     adj[A][B] = adj[B][A] = 1

    for i in range(E):
        A = edge[2 * i]
        B = edge[2 * i + 1]
        adj[A][B] = adj[B][A] = 1

    ans = 0

    for i in range(1, V + 1):
        if not team[i]:
            ans += 1
            bfs(i)

    print('#{} {}'.format(tc, ans))
