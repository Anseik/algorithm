import sys
sys.stdin = open('boj_4195_친구네트워크.txt')


T = int(input())
for tc in range(1, T + 1):
    F = int(input())
    G = {}
    for i in range(F):
        p1, p2 = input().split()
        # print(p1, p2)
        if p1 in G:
            G[p1][0].append(p2)
            G[p1][1] += 1
        else:
            G[p1] = [[p2], 2]
        if p2 in G:
            G[p2][0].append(p1)
            G[p2][1] += 1
        else:
            G[p2] = [[p1], 2]
        # print(G)

        # 새로 친구관계를 맺은 두 사람이 둘다 내 친구이면 나의 친구네트워크는 증가하지 않는다.
        # 새로 친구관계를 맺은 두 사람이 둘다 내 친구가 아니면 나의 친구네트워크는 증가하지 않는다.
        # 새로 친구관계를 맺은 두 사람 중 한 명만 내 친구여야 나의 친구네트워크가 1증가한다.
        # print(G)
        for n1 in G[p1][0]:
            if n1 != p2:
                if p2 not in G[n1][0]:
                    G[n1][1] += 1
                    G[p2][1] += 1

        for n2 in G[p2][0]:
            if n2 != p1:
                if p1 not in G[n2][0]:
                    G[n2][1] += 1
                    G[p1][1] += 1

        ans = G[p1][1]
        print(ans)


