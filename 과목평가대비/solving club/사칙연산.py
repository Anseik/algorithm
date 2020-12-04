import sys
sys.stdin = open('사칙연산.txt')

cal = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

def post_order(v):
    if not v: return 0
    l = post_order(tree[v][1])
    r = post_order(tree[v][2])
    if tree[v][0] in cal:
        ope = tree[v][0]
        return cal[ope](l, r)
    return tree[v][0]

T = 10
for tc in range(1, T + 1):
    N = int(input())

    # 값, 왼쪽, 오른쪽, 부모
    tree = [[0] * 4 for _ in range(N + 1)]
    for _ in range(N):
        node = input().split()
        if len(node) == 4:
            p, l, r = int(node[0]), int(node[2]), int(node[3])
            tree[p][0] = node[1]
            tree[p][1], tree[p][2] = l, r
            tree[l][3] = tree[r][3] = p
        else: # 길이가 2일 경우
            p, val = int(node[0]), int(node[1])
            tree[p][0] = val
    # print(tree)

    result = int(post_order(1))
    print("#{} {}".format(tc, result))
