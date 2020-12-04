import sys
sys.stdin = open('행렬찾기.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # print(N)
    # print(matrix)

    # sub_matrix의 정보를 저장할 리스트가 필요하다.(행, 열, 크기)
    # 순회하면서 0이 아닌것을 만나면 행의 길이와 열의길이를 확인하면서 sub_matrix를 순회하고
    # 순회 하면서 지나간 곳은 0으로 변경한다.
    sub_matrix = []
    for r in range(N):
        for c in range(N):
            if matrix[r][c] != 0:
                row = 0
                col = 0
                # i = r
                # j = c
                # while i < N and matrix[i][c] != 0:
                #     row += 1
                #     i += 1
                # while j < N and matrix[r][j] != 0:
                #     col += 1
                #     j += 1

                for a in range(r, N):
                    if matrix[a][c] != 0:
                        row += 1
                    else:
                        break

                for b in range(c, N):
                    if matrix[r][b] != 0:
                        col += 1
                    else:
                        break

                # for k in range(row):
                #     for l in range(col):
                #         matrix[r+k][c+l] = 0

                for k in range(r, r+row):
                    for l in range(c, c+col):
                        matrix[k][l] = 0

                sub_matrix.append((row, col, row*col))

    # 선택정렬
    for m in range(len(sub_matrix)-1):
        min = m
        for n in range(m, len(sub_matrix)):
            if sub_matrix[n][2] < sub_matrix[min][2]:
                min = n
            elif sub_matrix[n][2] == sub_matrix[min][2]:
                if sub_matrix[n][0] < sub_matrix[min][0]:
                    min = n
        sub_matrix[m], sub_matrix[min] = sub_matrix[min], sub_matrix[m]

    print("#{}".format(tc), end=" ")
    print(len(sub_matrix), end=" ")
    for sub in sub_matrix:
        print(sub[0], sub[1], end=" ")
    print()



