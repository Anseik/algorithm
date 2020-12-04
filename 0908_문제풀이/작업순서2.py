import sys
sys.stdin = open('작업순서.txt')

T = 10
for tc in range(1, T+1):
    V, E = map(int, input().split())
    rel = list(map(int, input().split()))
    # print(V, E)
    # print(rel)

    # 선행 조건 리스트(특정 노드의 선행조건을 확인하기 위한 리스트)
    G = [[] for _ in range(V + 1)]
    for i in range(E):
        before, after = rel[2 * i], rel[2 * i + 1]
        G[after].append(before) # before와 after를 반대로 집어넣는게 포인트!!
    # print(G)
    # G[1]의 요소가 2, 3이라면 1번 노드의 선행조건이 2,3이라는 의미

    # 방문체크
    visit = [0] * (V + 1)

    result = []

    n = 0
    while n != V:
        for i in range(1, V + 1):
            if visit[i]: # 이미 처리한 일이라면 다른 노드로
                continue
            for j in G[i]:
                if not visit[j]: # 선행조건을 완료하지 않았으면 다른 노드로
                    break
            else: # 모든 선행조건이 완료되었으면 그 일을 처리한다.
                visit[i] = 1
                result.append(i)
                n += 1

    print("#{}".format(tc), *result)