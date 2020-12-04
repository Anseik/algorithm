import sys
sys.stdin = open('swea_5249_최소신장트리_solution.txt')

# def make_set(x):
#     p[x] = x

def find_set(x):
    if p[x] != x:
        p[x] = find_set(p[x])

    return p[x]

def union(x, y):
    p[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    edges.sort(key = lambda x: x[2]) # 가중치를 기준으로 오름차순 정렬
    # print(edges)

    # p = [0] * (V + 1)
    # for i in range(V + 1):
    #     make_set(i)

    p = list(range(V + 1))

    ans = 0
    cnt = 0 # 선택한 간선의 개수, V개가 선택되면 종료
    idx = 0

    while cnt < V:
        x = edges[idx][0]
        y = edges[idx][1]

        if find_set(x) != find_set(y): # 같은 그룹이 아니면
            union(x, y)
            cnt += 1
            ans += edges[idx][2]

        idx += 1

    print('#{} {}'.format(tc, ans))

