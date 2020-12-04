import sys
sys.stdin = open('노드의합.txt')

def post_order(v):
    if v > N: return 0
    l = post_order(2 * v)
    r = post_order(2 * v + 1)
    tree[v] = tree[v] + l + r
    return tree[v]


T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for _ in range(M):
        node, number = map(int, input().split())
        tree[node] = number

    post_order(1)
    result = tree[L]
    print("#{} {}".format(tc, result))