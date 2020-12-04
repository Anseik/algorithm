import sys
sys.stdin = open('SWEA_중위순회.txt')


def in_order(node):
    if node:
        in_order(tree[node][0])
        result.append(tree[node][3])
        in_order(tree[node][1])

T = 10
for tc in range(1, T+1):
    N = int(input())
    info = [input().split() for _ in range(N)]

    for i in range(N):
        for j in range(len(info[i])):
            if j != 1:
                info[i][j] = int(info[i][j])

    tree = [[0] * 4 for _ in range(N + 1)]

    for i in range(N):
        v = info[i][0]
        for j in range(1, len(info[i])):
            t = info[i][j]
            if j == 1:
                tree[v][3] = t
            else:
                if tree[v][0] == 0:
                    tree[v][0] = t
                    tree[t][2] = v
                else:
                    tree[v][1] = t
                    tree[t][2] = v

    result = []
    in_order(1)
    answer = "".join(result)
    print("#{} {}".format(tc, answer))