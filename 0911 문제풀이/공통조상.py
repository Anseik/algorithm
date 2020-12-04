import sys
sys.stdin = open('공통조상.txt')

def post_order(v):
    if v == 0: return 0
    l = post_order(tree[v][0])
    r = post_order(tree[v][1])
    return l + r + 1

T = int(input())
for tc in range(1, T + 1):
    V, E, node1, node2 = map(int, input().split())
    edges = list(map(int, input().split()))
    tree = [[0] * 3 for _ in range(V + 1)]

    for i in range(E):
        p, c = edges[2 * i], edges[2 * i + 1]
        if tree[p][0] == 0:
            tree[p][0] = c
        else:
            tree[p][1] = c
        tree[c][2] = p
    # print(tree)

    # node1의 조상을 모두 찾아 리스트로 만든다.
    p_node1 = []
    cur = node1
    parent = tree[cur][2]
    while parent:
        p_node1.append(parent)
        cur = parent
        parent = tree[cur][2]

    # node2의 조상을 하나씩 찾으며 그 조상이 node1의 조상 리스트에 있으면 공통조상이다.
    c_parent = 0 # 공통조상
    cur = node2
    parent = tree[cur][2]
    while parent:
        if parent in p_node1:
            c_parent = parent
            break
        cur = parent
        parent = tree[cur][2]

    cnt_node = post_order(c_parent)

    print("#{} {} {}".format(tc, c_parent, cnt_node))