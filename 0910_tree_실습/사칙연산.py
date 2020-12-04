import sys
sys.stdin = open('사칙연산.txt')

def post_order(v): # 후위 순회
    if v:
        v1 = post_order(tree[v][1])
        v2 = post_order(tree[v][2])
        if v1 and v2:
            return cal[tree[v][0]](v1, v2)
        return tree[v][0]

T = 10
for tc in range(1, T + 1):
    N = int(input())
    info = [input().split() for _ in range(N)]
    # print(info)

    # 트리 초기화 [0번: value(연산자 또는 값), 1번: 왼쪽자식, 2번 : 오른쪽 자식, 3번: 부모]
    tree = [[0] * 4 for _ in range(N + 1)]

    # 사칙연산
    cal = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }

    # 트리 구성
    for i in range(N):
        node, value, *child = info[i]
        v = int(node)
        if value in cal:
            tree[v][0] = value # 연산자이면 value를 그냥 넣고

            # value가 연산자 일때는 항상 2개의 자식이 있으므로
            lc, rc = int(child[0]), int(child[1])

            # 자식정보
            tree[v][1], tree[v][2] = lc, rc

            # 부모정보
            tree[lc][3] = tree[rc][3] = v

        else:
            tree[v][0] = int(value) # 피연산자이면 value를 형변환해서 넣고

    # print(tree)

    result = int(post_order(1))
    print("#{} {}".format(tc, result))