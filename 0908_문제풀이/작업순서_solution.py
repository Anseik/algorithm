import sys
sys.stdin = open('작업순서.txt')

T = 10
for tc in range(1,T + 1):
    V, E = map(int, input().split())
    edges = list(map(int, input().split()))

    # 선행작업을 저장하는 행렬
    prev_arr = [[0] * (V + 1) for _ in range(V + 1)]
    for i in range(E):
        s, e = edges[2 * i], edges[2 * i + 1]
        prev_arr[e][s] = 1
    # print(prev_arr)

    # 작업순서를 저장할 리스트
    order_list = list()

    # 노드들을 순회하면서, order_list에 넣을지를 결정
    # 선행작업 목록 확인해서, 선행작업들이 모두 order_list에 들어가 있거나 선행작업이 없으면
    # 선행작업이 완료된 상황 --> order_list에 추가한다.
    # order_list에 모든 노드들이 들어갈 때까지 반복
    while len(order_list) < V:
        for i in range(1, V + 1):
            if i not in order_list: # i번째 노드 작업하지 않음.
                # i번 노드의 선행작업이 모두 이루어졌는지 확인
                # 선행작업 prev_arr 확인
                for j in range(1, V + 1):
                    # j번 작업이 i번 작업의 선행작업인데, j가 order_list에 없으면,
                    if prev_arr[i][j] == 1 and j not in order_list:
                        # i는 작업하면 안됨
                        break
                else: # break가 안걸리면, 선행작업이 완료된 상황
                    order_list.append(i)

    print("#{}".format(tc), *order_list)
