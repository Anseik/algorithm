import sys
sys.stdin = open('노드의 합.txt')

def post_order(idx):
    if idx > N:
        return
    v1 = post_order(2 * idx)
    v2 = post_order(2 * idx + 1)
    if v1 and v2: # 양쪽 자식 다 있을 때
        tree[idx] = v1 + v2
    elif v1: # 왼쪽 자식만 있을 때
        tree[idx] = v1
    return tree[idx]

T = int(input())
for tc in range(1, T + 1):
    # N : 노드의개수, M : 리프의 개수, L: 값을 출력할 노드 번호
    N, M, L = map(int, input().split())

    tree = [0] * (N + 1)
    for i in range(M):
        node, num = map(int, input().split())
        tree[node] = num
    # print(tree)

    post_order(1)
    result = tree[L]
    print("#{} {}".format(tc, result))