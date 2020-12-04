import sys
sys.stdin = open('subtree.txt')

def post_order(v):
    global cnt
    if not v: return
    post_order(tree[v][0])
    post_order(tree[v][1])
    cnt += 1

T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    V = E + 1
    edges = list(map(int, input().split()))

    # 왼쪽자식, 오른쪽자식, 부모
    tree = [[0] * 3 for _ in range(V + 1)]
    for i in range(E):
        p, c = edges[2 * i], edges[2 * i + 1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c
        tree[c][2] = p

    cnt = 0
    post_order(N)

    # print(tree)
    print("#{} {}".format(tc, cnt))
