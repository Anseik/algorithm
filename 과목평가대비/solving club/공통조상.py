import sys
sys.stdin = open('공통조상.txt')

def post_order(v):
    global cnt
    if v:
        post_order(tree[v][0])
        post_order(tree[v][1])
        cnt += 1

T = int(input())
for tc in range(1, T + 1):
    V, E, node1, node2 = map(int, input().split())
    edges = list(map(int, input().split()))
    # print(V, E, node1, node2)
    # print(edges)

    tree = [[0] * 3 for _ in range(V + 1)]
    for i in range(E):
        p, c = edges[2 * i], edges[2 * i + 1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c
        tree[c][2] = p
    # print(tree)

    node1_parent = []
    cur = node1
    parent = tree[cur][2]
    while parent:
        node1_parent.append(parent)
        cur = parent
        parent = tree[cur][2]
    # print(node1_parent)

    cur = node2
    parent = tree[cur][2]
    common_parent = 0
    while parent:
        if parent in node1_parent:
            common_parent = parent
            break
        else:
            cur = parent
            parent = tree[cur][2]
    # print(common_parent)

    cnt = 0
    post_order(common_parent)
    print("#{} {} {}".format(tc, common_parent, cnt))