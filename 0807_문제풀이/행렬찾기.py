# 행렬 접근하기
# 1 2 0 0 0 1
# 2 1 0 0 0 0
# 0 0 1 2 3 2
# 0 0 3 2 1 3
# 0 0 2 1 3 4
# 0 0 0 0 0 0
# 행렬을 입력 받아서
# 행렬에 포함되어 있는 sub_matrix 크기 계산하기
# matrix 순회하면서 0이 아닌 위치 찾기
# 가로, 세로 길이 구하기
# 표시한 영역은 0으로 다 바꾸기

import sys
sys.stdin = open('행렬찾기.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    # for row in matrix:
    #     print(*row)


    sub = []
    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 0:
                # 행의 길이, 열의 길이
                x = 0 # 행의 길이
                for k in range(i, N):
                    if matrix[k][j] != 0:
                        x += 1
                    else:
                        break

                y = 0 # 열의 길이
                for k in range(j, N):
                    if matrix[i][k] != 0:
                        y += 1
                    else:
                        break

                # 표시한 영역 0으로 다 바꾸기
                for l in range(i, i+x):
                    for m in range(j, j+y):
                        matrix[l][m] = 0

                sub.append((x, y, x * y))

    # print(sub)

    # print(sub_matrix)
    # 부분행렬의 개수 카운트
    # 크기를 비교하여 작은거부터 정렬
    # 크기가 같으면 행이 작은것이 앞으로오게
    # 정렬된 sub_matrix를 순회하며 행과 열의 크기를 출력
    for n in range(len(sub)-1, 0, -1):
        for o in range(n):
            if sub[o][2] > sub[o + 1][2]:
                sub[o], sub[o + 1] = sub[o + 1], sub[o]
            elif sub[o][2] == sub[o + 1][2]:
                if sub[o][0] > sub[o + 1][0]:
                    sub[o], sub[o + 1] = sub[o + 1], sub[o]

    # print(sub)
    result = []
    cnt = 0
    for p in range(len(sub)):
        cnt += 1
        result.append(sub[p][0])
        result.append(sub[p][1])
    result.insert(0, cnt)

    print('#%d' %tc, end=" ")
    for q in result:
        print(q, end=" ")
    print()

