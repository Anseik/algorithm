import sys
sys.stdin = open('swea_5248_그룹나누기_solution.txt')


def make_set(x):
    p[x] = x


def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])
    return p[x]


def union(x, y):
    p[find_set(y)] = find_set(x)


T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    team = [False] * (V + 1)
    edge = list(map(int, input().split()))

    p = [0] * (V + 1)

    for i in range(V + 1):
        make_set(i)

    for i in range(E):
        A = edge[2 * i]
        B = edge[2 * i + 1]
        union(A, B)

    for i in range(1, V + 1):
        find_set(i)

    print('#{} {}'.format(tc, len(set(p)) - 1))
