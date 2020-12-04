import sys
sys.stdin = open('swea_5248_그룹나누기.txt')

def find_set(x):
    if x == parent[x]:
        return x

    p = find_set(parent[x])
    parent[x] = p
    return p

def union(x, y):
    global group
    a, b = find_set(x), find_set(y)
    if a != b:
        parent[b] = a
        group -= 1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    # print(N, M)
    # print(arr)

    parent = list(range(N + 1))
    # print(parent)

    group = N
    for i in range(M):
        f1, f2 = arr[2 * i], arr[2 * i + 1]
        # print(f1, f2)
        union(f1, f2)

    print('#{} {}'.format(tc, group))

