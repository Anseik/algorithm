import sys
sys.stdin = open('subtree.txt')

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split()) # E : 간선수, 정점수 : E + 1
    # 정점 번호 : 1 ~ E + 1
    L = [0] * (E + 2)
    R = [0] * (E + 2)
    P = [0] * (E + 2)

    arr = list(map(int, input().split()))
    for i in range(0, E * 2, 2): # arr[i] ---> arr[i + 1]
        p, c = arr[i], arr[i + 1]

        if L[p]: R[p] = c
        else: L[p] = c
        P[c] = p

    # 깊이 우선
    def traverse(v):
        if v == 0: return 0
        return traverse(L[v]) + traverse(R[v]) + 1

    print(traverse(N))

    # 너비 우선
    # ans = 0
    # Q = [N]
    # while Q:
    #     v = Q.pop(0)
    #     if v == 0: continue
    #     ans += 1
    #     Q.append(L[v])
    #     Q.append(R[v])
    #
    # print(ans)
